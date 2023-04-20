#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request, jsonify
from slugify import slugify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/all/', methods=['GET'])
def query_all_records():
    data = json.load(open('./tmp/movie_title_all_detail.json'))
    
    return jsonify(data)

@app.route('/idtv/', methods=['GET'])
def query_tv_records():
    if request.args.get('name'):
        name = request.args.get('name')
        records = json.load(open('./tmp/3_series_poster_details.json'))
        episode = []
        for record in records:
            if name.lower() in record['name'].lower():
                episode.append(record)
        return jsonify(episode)  
    return "Episode not found"   

@app.route('/title/', methods=['GET'])
def query_title_records():
    if request.args.get('id'):
        id = int(request.args.get('id'))
    else:
        id=0
    records = json.load(open('./tmp/movie_title_all_detail.json'))
    titles = []
    for record in records:
        # titles.append(record['name']+ ' (' + str(record['year']) + ')')
        if len(titles)>12:
            break
        if (record['id'] >= id):
            titles.append(record)
    return jsonify(titles)        
        
@app.route('/slug/', methods=['GET'])
def query_name_records():
    name = request.args.get('slug')
    records = json.load(open('./tmp/movie_title_all_detail.json'))
    for record in records:
        if (record['slug'] == name):
            return (record)

@app.route('/idmv/', methods=['GET'])
def query_record():
    id = int(request.args.get('id'))
    
    with open('./tmp/movie_title_all_detail.json', 'r') as f:
        data = f.read()
        records = json.loads(data)
        
        for record in records:
            if  (record['id'] == id):
                return (record)
        
        # return jsonify(results)
        return jsonify({'error': 'data not found'})

@app.route('/mv/', methods=['GET'])
def query_records():
    slug = request.args.get('slug')
    year = request.args.get('year')
    print (slug)
    with open('./tmp/movie_title_all_detail.json', 'r') as f:
        data = f.read()
        records = json.loads(data)
        
        for record in records:
            if  (record['slug'] in slug) and (str(record['year']) == year):
                return (record)
        
        # return jsonify(results)
        return jsonify({'error': 'data not found'})

@app.route('/mv/', methods=['PUT'])
def create_record():
    record = json.loads(request.data)
    with open('/tmp/movie_title_all_detail.json', 'r') as f:
        data = f.read()
    if not data:
        records = [record]
    else:
        records = json.loads(data)
        records.append(record)
    with open('/tmp/movie_title_all_detail.json', 'w') as f:
        f.write(json.dumps(records, indent=2))
    return jsonify(record)

@app.route('/mv/', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    new_records = []
    with open('/tmp/movie_title_all_detail.json', 'r') as f:
        data = f.read()
        records = json.loads(data)
    for r in records:
        if r['name'] == record['name']:
            r['email'] = record['email']
        new_records.append(r)
    with open('/tmp/movie_title_all_detail.json', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)
    
@app.route('/mv/', methods=['DELETE'])
def delte_record():
    record = json.loads(request.data)
    new_records = []
    with open('/tmp/movie_title_all_detail.json', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for r in records:
            if r['name'] == record['name']:
                continue
            new_records.append(r)
    with open('/tmp/movie_title_all_detail.json', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)

if __name__ == "__main__":
    app.run()