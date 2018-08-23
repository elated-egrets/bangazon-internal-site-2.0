"""module: Edit Profile View
   author: Jonny Riggs
"""

from website.forms import UserForm, ProfileForm, ProfileUpdateForm, EditUserForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from website.models import Profile

@login_required
def edit_profile(request, pk):
    '''view to be able to edit and update the profile

    Arguments:
        request {[POST]} -- posting updated information for the user to be displayed on the profile.
        pk {user} -- user id on the profile

    Returns:
        [request] -- rendering the profile and user form along with the edit and update.
    '''

    # user = get_object_or_404(User,)
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == "POST":
        profile_form = ProfileUpdateForm(request.POST, instance=profile)
        user_form = EditUserForm(request.POST, instance=request.user)
        if profile_form.is_valid() and user_form.is_valid():
            user = user_form.save()
            profile = profile_form.save()
            return redirect('website:profile')
    else:
        profile_form = ProfileUpdateForm(instance=profile)
        user_form = EditUserForm(instance=request.user)

    return render(request, 'profile/edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})

