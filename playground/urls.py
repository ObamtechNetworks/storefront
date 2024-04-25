from django.urls import path  # the path function from django.urls
from . import views  # import our views module so we can reference our view functions

# define URL CONFIGURATION
# this urlpattern data structure is what django looks for
# this is a list that defines the different urlpatterns :endpoints for our app
urlpatterns = [
    # the path function takes about 3 parameters which are basically for defining the url patterns
    # route -> a string which is the endpoint url
    # view -> the view function to call from the views module
    # Returns a URLPattern object
    path('hello/', views.say_hello)
]
