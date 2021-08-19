from whatwasthatbookcalled.profiles.models import Profile


def get_by_id(id):
    return Profile.objects.get(id=id)
