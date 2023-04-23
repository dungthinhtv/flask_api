import requests
import json
from requests.exceptions import ConnectTimeout
  
# Opening JSON file
f = open('./tmp/movie_title_all_detail.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
for i in data:
    
    if i['id'] == 358:
    
        try: 
            tmdb_res = requests.get('https://api.themoviedb.org/3/search/movie?api_key=10471161c6c1b74f6278ff73bfe95982&query='+i['name'])
            data = tmdb_res.text
            parse_json = json.loads(data)
            if (len(parse_json['results']) > 0):
                try: 
                    print(str(i['id'])+ ' - ' + i['name'])
                    id = parse_json['results'][0]['id']
                    src = i['src1']
                    idpm = i['id']
                    url_imp = 'https://somot.one/web/movie/import-new.html?id=' + str(id) + '&urlpm=' + src + '&idpm=' + str(idpm)
                    
                    try:
                        import_url = requests.get(url_imp, timeout=(10,30))
                    except ConnectTimeout:
                        print('Request has timed out')
                    
                    print (import_url.text)
                    # print(str(idpm))
                    # time.sleep(5)
                except:
                    print(str(i['id'])+ ' - ' + i['name'])
                    print("An exception occurred")
        except:
                print(str(i['id'])+ ' - ' + i['name'])
                print("An exception occurred")
# Closing file
f.close()