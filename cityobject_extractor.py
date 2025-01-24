import simplejson as json

with open('/home/thomas/geodata/wip/cityjson/test_mel/sortie/cityjson_mel.json', 'r') as file:
    cityjson = json.load(file)

for key in cityjson['CityObjects']:
    print (key)