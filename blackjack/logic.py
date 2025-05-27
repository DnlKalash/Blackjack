from django.conf import settings
import random as rn

class BlackjackLogic:
    def __init__(self, request):
        self.session = request.session
        self.game = self.session.get(settings.BLACKJACK_SESSION_ID)

        if not self.game:
            current_balance = 1000
            self.game = self.create_new_game(balance=current_balance)
        else:
            current_balance = self.game.get('balance', 1000)
            defaults = {
                'created_deck': [],
                'player_cards': [],
                'dealer_cards': [],
                'player_score': 0,
                'dealer_score': 0,
                'is_over': False,
                'winner': None,
                'balance': current_balance,
                'bet': 0,
            }
            for key, value in defaults.items():
                self.game.setdefault(key, value)

        self.save_game()

    def save_game(self):
        self.session[settings.BLACKJACK_SESSION_ID] = self.game
        self.session.modified = True

    def create_new_game(self, balance=1000):
        suits = ['♠', '♥', '♦', '♣']
        ranks = list(range(1, 12))
        created_deck = [(rank, suit) for suit in suits for rank in ranks]
        rn.shuffle(created_deck)
        return {
            'created_deck': created_deck,
            'player_cards': [],
            'dealer_cards': [],
            'player_score': 0,
            'dealer_score': 0,
            'is_over': False,
            'winner': None,
            'balance': balance,
            'bet': 0,
        }

    def first_bet(self, amount=None):
        bet = amount if amount is not None and amount > 0 else 10
        if bet > self.game['balance']:
            bet = self.game['balance']  

        self.game['bet'] = bet
        self.game['balance'] -= bet
        self.game['player_cards'] = self.game['created_deck'][:2]
        self.game['dealer_cards'] = self.game['created_deck'][2:4]
        self.game['created_deck'] = self.game['created_deck'][4:]
        self.update_scores('player', self.game['player_cards'])
        self.update_scores('dealer', self.game['dealer_cards'])
        self.save_game()

    def hit(self):
        if self.game['is_over']:
            return
        card = self.draw_card()
        if card:
            self.game['player_cards'].append(card)
            score = self.update_scores('player', self.game['player_cards'])
            if score > 21:
                self.determine_winner()
                self.game['is_over'] = True
            self.save_game()

    def stand(self):
        dealer_score = self.game['dealer_score']
        player_score = self.game['player_score']
        while dealer_score < player_score and dealer_score < 21:
            card = self.draw_card()
            if not card:
                break
            self.game['dealer_cards'].append(card)
            dealer_score = self.update_scores('dealer', self.game['dealer_cards'])
        self.determine_winner()
        self.game['is_over'] = True
        self.save_game()

    def draw_card(self):
        return self.game['created_deck'].pop(0) if self.game['created_deck'] else None

    def update_scores(self, who, cards):
        score = self.calculate_score(cards)
        self.game[f'{who}_score'] = score
        return score

    def calculate_score(self, cards):
        score = 0
        aces = 0
        for rank, suit in cards:
            if rank == 1:
                score += 11
                aces += 1
            elif rank >= 10:
                score += 10
            else:
                score += rank
        while score > 21 and aces:
            score -= 10
            aces -= 1
        return score

    def determine_winner(self):
        p, d = self.game['player_score'], self.game['dealer_score']
        if p > 21:
            self.game['winner'] = 'dealer'
        elif d > 21 or p > d:
            self.game['winner'] = 'player'
            self.game['balance'] += int(self.game['bet'] * 1.5)
        elif p < d:
            self.game['winner'] = 'dealer'
        else:
            self.game['winner'] = 'draw'
            self.game['balance'] += self.game['bet']

    def reset(self):
        current_balance = self.game.get('balance', 1000)
        self.game = self.create_new_game(balance=current_balance)
        self.save_game()
