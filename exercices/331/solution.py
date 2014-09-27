import json
file = open('velib.json')
lis = json.load(file)
dic2 = {}
liste2 = []
for dic in lis:
    dic2 = {}
    for key in dic:
        if key == 'name':
            d = dic['name']
            dic2['name'] = d[8:]
            dic2['zip_code'] = d[:5]
        elif key == 'number':
            dic2['number'] = dic['number']
        elif key == "adress":
            a = dic[key].split(' - ', 2)
            dic2['adress'] = a[1]
        elif key == "latitude":
            dic2['latitude'] = dic['latitude']
        elif key == "longitude":
            dic2['longitude'] = dic['longitude']
    liste2.append(dic2)
json.dump(liste2, open("solution.json", 'w'))
