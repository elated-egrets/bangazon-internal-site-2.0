from website.forms import UserForm
from django.shortcuts import render

from website.models import Profile


def profile_view(request):
   view_profile = Profile.objects.all()
   template_name = 'profile/profile.html'
   return render(request, template_name, {'profiles': view_profile})