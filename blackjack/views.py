from django.shortcuts import render
from .logic import BlackjackLogic
from main.views import jwt_required

def blackjack_view(request):
    logic = BlackjackLogic(request)

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'hit':
            logic.hit()
        elif action == 'stand':
            logic.stand()
        elif action == 'bet':
            bet_str = request.POST.get('bet_amount', '').strip()
            bet_amount = int(bet_str) if bet_str.isdigit() else 10
            logic.first_bet(bet_amount)
        elif action == 'play_again':
            logic.reset()

    context = {
        'game': logic.game,
        'balance': logic.game.get('balance', 0),
        'bet': logic.game.get('bet', 0),
    }

    return render(request, 'blackjack/game.html', context)

#test