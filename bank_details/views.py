from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import json
from django.views.decorators.csrf import csrf_exempt
import urllib3
import requests
from bank_details.models import Banks

@csrf_exempt
def run(request):
    # print(request.body)
    received_json_data = json.loads(request.body)
    username = str(received_json_data['username'])
    password = str(received_json_data['password'])
    ifsc = str(received_json_data['ifsc'])
    http = urllib3.PoolManager()

    r = http.request('POST', 'https://fyle-task1.herokuapp.com/api/token/',
                     # headers={'Content-Type': 'application/json'},
                     fields={'username': username, 'password' : password})
    # print(r.data)
    tokens = json.loads(r.data)
    if('access' in tokens):
        access_token = str(tokens['access'])
        # print(access_token)
        data = {'ifsc':ifsc}
        hed = {'Authorization': 'Bearer ' + access_token}
        response = requests.get('https://fyle-task1.herokuapp.com/bank_details/', headers={'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token},json=data)
        res = response.json()
        if('ifsc' in res):
            return JsonResponse(res)
        else:
            return JsonResponse({"detail": "Authentication credentials were not provided."})
    else:
        return JsonResponse({"detail": "No active account found with the given credentials"})
    return HttpResponse(1)



# Code with JWT Authentication
class Bank_details(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        print(request.body)
        received_json_data = json.loads(request.body)
        input_Ifsc = str(received_json_data['ifsc'])
        bank_data = Banks.objects.get(ifsc=input_Ifsc)
        return JsonResponse({'ifsc': bank_data.ifsc,
                             'bank_id': bank_data.bank_id,
                             'branch': bank_data.branch,
                             'address': bank_data.address,
                             'city': bank_data.city,
                             'district': bank_data.district,
                             'state': bank_data.state,
                             'bank_name': bank_data.bank_name})


# Code with out JWT Authentication

# @csrf_exempt
# def get_bank_details(request):
#     print(request.body)
#
#     received_json_data = json.loads(request.body)
#     input_Ifsc = str(received_json_data['ifsc'])
#     bank_data = Banks.objects.get(ifsc=input_Ifsc)
#     return JsonResponse({'ifsc': bank_data.ifsc,
#                          'bank_id' : bank_data.bank_id,
#                          'branch': bank_data.branch,
#                          'address' : bank_data.address,
#                          'city' :  bank_data.city,
#                          'district' : bank_data.district,
#                          'state' : bank_data.state,
#                          'bank_name' : bank_data.bank_name})