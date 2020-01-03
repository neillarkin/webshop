from django.conf.urls import url, include
from accounts.views import logout, login, registration, user_profile
from accounts import url_reset


"""URL Patterns route URLs to Views"""
"""Each URLPattern line contians three paremeters: 
    the actual URL, 
    the view function, 
    and the name for that function for referencing in templates expressions"""
urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="registration"),
    url(r'^profile/', user_profile, name="profile"),
    url(r'^password-reset/', include(url_reset))
]