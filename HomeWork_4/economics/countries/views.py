from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseNotAllowed
from django.http.response import JsonResponse
from django.views.decorators.http import require_POST, require_GET


tmp_data_countries_list = {
    1: 'Зона спокойствия',
    2: 'Раздражение слизистой',
    3: 'Страх ночи',
    4: 'Злость отчима',
    5: 'Радость встречи',
}

tmp_data_countries_info = {
    1: {'Площадь': '25 млн кв.км','Население': '50 млн','Богатство': 'Умеренно','Удовлетворение': 'На высшем уровне'},
    2: {'Площадь': '15 млн кв.км','Население': '1.1 млн','Богатство': 'Мало','Удовлетворение': 'Немного неприятно, но терпимо'},
    3: {'Площадь': '10 млн кв.км','Население': '3.3 млн','Богатство': 'Высоко','Удовлетворение': 'Если не спать, то пойдёт'},
    4: {'Площадь': '20 млн кв.км','Население': '2.2 млн','Богатство': 'Мало','Удовлетворение': 'Проще повеситься'},
    5: {'Площадь': '5 млн кв.км','Население': '0.5 млн','Богатство': 'Умеренно','Удовлетворение': 'Лучше не бывает'},
}


def country_list(request):
    if request.method == 'GET':
        return JsonResponse(tmp_data_countries_list)
    elif request.method == 'POST':
        try:
            country_id = int(request.POST.get('country_id'))
            name = request.POST.get('name')
        except TypeError:
            return HttpResponseBadRequest('country_id must be integer')
        if name is None:
            return HttpResponseBadRequest('Not all parameters!\nParameters: country_id, name')
        tmp_data_countries_list[country_id] = name
        return JsonResponse(tmp_data_countries_list)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


def country_info(request, country_id):
    if not isinstance(country_id, int):
        return HttpResponseBadRequest("country_id must be integer")
    country_id = int(country_id)
    if request.method == 'GET':
        return JsonResponse(tmp_data_countries_info[country_id])
    elif request.method == 'POST':
        wealth = request.POST.get('wealth')
        area = request.POST.get('area')
        population = request.POST.get('population')
        pleasure = request.POST.get('pleasure')
        if wealth is None or area is None or population is None or pleasure is None:
            return HttpResponseBadRequest("Not all parameters!\nParameters: wealth, area, population, pleasure")
        tmp_data_countries_info[country_id] = {'Площадь': area,'Население': population,'Богатство': wealth,'Удовлетворение': pleasure}
        return JsonResponse(tmp_data_countries_info[country_id])
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])
