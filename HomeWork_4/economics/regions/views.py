from django.shortcuts import render
from django.http.response import JsonResponse
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest

tmp_data_regions_list = {
    1: 'Мёртвая пустошь',
    2: 'Зловещий лес',
    3: 'Ледяные вершины',
    4: 'Великая степь',
    5: 'Райский материк',
    6: 'Трясущиеся острова',
}

tmp_data_regions_info = {
    1: {'Капитал': '12.7 млн камней', 'Площадь': '10.3 млн кв.км', 'Плодородие': 'Такого не имеется', 'Полезные ископаемые': 'Разбросаны по всей территории в небольших количествах', 'Население': '10.7 млн'},
    2: {'Капитал': '18.4 млн камней', 'Площадь': '2.1 млн кв.км', 'Плодородие': 'Средненько', 'Полезные ископаемые': 'Небольшое скопление на юге', 'Население': '18.3 млн'},
    3: {'Капитал': '33.1 млн камней', 'Площадь': '3.8 млн кв.км', 'Плодородие': 'Оставляет желать лучшего', 'Полезные ископаемые': 'Очень много', 'Население': '3.7 млн'},
    4: {'Капитал': '2.3 млн камней', 'Площадь': '28.9 млн кв.км', 'Плодородие': 'Выше крыши', 'Полезные ископаемые': 'Не найдены', 'Население': '2.9 млн'},
    5: {'Капитал': '0.2 млн камней', 'Площадь': '12.2 млн кв.км', 'Плодородие': 'Выше среднего', 'Полезные ископаемые': 'Много', 'Население': '0.8 млн'},
    6: {'Капитал': '1.9 млн камней', 'Площадь': '0.8 млн кв.км', 'Плодородие': 'Средненько', 'Полезные ископаемые': 'Много', 'Население': '1.5 млн'},
}


def region_list(request):
    if request.method == 'GET':
        return JsonResponse(tmp_data_regions_list)
    elif request.method == 'POST':
        try:
            region_id = int(request.POST.get('region_id'))
            name = request.POST.get('name')
        except TypeError:
            return HttpResponseBadRequest('region_id must be integer')
        if name is None:
            return HttpResponseBadRequest('Not all parameters!\nParameters: region_id, name')
        tmp_data_regions_list[region_id] = name
        return JsonResponse(tmp_data_regions_list)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


def region_info(request, region_id):
    if not isinstance(region_id, int):
        return HttpResponseBadRequest("region_id must be integer")
    region_id = int(region_id)
    if request.method == 'GET':
        return JsonResponse(tmp_data_regions_info[region_id])
    elif request.method == 'POST':
        capital = request.POST.get('capital')
        area = request.POST.get('area')
        population = request.POST.get('population')
        fertility = request.POST.get('fertility')
        minerals = request.POST.get('minerals')
        if capital is None or area is None or population is None or fertility is None or minerals is None:
            return HttpResponseBadRequest("Not all parameters!\nParameters: capital, area, population, fertility, minerals")
        tmp_data_regions_info[region_id] = {'Капитал': capital, 'Площадь': area, 'Плодородие': fertility, 'Полезные ископаемые': minerals, 'Население': population}
        return JsonResponse(tmp_data_regions_info[region_id])
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


