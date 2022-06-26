from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.views import generic
from django.urls import reverse_lazy
from .forms import EditConfidentialForm,ProfilePageForm,EditProfilePageForm
from django.views.generic import DetailView,CreateView
from classroom.models import Profile

# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class=EditConfidentialForm
    template_name='registration/edit_profile.html'
    success_url = reverse_lazy('home_page')

    def get_object(self):
        return self.request.user #this is how u fill the inputs

class PasswordsChangeView(PasswordChangeView):
    form_class=PasswordChangeForm
    success_url=reverse_lazy('home_page')

class EditProfilePageView(generic.UpdateView):
    model=Profile
    form_class = EditProfilePageForm
    template_name='registration/edit_profile_page.html'
    success_url=reverse_lazy('home_page')

class CreateProfilePageView(CreateView):
    model=Profile
    template_name='registration/create_user_profile.html'
    form_class=ProfilePageForm

    def form_valid(self,form):
        form.instance.user= self.request.user
        return super().form_valid(form)
