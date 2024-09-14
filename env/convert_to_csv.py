import glob
import json
import csv

data_csv = [['date','maxtemp_c','mintemp_c','windspeed_kph','avghumidity']]
files = glob.glob('weather_*.json')
for file in files:
    data = json.load(open(file))
    detailed_data= data['forecast']['forecastday']
    for i in detailed_data:
       date = i['date']
       max_c = i['day']['maxtemp_c']
       min_c = i['day']['mintemp_c']
       maxwind_kph = i['day']['maxwind_kph']
       avghumidity = i['day']['avghumidity']
       data_to_import = [date,max_c,min_c,maxwind_kph,avghumidity]
       data_csv.append(data_to_import)

with open('weather_data.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data_csv)

