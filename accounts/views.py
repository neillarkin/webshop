from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm


def index(request):
    """Returns the index.html page"""
    return render(request,  'index.html')

"""Before exectuing Logout, this Decorator checks if user is already logged in"""
@login_required 
def logout(request):
    """Logs the current user out and returns to Index page"""
    auth.logout(request)
    messages.success(request, "You are logged out")
    return redirect(reverse('index'))  
    # 'reverse' allows us to pass the name of a URL instead of the name of a View


def login(request):
    """Return a login page if user is already logged in"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
        
    """Create login form instance containing data posted on the forms UI"""
    if request.method == "POST":
        login_form = UserLoginForm(request.POST) # instance of class in forms.py 

        """Validate form then pass in keys from POST dictionary"""
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])

            """If a user exists then log them in and redirect to home page"""
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        """create empty object"""
        login_form = UserLoginForm()
        
    return render(request, 'login.html', {'login_form': login_form})
    """returned to Login.html template with key and value(form instance of 
    UserLoginForm class)"""


def registration(request):
    """If user is already authenticated then return to Home page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
        
    """If POST, then instanstiate variable using values in the POST request method"""
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        """If form is valid, then save the user data to database"""
        if registration_form.is_valid():
            registration_form.islower().save()

            """Reference the authenticated data to object called user """
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
                                     
            """Log user in """
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    
    """Return template and context dictionary with object as the value"""
    return render(request, 'registration.html', {
        "registration_form": registration_form})
        

def user_profile(request):
    """Retrieve user from database using email to get that specific user object"""
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {"profile": user})