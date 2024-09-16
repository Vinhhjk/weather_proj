import glob
import json
import csv

fieldname = ['province','date','maxtemp_c','mintemp_c','windspeed_kph','avghumidity']
data_csv = []
files = glob.glob('weather_*.json')
for file in files:
    data = json.load(open(file))
    province = data['location']['name']
    detailed_data= data['forecast']['forecastday']
    for i in detailed_data:
       date = i['date']
       max_c = i['day']['maxtemp_c']
       min_c = i['day']['mintemp_c']
       maxwind_kph = i['day']['maxwind_kph']
       avghumidity = i['day']['avghumidity']
       data_to_import = {'province': province, 'date':date,'maxtemp_c':max_c,'mintemp_c':min_c,'windspeed_kph':maxwind_kph,'avghumidity':avghumidity}
       data_csv.append(data_to_import)

with open('weather_data.csv', 'a', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = fieldname)
    writer.writeheader()
    writer.writerows(data_csv)

