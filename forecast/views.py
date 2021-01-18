import requests, json
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # base URL
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = request.GET['CITY']
    print(CITY)
    API_KEY = "5f6d4ce96d3d088b0a5eca5a9584890c"
    # updating the URL
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    try: 
        # HTTP request
        response = requests.get(URL)
    except Exception as e:
            return(str(e))
    # checking the status code of the request
    if response.status_code == 200:
        # getting data in the json format
        data = response.json()
    
        # getting the main dict block
        main = data['main']
        print(main)
        temp = main.get('temp')
        feelsLikeTemp = main.get('feels_like')
        tempMax = main.get('temp_max')
        tempMin = main.get('temp_min')
        #Calculate averaage temp
        tempAvg = (temp + feelsLikeTemp + tempMax + tempMin)/4
        tempObject = {
            'maximum': tempMax,
            'minimum': tempMin,
            'average': tempAvg,
            'median': main.get('temp'),
        }
        print(tempObject)
        return HttpResponse(str(tempObject))
    else:
    # showing the error message
        print("Error in the HTTP request")
        return HttpResponse("Error in the HTTP request")