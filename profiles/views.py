from django.shortcuts import render, get_object_or_404, reverse
from .models import UserProfile
from .forms import ProfileForm

def view_profile(request):
    """
    Display an individual :model:UserProfile if this exists
    """
    queryset = UserProfile.objects.all()

    has_profile=False

    if request.method == "POST":
        profile_form = ProfileForm(data=request.POST)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            comment.save()


    # display profile as a form - update if it exists, create if not
    try:
        profile = get_object_or_404(queryset, username=request.user)
    except:
        # profile_form = ProfileForm()
        # context_to_render = {"profile_form": profile_form,
        #     "has_profile": has_profile,
        # }
        profile_form = profile.ProfileForm()

    else:
        # display profile if one exists for logged-in user
        has_profile=True
        profile_form = ProfileForm(firstname=profile.firstname, 
            lastname=profile.lastname,
            bio=profile.bio)
        context_to_render = {"profile": profile,
            "profile_form": profile_form,
            "has_profile": has_profile,
        }

    

    return render(
        request,
        "profiles/view_profile.html",
        {"profile": profile,
            "profile_form": profile_form,
            "has_profile": has_profile,
        },
    )


