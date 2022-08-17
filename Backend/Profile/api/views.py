from django.http.response import JsonResponse
from rest_framework import generics, viewsets
from .serializers import ProfileSerializer
from Profile.models import ProfileModel
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes, permission_classes
from django.http import HttpResponse
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from social_django.utils import psa
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
import requests
import base64
import json
# DetailView CreateView FormView


class ProfileRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'  # slug, id # url(r'?P<pk>\d+')
    serializer_class = ProfileSerializer

    def get_queryset(self):
        obj = ProfileModel.objects.filter(user=self.request.user)
        obj[0].check_credit_month()
        return obj

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class MyProfileView(viewsets.ModelViewSet):
    model = ProfileModel
    serializer_class = ProfileSerializer
    queryset = ProfileModel.objects.all()

    def get_object(self):
        obj = ProfileModel.objects.get(user=self.request.user)
        obj.check_credit_month()
        return obj

    def list(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


@api_view(['POST'])
def patch_meeting(request):
    #first_name = request.data.get('first_name')
    #last_name = request.data.get('last_name')
    #email = request.data.get('email')
    #bio = request.data.get('bio')
    #location = request.data.get('location')
    threshold = request.data.get('threshold')
    language = request.data.get('language')

    #user_obj = User.objects.get(id=request.user.id)
    profile_obj = ProfileModel.objects.get(user=request.user)

    #commend out, DONT NEED TO CHANGE THESE
    #user_obj.first_name = first_name
    #user_obj.last_name = last_name
    #user_obj.email = email
    #user_obj.save()

    #profile_obj.bio = bio
    #profile_obj.location = location

    profile_obj.threshold = threshold
    profile_obj.language = language
    profile_obj.save()

    return Response({"message": "OK"})


@api_view(['GET'])
def zoom_active(request):
    user_obj = ProfileModel.objects.get(user=request.user)
    zoom_acess_token = user_obj.zoom_access_token
    zoom_refresh_token = user_obj.zoom_refresh_token

    if (zoom_acess_token != '' and zoom_refresh_token != ''):
        msg = 'true'
    else:
        msg = 'false'

    return Response({"active": msg})


@api_view(['GET'])
# @permission_classes([permissions.AllowAny])
def zoom_auth(request):

    code = request.data.get('code', '')

    # call zoom api to get access / refresh tokens
    encoded = base64.b64encode(
        (settings.ZOOM_ID+':'+settings.ZOOM_SECRET).encode())

    headers = {
        'Authorization': 'Basic '+str(encoded),
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect': 'https://app.wudpecker.io/settings',
    }

    res = requests.post('https://zoom.us/oauth/token',
                        data=data, headers=headers)
    data = json.loads(res.text)

    user_obj = ProfileModel.objects.get(user=request.user)
    user_obj.zoom_access_token = res.text
    user_obj.zoom_refresh_token = "hello"
    user_obj.save()

    return Response({"request": "ok"})


@api_view(['POST'])
def reset_password(request):
    old_password = request.data.get('old')
    new_password = request.data.get('new')

    user_obj = User.objects.get(id=request.user.id)

    if user_obj.check_password(old_password):
        user_obj.set_password(new_password)
        user_obj.save()
        return Response({"message": "OK"})

    return Response({"message": "ERROR"}, status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def new_sign_up_view(request):
    if request.method == 'POST':
        username = request.data.get('email')
        email = request.data.get('email')
        password = request.data.get('password')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        # bio = request.data.get('bio')
        # location = request.data.get('location')

        # create a user object (profile object will be created automatically)
        new_user = User.objects.create_user(username, email, password)
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.save()

        # edit profile object with these entries
        new_profile = ProfileModel.objects.get(user=new_user)
        # new_profile.bio = bio
        # new_profile.location = location
        new_profile.save()

        # return Response({"message": "Done", "data": engaged_val})
        response = HttpResponse()
        response.status_code = 200
        response['user_id'] = new_profile.id
        return response

    return Response({"message": "Why you doing GET request bruh?"})


class SocialSerializer(serializers.Serializer):
    """
    Serializer which accepts an OAuth2 access token.
    """
    access_token = serializers.CharField(
        allow_blank=False,
        trim_whitespace=True,
    )


@api_view(http_method_names=['POST'])
@permission_classes([permissions.AllowAny])
@psa()
def exchange_token(request, backend):
    serializer = SocialSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        # This is the key line of code: with the @psa() decorator above,
        # it engages the PSA machinery to perform whatever social authentication
        # steps are configured in your SOCIAL_AUTH_PIPELINE. At the end, it either
        # hands you a populated User model of whatever type you've configured in
        # your project, or None.
        user = request.backend.do_auth(
            serializer.validated_data['access_token'])

        if user:
            # if using some other token back-end than DRF's built-in TokenAuthentication,
            # you'll need to customize this to get an appropriate token object

            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            return Response({
                'token': token,
            })

        else:
            return Response(
                {'errors': {'token': 'Invalid token'}},
                status=status.HTTP_400_BAD_REQUEST,
            )
