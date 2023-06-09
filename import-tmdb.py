import requests
import json
import time
  
# Opening JSON file
f = open('./tmp/movie_title_all_detail.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)

f_new = []
  
# Iterating through the json
# list
for i in data:
    
    if (i['id'] >= 0):
        try: 
            tmdb_res = requests.get('https://api.themoviedb.org/3/search/movie?api_key=10471161c6c1b74f6278ff73bfe95982&query='+i['name'])
            data = tmdb_res.text
            parse_json = json.loads(data)
            if (len(parse_json['results']) > 0):
                try: 
                    print(str(i['id'])+ ' - ' + i['name'])
                    id = parse_json['results'][0]['id']
                    i['tmdbID'] = id
                    
                    f_new.append(i)
                    # src = i['src1']
                    # idpm = i['id']
                    # url_imp = 'https://somot.one/web/movie/import-new.html?id=' + str(id) + '&urlpm=' + src + '&idpm=' + str(idpm)
                    # import_url = requests.get(url_imp)
                    
                    # print (import_url.text)
                    # print(str(idpm))
                    time.sleep(5)
                except:
                    print("An exception occurred")
        except:
                print("An exception occurred")
                
jsonString = json.dumps(f_new,ensure_ascii=False)
jsonFile = open("data.json", "w",encoding='utf8')
jsonFile.write(jsonString)
jsonFile.close()
# Closing file
f.close()