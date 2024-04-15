# middleware.py

from django.http import HttpResponseForbidden
from django.urls import reverse

class AuthenticationMiddleware:
    PUBLIC_PATHS = ['/public/']  # Define paths that do not require authentication

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the requested path is in the public paths list
        if request.path_info in self.PUBLIC_PATHS:
            # If it's a public path, allow the request to proceed
            return self.get_response(request)
        
        # If it's not a public path, check if the user is authenticated
        if request.user.is_authenticated:
            # If the user is authenticated, allow the request to proceed
            return self.get_response(request)
        else:
            # If the user is not authenticated, redirect to the login page
            return HttpResponseForbidden("You are not authenticated. Please log in.")

