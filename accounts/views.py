from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import SignupForm


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    else:
        form = SignupForm()
    return render(request, 'authentication.html', {'form' : form, 'is_signup': True})

class signin(LoginView):
    template_name = 'authentication.html'
    def get_success_url(self):
        return reverse_lazy('home')

#@method_decorator(login_required, name='dispatch')
class signout(LogoutView):
    next_page = 'signin'