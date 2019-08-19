from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json

from bank_details.models import Banks
# Create your views here.
@csrf_exempt
def get_bank_details(request):
    print(request.body)

    received_json_data = json.loads(request.body)
    input_Ifsc = str(received_json_data['ifsc'])
    bank_data = Banks.objects.get(ifsc=input_Ifsc)
    return JsonResponse({'ifsc': bank_data.ifsc,
                         'bank_id' : bank_data.bank_id,
                         'branch': bank_data.branch,
                         'address' : bank_data.address,
                         'city' :  bank_data.city,
                         'district' : bank_data.district,
                         'state' : bank_data.state,
                         'bank_name' : bank_data.bank_name})