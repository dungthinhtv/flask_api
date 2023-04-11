import requests
import json
import time
  
# Opening JSON file
f = open('./tmp/movie_title_all_detail.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
for i in data:
    
    if (i['id'] > 2567):
    
    
        tmdb_res = requests.get('https://api.themoviedb.org/3/search/movie?api_key=10471161c6c1b74f6278ff73bfe95982&query='+i['name'])
        
        data = tmdb_res.text
        
        parse_json = json.loads(data)
        
        if (len(parse_json['results']) > 0):
            
            print(i['name'])
        
            id = parse_json['results'][0]['id']
            
            src = i['src1']
            
            idpm = i['id']
            
            url_imp = 'https://somot.one/web/movie/import-new.html?id=' + str(id) + '&urlpm=' + src + '&idpm=' + str(idpm)
            
            
            
            import_url = requests.get(url_imp)
            
            print (import_url.text)
            print(str(idpm))
            
            time.sleep(5)
    
    
    
# Closing file
f.close()