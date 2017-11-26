from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

import os
import csv

def index(request):
    PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))
    csv_filepath = os.path.join(PROJECT_PATH, 'fire-events_sortedbytime.csv')

    if request.method == 'GET':
        vars = {'title': 'Home Page la'}
        return render(request,'base.html',vars)
    elif request.method == 'POST':
        # prepare python dict
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
                    })
                else:
                    break
                i += 1
        # convert to json
        # ready to send json
        return JsonResponse({'data': row_data_list})
        pass
    else:
        return HttpResponse('Not allowed request.')