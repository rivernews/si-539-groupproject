from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json

import os
import csv

import datetime
import sys

def get_param_to_dict(get_query_dict):
    param_dict = {}
    for key, value in get_query_dict.items():
        param_dict[key] = value
    return param_dict

def getCSVdata(param_dict={}):
    # validate paramter first: bad format / missing required params
    # validate parameter: start value should always smaller than end
    # validate "amount": avoid negative or too big value.
    
    '''importing 
    paramters'''
    # amount - loose policy
    nol_to_read = 10
    try:
        nol_to_read = int(param_dict['amount']) if param_dict['amount'] != 'ALL' else sys.maxsize
    except KeyError as e:
        pass
    # time - strict policy
    end_time = None
    try:
        start_time = datetime.datetime.strptime(param_dict['time-start'], '%Y-%m')
        end_time = datetime.datetime.strptime(param_dict['time-end'], '%Y-%m')
    except ValueError as e:
        pass
    except KeyError as e:
        pass
    # area - strict policy
    area_max = None
    try:
        area_min = int(param_dict['area-min'])
        area_max = int(param_dict['area-max'])
    except KeyError as e:
        pass
    # state - loose policy
    state_req = 'ALL'
    try:
        state_req = param_dict['state']
    except KeyError as e:
        pass
    
    
    # read file csv
    PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))
    csv_filepath = os.path.join(PROJECT_PATH, 'fire-has-state.csv')
    row_data_list = []
    i = 0
    max_area = -1
    with open(csv_filepath, newline='') as csvfile:
        csv_dictreader = csv.DictReader(csvfile)
        for row in csv_dictreader:
            '''preprocessing'''
            # preprocess 'time'
            time = datetime.datetime(int(row['year']), int(row['month']), int(row['day']))
            # preprocess 'area'
            area = int(row['acres_burned'])
            # preprocess 'state'
            state = row['states']
            
            '''compare / 
            filter rows here'''
            # filter 'time'
            if (end_time is None) or not (start_time <= time <= end_time): continue
            
            # filter 'area'
            if (area_max is None) or not (area_min <= area <= area_max): continue

            # filter 'amount'
            if (i>=nol_to_read): break

            # filter 'state'
            if (state_req != 'ALL' and (state_req.casefold() != state.casefold())): continue

            # start fetching row data
            row_data_list.append({
                'time': time,

                'lat': row['lat'],
                'long': row['long'],
                'area': area,

                'name': ' or '.join( [ row['na_l3name'], row['na_l2name'], row['na_l1name'] ] ),

                'max_temp': row['max_air_temp'],
                'wind_speed': row['mean_wind_speed'],
                'mean_potential_et': row['mean_potential_et'],
                'total_precip' : row['total_precip'],

                'state': state,
            })
            i += 1
    # convert to json
    # ready to send json
    return row_data_list

def api_get(request):
    if request.method == 'GET':
        print('try to pull out GET parameters')
        # json_passed = json.loads(request.GET.decode('utf-8'))
        param_dict = get_param_to_dict(request.GET)
        
        json_dict = {
            'row_list': getCSVdata(param_dict),
        }
        return JsonResponse(json_dict)

def prevent(request):
    if request.method == 'GET':
        vars = {
        }
        return render(request,'prevent.html',vars)

def index(request):
    if request.method == 'GET':
        vars = {
            'title': 'Home Page la',
            'data': getCSVdata(),
        }
        return render(request,'main_app/index.html',vars)