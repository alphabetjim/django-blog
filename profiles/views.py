from django.shortcuts import render, get_object_or_404, reverse
from .models import UserProfile
from .forms import ProfileForm

def view_profile(request):
    """
    Display an individual :model:UserProfile
    """
    queryset = UserProfile.objects.all()
    profile = get_object_or_404(queryset, user=request.user)

    return render(
        request,
        "profiles/view_profile.html",
        {"profile": profile},
    )

def update_profile(request):
    """
    Allow user to update their profile
    """
    if request.method == "POST":
        profile_form = ProfileForm(data=request.POST)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            comment.save()

    profile_form = profile.ProfileForm()
    return render(
        request,
        "profiles/view_profile.html",
        {"profile": profile,
            "profile_form": profile_form,
        },
    )