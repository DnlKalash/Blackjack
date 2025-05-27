from django import forms

class GameActionForm(forms.Form):
    ACTIONS = [
        ('hit', 'Hit'),
        ('stand', 'Stand'),
        ('bet', 'Bet'),
        ('play_again', 'Play Again'),
    ]
    action = forms.ChoiceField(choices=ACTIONS, widget=forms.RadioSelect)