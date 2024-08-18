#IMPORTAÇÕES:


from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Devices, Equipments, Vehicles
import json
import logging

logger = logging.getLogger(__name__)
#====================================================================

#GET - RENDER
#RENDER-DISPOSITIVOS
@csrf_exempt
@require_http_methods(["GET"])
def devices_list(request):
    dispositivos = list(Devices.objects.values())
    return JsonResponse(dispositivos, safe=False)
#RENDER-EQUIPAMENTOS

@csrf_exempt
@require_http_methods(["GET"])
def equipments_list(request):
    equipamentos = list(Equipments.objects.values())
    return JsonResponse(equipamentos, safe=False)
#RENDER - VEÍCULOS

@csrf_exempt
@require_http_methods(["GET"])
def vehicles_list(request):
    vehicles = list(Vehicles.objects.values())
    return JsonResponse(vehicles, safe=False)



#====================================================================
                                    #GET
#GET - DISPOSITIVOS:

@csrf_exempt
@require_http_methods(["GET"])
def devices_detail(request, pk):
    try:
        dispositivo = Devices.objects.get(pk=pk)
        return JsonResponse({
            'id': dispositivo.id,
            'nome': dispositivo.nome,
            'descricao': dispositivo.descricao,
        })
    except Devices.DoesNotExist:
        return HttpResponseNotFound(json.dumps({"error": "User not found"}))
#GET - EQUIPAMENTOS:

@csrf_exempt
@require_http_methods(["GET"])
def equipments_detail(request, pk):
    try:
        esquipamento = Equipments.objects.get(pk=pk)
        return JsonResponse({
            'id': esquipamento.id,
            'nome': esquipamento.nome,
            'descricao': esquipamento.descricao,
        })
    except Equipments.DoesNotExist:
        return HttpResponseNotFound(json.dumps({"error": "Equipment not found"}))
#GET - VEÍCULOS:

@csrf_exempt
@require_http_methods(["GET"])
def vehicles_detail(request, pk):
    try:
        veiculo = Vehicles.objects.get(pk=pk)
        return JsonResponse({
            'id': veiculo.id,
            'nome': veiculo.nome,
            'descricao': veiculo.descricao,
        })
    except Vehicles.DoesNotExist:
        return HttpResponseNotFound(json.dumps({"error": "Vehicle not found"}))
    

#====================================================================
            
                                                      #POST

#POST - DISPOSITIVOS
@csrf_exempt
@require_http_methods(["POST"])
def devices_create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            nome = data.get('nome')
            descricao = data.get('descricao')
            if not nome or not descricao:
                return HttpResponseBadRequest(json.dumps({"error": "Missing 'nome' or 'descricao' field"}), content_type='application/json')

            # Cria o dispositivo
            device = Devices.objects.create(nome=nome, descricao=descricao)

            return JsonResponse({'id': device.id, 'nome': device.nome, 'descricao': device.descricao}, status=201)
        except json.JSONDecodeError:
            return HttpResponseBadRequest(json.dumps({"error": "Invalid JSON"}), content_type='application/json')
        except Exception as e:
            logger.error(f"Error creating device: {str(e)}")
            return HttpResponseBadRequest(json.dumps({"error": "An error occurred"}), content_type='application/json')
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
#POST - EQUIPAMENTOS

@csrf_exempt
@require_http_methods(["POST"])
def equipments_create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            nome = data.get('nome')
            descricao = data.get('descricao')
            if not nome or not descricao:
                return HttpResponseBadRequest(json.dumps({"error": "Missing 'nome' or 'descricao' field"}), content_type='application/json')

            # Cria o dispositivo
            equipments = Equipments.objects.create(nome=nome, descricao=descricao)

            return JsonResponse({'id': equipments.id, 'nome': equipments.nome, 'descricao': equipments.descricao}, status=201)
        except json.JSONDecodeError:
            return HttpResponseBadRequest(json.dumps({"error": "Invalid JSON"}), content_type='application/json')
        except Exception as e:
            logger.error(f"Error creating device: {str(e)}")
            return HttpResponseBadRequest(json.dumps({"error": "An error occurred"}), content_type='application/json')
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
#POST - VEÍCULOS

