# from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .form import ManufacturerSignUpForm,DistributorSignUpForm,RetailerSignUpForm,GovernmentBodySignUpForm,NormalUserSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User

def register(request):
    return render(request,'../templates/register.html')

class manufacturer_register(CreateView):
    model = User
    form_class = ManufacturerSignUpForm
    template_name = '../templates/manufacturer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class distributor_register(CreateView):
    model = User
    form_class = DistributorSignUpForm
    template_name = '../templates/distributor_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class retailer_register(CreateView):
    model = User
    form_class = RetailerSignUpForm
    template_name = '../templates/retailer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class governmentbody_register(CreateView):
    model = User
    form_class = GovernmentBodySignUpForm
    template_name = '../templates/governmentbody_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class normaluser_register(CreateView):
    model = User
    form_class = NormalUserSignUpForm
    template_name = '../templates/normaluser_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

def login_request(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")
    return render(request,'../templates/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')