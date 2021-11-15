from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.http.response import JsonResponse
from django.views.decorators.http import require_POST, require_GET
from .models import City
from countries.models import Country


@require_GET
def city_list(request):
    cities = City.objects.all()
    data = [
        {
            'id': city.id,
            'name': city.name,
            'country': city.country.name,
        } for city in cities
    ]
    return JsonResponse({'cities': data})


@require_GET
def city_info(request, city_id):
    try:
        city = City.objects.get(id=city_id)
        data = {
            'name': city.name,
            'country': city.country.name,
            'wealth': city.wealth,
            'area': f"{city.area} km^2",
            'population': f"{city.population} mln",
            'pleasure': city.pleasure,
        }
        return JsonResponse({f"city with id={city_id}": data})
    except City.DoesNotExist:
        return HttpResponseNotFound("<h2>City not found</h2>")


@require_POST
def city_delete(request, city_id):
    try:
        city = City.objects.get(id=city_id)
        city.delete()
        return render(request, 'deletion.html')
    except City.DoesNotExist:
        return HttpResponseNotFound("<h2>City not found</h2>")


@require_POST
def city_edit(request, city_id):
    try:
        city = City.objects.get(id=city_id)
        city.name = request.POST.get("name")
        city.wealth = request.POST.get("wealth")
        city.area = request.POST.get("area")
        city.population = request.POST.get("population")
        city.pleasure = request.POST.get("pleasure")
        country_id = int(request.POST.get("country_id"))
        country = Country.objects.get(id=country_id)
        city.country = country
        city.save()
        return render(request, 'editing.html')
    except City.DoesNotExist:
        return HttpResponseNotFound("<h2>City not found</h2>")
    except Country.DoesNotExist:
        return HttpResponseNotFound("<h2>Country not found</h2>")
    except ValueError:
        return HttpResponseBadRequest("<h2>invalid input parameters</h2>")
    except TypeError:
        return HttpResponseBadRequest("<h2>invalid input parameters</h2>")


@require_POST
def city_create(request):
    try:
        city = City()
        city.name = request.POST.get("name")
        city.wealth = request.POST.get("wealth")
        city.area = request.POST.get("area")
        city.population = request.POST.get("population")
        city.pleasure = request.POST.get("pleasure")
        country_id = int(request.POST.get("country_id"))
        country = Country.objects.get(id=country_id)
        city.country = country
        city.save()
        return render(request, 'creation.html')
    except Country.DoesNotExist:
        return HttpResponseNotFound("<h2>Country not found</h2>")
    except ValueError:
        return HttpResponseBadRequest("<h2>invalid input parameters</h2>")
    except TypeError:
        return HttpResponseBadRequest("<h2>invalid input parameters</h2>")