@csrf_exempt
@require_http_methods(["POST"])
def vehicles_create(request):
    try:
        data = json.loads(request.body)
        veiculo = Vehicles.objects.create(
            nome=data['nome'],
            descricao=data['descricao'],
        )
        return JsonResponse({
            'id': veiculo.id,
            'nome': veiculo.nome,
            'descricao': veiculo.descricao,}, status=201)
    except (KeyError, TypeError, ValueError) as e:
        return HttpResponseBadRequest(json.dumps({"error": str(e)}))
    
#====================================================================

                                    #PUT
#PUT - DISPOSITIVOS
@csrf_exempt
@require_http_methods(["PUT"])
def devices_update(request, pk):
    try:
        dispositivo = Equipments.objects.get(pk=pk)
        data = json.loads(request.body)
        dispositivo.nome = data.get('nome', dispositivo.nome)
        dispositivo.descricao = data.get('descricao', dispositivo.descricao)
        dispositivo.save()
        return JsonResponse({
            'id': dispositivo.id,
            'nome': dispositivo.nome,
            'descricao': dispositivo.descricao,
        })
    except Devices.DoesNotExist:
        return HttpResponseNotFound(json.dumps({"error": "Device not found"}))
    except (KeyError, TypeError, ValueError) as e:
        return HttpResponseBadRequest(json.dumps({"error": str(e)}))

    
#PUT - EQUIPAMENTOS

@csrf_exempt
@require_http_methods(["PUT"])
def equipments_update(request, pk):
    try:
        equipamento = Equipments.objects.get(pk=pk)
        data = json.loads(request.body)

        equipamento.nome = data.get('nome', equipamento.nome)
        equipamento.descricao = data.get('descricao', equipamento.descricao)
        equipamento.save()
        return JsonResponse({
            'id': equipamento.id,
            'nome': equipamento.nome,
            'descricao': equipamento.descricao,
        })
    except Equipments.DoesNotExist:
        return HttpResponseNotFound(json.dumps({"error": "Equipament not found"}))
    except (KeyError, TypeError, ValueError) as e:
        return HttpResponseBadRequest(json.dumps({"error": str(e)}))

#PUT - VEÍCULOS

@csrf_exempt
@require_http_methods(["PUT"])
def vehicles_update(request, pk):
    try:
        veiculos = Vehicles.objects.get(pk=pk)
        data = json.loads(request.body)

        veiculos.nome = data.get('nome', veiculos.nome)
        veiculos.descricao = data.get('descricao', veiculos.descricao)
        veiculos.save()
        return JsonResponse({
            'id': veiculos.id,
            'nome': veiculos.nome,
            'descricao': veiculos.descricao,
        })
    except Vehicles.DoesNotExist:
        return HttpResponseNotFound(json.dumps({"error": "Equipament not found"}))
    except (KeyError, TypeError, ValueError) as e:
        return HttpResponseBadRequest(json.dumps({"error": str(e)}))
    
    
#====================================================================


                                  #DELETE
#DELETE - DISPOSITIVOS: 
@csrf_exempt
@require_http_methods(["DELETE"])
def devices_delete(request, pk):
    try:
        dispositivos = Devices.objects.get(pk=pk)
        dispositivos.delete()
        return JsonResponse({"message": "Device deleted successfully"})
    except Devices.DoesNotExist:
        return HttpResponseNotFound(json.dumps({"error": "Device not found"}))

#DELETE - EQUIPAMENTOS: 
@csrf_exempt
@require_http_methods(["DELETE"])
def equipments_delete(request, pk):
    try:
        equipamentos = Equipments.objects.get(pk=pk)
        equipamentos.delete()
        return JsonResponse({"message": "Equipment deleted successfully"})
    except Equipments.DoesNotExist:
        return HttpResponseNotFound(json.dumps({"error": "Equipment not found"}))


#DELETE - VEÍCULOS: 
@csrf_exempt
@require_http_methods(["DELETE"])
def vehicles_delete(request, pk):
    try:
        veiculos = Vehicles.objects.get(pk=pk)
        veiculos.delete()
        return JsonResponse({"message": "Vehicle deleted successfully"})
    except Vehicles.DoesNotExist:
        return HttpResponseNotFound(json.dumps({"error": "Vehicle not found"}))
