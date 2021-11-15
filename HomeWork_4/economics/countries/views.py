from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.http.response import JsonResponse
from django.views.decorators.http import require_POST, require_GET
from .models import Country
from regions.models import Region


@require_GET
def country_list(request):
    countries = Country.objects.all()
    data = [
        {
            'id':  country.id,
            'name':  country.name,
            'country':  country.region.name,
        } for country in countries
    ]
    return JsonResponse({'countries': data})


@require_GET
def country_info(request, country_id):
    try:
        country = Country.objects.get(id=country_id)
        data = {
            'name': country.name,
            'region': country.region.name,
            'wealth': country.wealth,
            'area': f"{country.area} km^2",
            'population': f"{country.population} mln",
            'pleasure': country.pleasure,
        }
        return JsonResponse({f"country with id={country_id}": data})
    except Country.DoesNotExist:
        return HttpResponseNotFound("<h2>Country not found</h2>")


@require_POST
def country_delete(request, country_id):
    try:
        country = Country.objects.get(id=country_id)
        country.delete()
        return render(request, 'deletion.html')
    except Country.DoesNotExist:
        return HttpResponseNotFound("<h2>Country not found</h2>")


@require_POST
def country_edit(request, country_id):
    try:
        country = Country.objects.get(id=country_id)
        country.name = request.POST.get("name")
        country.wealth = request.POST.get("wealth")
        country.area = request.POST.get("area")
        country.population = request.POST.get("population")
        country.pleasure = request.POST.get("pleasure")
        region_id = int(request.POST.get("region_id"))
        region = Region.objects.get(id=region_id)
        country.region = region
        country.save()
        return render(request, 'editing.html')
    except Country.DoesNotExist:
        return HttpResponseNotFound("<h2>Country not found</h2>")
    except Region.DoesNotExist:
        return HttpResponseNotFound("<h2>Region not found</h2>")
    except ValueError:
        return HttpResponseNotFound("<h2>invalid input parameters</h2>")
    except TypeError:
        return HttpResponseBadRequest("<h2>invalid input parameters</h2>")


@require_POST
def country_create(request):
    try:
        country = Country()
        country.name = request.POST.get("name")
        country.wealth = request.POST.get("wealth")
        country.area = request.POST.get("area")
        country.population = request.POST.get("population")
        country.pleasure = request.POST.get("pleasure")
        region_id = int(request.POST.get("region_id"))
        region = Region.objects.get(id=region_id)
        country.region = region
        country.save()
        return render(request, 'creation.html')
    except Region.DoesNotExist:
        return HttpResponseNotFound("<h2>Region not found</h2>")
    except ValueError:
        return HttpResponseBadRequest("<h2>invalid input parameters</h2>")
    except TypeError:
        return HttpResponseBadRequest("<h2>invalid input parameters</h2>")
