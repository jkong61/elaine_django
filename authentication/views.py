from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.views.generic.edit import FormView
from .forms import RegisterForm

# Create your views here.

class RegisterPageView(FormView):
    template_name = 'registration/signup.html'

    # Pass the form to be used 
    form_class = RegisterForm

    # use lazy reverse to get the url name defined in settings
    success_url = reverse_lazy('core-index')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        # Form saves the data in into the Database
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')

        # Authenticate the user for use with the website
        user = authenticate(username=username, password=password)

        # Login the user into the session
        login(self.request, user)
        return super().form_valid(form)