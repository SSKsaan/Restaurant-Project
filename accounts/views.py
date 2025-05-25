from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, logout
from django.contrib import messages
from . import forms
from orders.models import Order


# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        messages.error(request, 'You are already logged in.')
        return redirect('profile')
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('signin')
        else:
            messages.error(request, 'Account creation failed! Please try again.')
    else:
        form = forms.SignupForm()
    return render(request, 'authentication.html', {'form' : form, 'is_signup': True})

class signin(LoginView):
    template_name = 'authentication.html'

    def form_valid(self, form):
        messages.success(self.request, 'Logged in successfully!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Incorrect credentials! Please try again.')
        return super().form_invalid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.error(request, 'You are already logged in.')
            return redirect('profile')
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        return reverse_lazy('home')

def signout(request):
    logout(request)
    messages.info(request, 'Logged out successfully!')
    return redirect('signin')

@login_required
def profile(request):
    user = request.user
    orders = Order.objects.filter(user=user)
    email = user.email

    if request.method == 'POST':
        user_form = forms.EmailChangeForm(request.POST, instance=user)
        pass_form = forms.PassChangeForm(user, request.POST)
        if user_form.is_valid():
            if email != user.email:
                messages.success(request, 'Email changed successfully!')
                user_form.save()
        else:
            messages.error(request, 'Email change failed! Please try again.')
        if pass_form.is_valid():
            pass_form.save()
            update_session_auth_hash(request, pass_form.user)
            messages.success(request, 'Password changed successfully!')
        elif request.POST.get('old_password') or request.POST.get('new_password1'):
            messages.error(request, 'Password change failed! Please try again.')
            for field in pass_form.errors:
                for error in pass_form.errors[field]:
                    messages.error(request, error)
        return redirect('profile')
    else:
        user_form = forms.EmailChangeForm(instance=user)
        pass_form = forms.PassChangeForm(user)

    return render(request, 'profile.html', 
                  {
                      'user': user, 
                      'orders': orders, 
                      'user_form': user_form,
                      'password_form': pass_form
                  }
           )