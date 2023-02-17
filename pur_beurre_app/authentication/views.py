from django.conf import settings
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import View
from authentication import forms
from authentication.models import User


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
    login_url = settings.LOGIN_URL
    
    def get(self, request, id):
        user = User.objects.get(id=id)
        return render(request, self.template_name, context={'user': user})

def mentions_legals(request):
    return render(request, 'authentication/mentions_legals.html')
