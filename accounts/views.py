from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from . import forms
from orders.models import Order


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    else:
        form = forms.SignupForm()
    return render(request, 'authentication.html', {'form' : form, 'is_signup': True})

class signin(LoginView):
    template_name = 'authentication.html'
    def get_success_url(self):
        return reverse_lazy('home')

#@method_decorator(login_required, name='dispatch')
class signout(LogoutView):
    next_page = 'signin'

@login_required
def profile(request):
    user = request.user
    orders = Order.objects.filter(user=user)

    if request.method == 'POST':
        user_form = forms.EmailChangeForm(request.POST, instance=user)
        pass_form = forms.PassChangeForm(user, request.POST)
        if user_form.is_valid():
            user_form.save()
        if pass_form.is_valid():
            pass_form.save()
            update_session_auth_hash(request, pass_form.user)
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