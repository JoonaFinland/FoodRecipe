from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def verification_view(request):
    new_data = {
        "associatedApplications": [
            {
                "applicationId": "d100b1af-6439-4b80-bb74-f16420ee4fcb"
            }
        ]
    }
    return JsonResponse(new_data)
