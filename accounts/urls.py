from django.conf.urls import url, include
from accounts.views import logout, login, registration, user_profile, edit_profile, update_profile
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
    url(r'^edit-profile/', edit_profile, name="edit_profile"),
    url(r'^update-profile/', update_profile, name="update_profile"),
    url(r'^password-reset/', include(url_reset))
]