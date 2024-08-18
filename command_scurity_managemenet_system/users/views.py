from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import*
import json


@csrf_exempt
@require_http_methods(["GET"])
def user_list(request):
    users = list(Staff.objects.values())
    return JsonResponse(users, safe=False)


@csrf_exempt
@require_http_methods(["GET"])
def user_detail(request, pk):
    try:
        user = Staff.objects.get(pk=pk)
        return JsonResponse({
            'id': user.id,
            'dispositivo': user.dispositivo,
            'equipamento': user.equipamento,
            'veiculos': user.veiculos
        })
    except Staff.DoesNotExist:
        return HttpResponseNotFound(json.dumps({"error": "User not found"}))