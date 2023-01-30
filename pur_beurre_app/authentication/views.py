from django.conf import settings
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import View
from authentication import forms
from authentication.models import User


@login_required
def home(request):
    return render(request, 'authentication/home.html', )

def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', context={'form': form})

class LoginPageView(View):
    template_name = 'authentication/login.html'
    form_class = forms.LoginForm
    
    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})
        
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        message = 'Login failed!'
        return render(request, self.template_name, context={'form': form, 'message': message})

def user_profile(request, id):
    user = User.objects.get(id=id)
    return render(request, 'authentication/user_profile.html', context={'user': user})

def mentions_legals(request):
    return render(request, 'authentication/mentions_legales.html')
