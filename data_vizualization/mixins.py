from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import UserPassesTestMixin
from userhandling.models import Profile


class FressnapfClients(UserPassesTestMixin):
    def test_func(self):
        user_profile = get_object_or_404(Profile, user = self.request.user)

        return user_profile.client.name == "Fressnapf"

    def handle_no_permission(self):
        return HttpResponseForbidden("You do not have permission to access this page.")
