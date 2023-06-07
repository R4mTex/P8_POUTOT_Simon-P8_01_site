from django.conf import settings
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import View
from product.scripts.parser import Parser
from authentication import forms
from authentication.models import User

from django.http import HttpResponse  
from pur_beurre_app import settings  
from django.core.mail import send_mail  


@login_required
def home(request):
    return render(request, 'authentication/home.html', )


class Signup(View):
    template_name = 'authentication/signup.html'
    form_class = forms.SignupForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        return render(request, self.template_name, context={'form': form})


class Login(View):
    template_name = 'authentication/login.html'
    form_class = forms.LoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect(settings.LOGIN_REDIRECT_URL)
        return render(request, self.template_name, context={'form': form})


class User_profile(LoginRequiredMixin, View):
    template_name = 'authentication/user_profile.html'

    def get(self, request, id_user):
        user = User.objects.get(id=id_user)
        return render(request, self.template_name, context={'user': user})
    
    def post(self, request, id_user):
        user = User.objects.get(id=id_user)

        img = request.POST
        img_id = img['icon_avatar']
        img_src = {
            'icon_avatar_1': '/static/images/icon_avatar_1.png',
            'icon_avatar_2': '/static/images/icon_avatar_2.png',
            'icon_avatar_3': '/static/images/icon_avatar_3.png',
            'icon_avatar_4': '/static/images/icon_avatar_4.png',
            'icon_avatar_5': '/static/images/icon_avatar_5.png',
            'icon_avatar_6': '/static/images/icon_avatar_6.png',
            'icon_avatar_7': '/static/images/icon_avatar_7.png',
            'icon_avatar_8': '/static/images/icon_avatar_8.png',
            'icon_avatar_9': '/static/images/icon_avatar_9.png',
            'icon_avatar_10': '/static/images/icon_avatar_10.png',
            'icon_avatar_11': '/static/images/icon_avatar_11.png',
        }
        img_selected_src = img_src[img_id]
        
        user.profile_picture = img_selected_src
        user.save()
        return render(request, self.template_name, context={'user': user})


def mentions_legals(request):
    return render(request, 'authentication/mentions_legals.html')
