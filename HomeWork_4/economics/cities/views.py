from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseNotAllowed
from django.http.response import JsonResponse


tmp_data_cities_list = {
    1: 'Майклштадт',
    2: 'Александровск',
    3: 'Екатеринград',
    4: 'Ивановск',
    5: 'Павлово',
    6: 'Мухосранск',
    7: 'Дарьевск',
    8: 'Данилино',
    9: 'Тимофеевск',
    10: 'Евгенштадт',
}

tmp_data_cities_info = {
    1: {'Площадь': '12 тыс кв.км','Население': '10.2 млн','Богатство': 'Умеренно','Удовлетворение': 'Комфортный город'},
    2: {'Площадь': '2 тыс кв.км','Население': '1.2 млн','Богатство': 'Мало','Удовлетворение': 'Немного грязно, но терпимо'},
    3: {'Площадь': '3 тыс кв.км','Население': '2.1 млн','Богатство': 'Высоко','Удовлетворение': 'Если ночью спать, то ничего'},
    4: {'Площадь': '1 тыс кв.км','Население': '0.8 млн','Богатство': 'Мало','Удовлетворение': 'Оставь надежду всякий сюда входящий'},
    5: {'Площадь': '0.5 тыс кв.км','Население': '0.4 млн','Богатство': 'Умеренно','Удовлетворение': 'Все довольны? Все довольны'},
    6: {'Площадь': '2 тыс кв.км','Население': '3.2 млн','Богатство': 'Умеренно','Удовлетворение': 'Что такое личная жизнь?'},
    7: {'Площадь': '1 тыс кв.км','Население': '1.9 млн','Богатство': 'Мало','Удовлетворение': 'Отличный город, всем нравится'},
    8: {'Площадь': '4 тыс кв.км','Население': '0.1 млн','Богатство': 'Высоко','Удовлетворение': 'Жить хорошо, есть нечего'},
    9: {'Площадь': '3 тыс кв.км','Население': '0.2 млн','Богатство': 'Мало','Удовлетворение': 'Когда будет отопление?'},
    10: {'Площадь': '0.6 тыс кв.км','Население': '0.5 млн','Богатство': 'Умеренно','Удовлетворение': 'Лучше не бывает'},
}


def city_list(request):
    if request.method == 'GET':
        return JsonResponse(tmp_data_cities_list)
    elif request.method == 'POST':
        try:
            city_id = int(request.POST.get('city_id'))
            name = request.POST.get('name')
        except TypeError:
            return HttpResponseBadRequest('city_id must be integer')
        if name is None:
            return HttpResponseBadRequest('Not all parameters!\nParameters: country_id, name')
        tmp_data_cities_list[city_id] = name
        return JsonResponse(tmp_data_cities_list)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


def city_info(request, city_id):
    if not isinstance(city_id, int):
        return HttpResponseBadRequest("city_id must be integer")
    city_id = int(city_id)
    if request.method == 'GET':
        return JsonResponse(tmp_data_cities_info[city_id])
    elif request.method == 'POST':
        wealth = request.POST.get('wealth')
        area = request.POST.get('area')
        population = request.POST.get('population')
        pleasure = request.POST.get('pleasure')
        if wealth is None or area is None or population is None or pleasure is None:
            return HttpResponseBadRequest("Not all parameters!\nParameters: wealth, area, population, pleasure")
        tmp_data_cities_info[city_id] = {'Площадь': area, 'Население': population, 'Богатство': wealth, 'Удовлетворение': pleasure}
        return JsonResponse(tmp_data_cities_info[city_id])
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])
