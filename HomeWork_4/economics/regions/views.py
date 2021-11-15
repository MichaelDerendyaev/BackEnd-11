from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.http.response import JsonResponse
from django.views.decorators.http import require_POST, require_GET
from .models import Region


@require_GET
def region_list(request):
    regions = Region.objects.all()
    data = [
        {
            'id':  region.id,
            'name':  region.name,
        } for region in regions
    ]
    return JsonResponse({'regions': data})


@require_GET
def region_info(request, region_id):
    try:
        region = Region.objects.get(id=region_id)
        data = {
            'name': region.name,
            'capital': f"{region.capital} P",
            'area': f"{region.area} km^2",
            'population': f"{region.population} mln",
            'fertility': region.fertility,
            'minerals': region.minerals
        }
        return JsonResponse({f"region with id={region_id}": data})
    except Region.DoesNotExist:
        return HttpResponseNotFound("<h2>Region not found</h2>")


@require_GET
def region_delete(request, region_id):
    try:
        region = Region.objects.get(id=region_id)
        region.delete()
        return render(request, 'deletion.html')
    except Region.DoesNotExist:
        return HttpResponseNotFound("<h2>Region not found</h2>")


@require_POST
def region_edit(request, region_id):
    try:
        region = Region.objects.get(id=region_id)
        region.name = request.POST.get("name")
        region.capital = request.POST.get("capital")
        region.area = request.POST.get("area")
        region.population = request.POST.get("population")
        region.fertility = request.POST.get("fertility")
        region.minerals = request.POST.get("minerals")
        region.save()
        return render(request, 'editing.html')
    except Region.DoesNotExist:
        return HttpResponseNotFound("<h2>Region not found</h2>")
    except ValueError:
        return HttpResponseNotFound("<h2>invalid input parameters</h2>")
    except TypeError:
        return HttpResponseBadRequest("<h2>invalid input parameters</h2>")


@require_POST
def region_create(request):
    try:
        region = Region()
        region.name = request.POST.get("name")
        region.capital = request.POST.get("capital")
        region.area = request.POST.get("area")
        region.population = request.POST.get("population")
        region.fertility = request.POST.get("fertility")
        region.minerals = request.POST.get("minerals")
        region.save()
        return render(request, 'creation.html')
    except ValueError:
        return HttpResponseBadRequest("<h2>invalid input parameters</h2>")
    except TypeError:
        return HttpResponseBadRequest("<h2>invalid input parameters</h2>")
