from website.forms import UserForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from website.models import Profile, Order

@login_required
def profile_view(request):
    '''View to access the profile along with user info thats auto populated by Django
    Returns:
        [GET] -- loading the user and profile information
    '''

    if request.method == 'GET':
        template_name = 'profile/profile.html'
        return render(request, template_name,)