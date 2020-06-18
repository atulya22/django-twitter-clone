# Django
from django.shortcuts import render, Http404, redirect
from django.http import HttpResponse, JsonResponse
from django.utils.http import is_safe_url
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
# DRF
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import (api_view,
                                       permission_classes,
                                       authentication_classes)
from rest_framework.permissions import IsAuthenticated

# General Python

from django.contrib.auth import get_user_model
from ..models import Profile

User = get_user_model()

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_follow_view(request, username, *args, **kwargs):
    me = request.user
    other_user_qs = User.objects.filter(username=username)

    if not other_user_qs.exists():
        return Response({}, status=404)
    other = other_user_qs.first()
    profile = other.profile
    data = request.data or {}

    action = data.get('action')
    if action == 'follow':
        profile.followers.add(me)
    elif action == 'unfollow':
        profile.followers.remove(me)
    else:
        pass

    current_followers_qs = profile.followers.all()

    return Response({"count": current_followers_qs.count()}, status=200)