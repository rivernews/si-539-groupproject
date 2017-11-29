from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

import os
import csv

def getCSVdata():
    # prepare python dict
    PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))
    csv_filepath = os.path.join(PROJECT_PATH, 'fire-events_sortedbytime.csv')
    row_data_list = []
    nol_to_read = 10
    i = 0
    with open(csv_filepath, newline='') as csvfile:
        csv_dictreader = csv.DictReader(csvfile)
        for row in csv_dictreader:
            if (i<nol_to_read):
                row_data_list.append({
                    'time': row['yearmonth'],
                    'lat': row['lat'],
                    'long': row['long'],
                    'area': row['acres_burned'],
                    'name': ' or '.join( [ row['na_l3name'], row['na_l2name'], row['na_l1name'] ] ),
                    'max_temp': row['max_air_temp'],
                    'wind_speed': row['mean_wind_speed'],
                    'mean_potential_et': row['mean_potential_et'],
                    'total_precip' : row['total_precip'],
                })
            else:
                break
            i += 1
    # convert to json
    # ready to send json
    return row_data_list

def index(request):
    print("request pre-processing in django")
    if request.method == 'GET':
        vars = {
            'title': 'Home Page la',
            'data': getCSVdata(),
        }
        return render(request,'base.html',vars)
    elif request.method == 'POST':
        print('POST received in Django')
        return HttpResponse('POST ok.')
        pass
    else:
        return HttpResponse('Not allowed request.')