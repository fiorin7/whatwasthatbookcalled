from whatwasthatbookcalled.landing.views import landing_page
from django.conf.urls import url


urlpatterns = [
    url(r"^$", landing_page, name="landing page"),
]
