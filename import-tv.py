import requests
import json
import time
import re
  
# Opening JSON file
f = open('./tmp/2_series_episodes.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
for i in data:
    
    if (i['idtv'] > 240):
        try: 
            tmdb_res = requests.get('https://api.themoviedb.org/3/search/tv?api_key=10471161c6c1b74f6278ff73bfe95982&query='+re.sub('\((.*?)\)','',str(i['name'])).strip())
            data = tmdb_res.text
            parse_json = json.loads(data)
            if (len(parse_json['results']) > 0):
                try: 
                    print(str(i['idtv'])+ ' - ' + i['name'])
                    id = parse_json['results'][0]['id']
                    # src = i['src1']
                    # idpm = i['idtv']
                    url_imp = 'https://somot.one/web/tv/import-new.html?id=' + str(id)
                    import_url = requests.get(url_imp)
                    
                    print (import_url.text)
                    # print(str(idpm))
                    # time.sleep(5)
                except:
                    print(str(i['idtv'])+ ' - ' + i['name'])
                    print("An exception occurred")
        except:
                print(str(i['idtv'])+ ' - ' + i['name'])
                print("An exception occurred")
# Closing file
f.close()