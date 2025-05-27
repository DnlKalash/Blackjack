import jwt as pyjwt
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.conf import settings
from functools import wraps
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .forms import UserForm
from .models import User
from django.urls import reverse




def htmlshablon(request):
    token = request.COOKIES.get('jwt')
    username = None

    if token:
        try:
            payload = pyjwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = payload.get('user_id')
            user = User.objects(id=user_id).first()
            if user:
                username = user.username
        except pyjwt.ExpiredSignatureError:
            pass
        except pyjwt.InvalidTokenError:
            pass

    return render(request, 'main/index.html', {'username': username})


def htmlregister(request):
    return render(request, 'main/register.html')


def htmllogin(request):
    return render(request, 'main/login.html')


def htmlgame(request):
    return render(request, 'main/game.html')




def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful!")
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserForm()
    return render(request, 'main/register.html', {'form': form})




def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects(username=username).first()

        if username and user and user.check_password(password):
            payload = {
                'user_id': str(user.id),
                'exp': datetime.utcnow() + timedelta(hours=24),
                'iat': datetime.utcnow(),
            }
            token = pyjwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
            response = redirect('htmlshablon')
            response.set_cookie('jwt', token, httponly=True, max_age=24 * 3600)
            return response
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'main/login.html', status=401)
    return render(request, 'main/login.html')



@require_POST
def logout(request):
    response = redirect('htmlshablon')
    response.delete_cookie('jwt')
    return response




def jwt_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        token = request.COOKIES.get('jwt')
        if not token:
            return redirect('login')

        try:
            payload = pyjwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = payload.get('user_id')
            user = User.objects(id=user_id).first()
            if not user:
                return redirect('login')
            request.user = user
        except pyjwt.ExpiredSignatureError:
            return redirect('login')
        except pyjwt.InvalidTokenError:
            return redirect('login')

        return view_func(request, *args, **kwargs)
    return wrapper
