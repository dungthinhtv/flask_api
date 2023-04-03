#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request, jsonify
from slugify import slugify
import re

app = Flask(__name__)

@app.route('/all/', methods=['GET'])
def query_all_records():
    data = json.load(open('./tmp/movie_title_100_detail.json'))
    
    return jsonify(data)
    # with open('./tmp/movie_full_src_999.json', 'r') as f:
    #     data = f.read()
    #     records = json.loads(data)
    #     for record in records:
    #         if  record['slug'] == slug:
    #             return (record)
        
        # return jsonify(results)
        # return jsonify({'error': 'data not found'})


@app.route('/mv/', methods=['GET'])
def query_records():
    slug = request.args.get('slug')
    year = request.args.get('year')
    print (slug)
    with open('./tmp/movie_title_100_detail.json', 'r') as f:
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
    with open('/tmp/movie_full_src_999.json', 'r') as f:
        data = f.read()
    if not data:
        records = [record]
    else:
        records = json.loads(data)
        records.append(record)
    with open('/tmp/movie_full_src_999.json', 'w') as f:
        f.write(json.dumps(records, indent=2))
    return jsonify(record)

@app.route('/mv/', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    new_records = []
    with open('/tmp/movie_full_src_999.json', 'r') as f:
        data = f.read()
        records = json.loads(data)
    for r in records:
        if r['name'] == record['name']:
            r['email'] = record['email']
        new_records.append(r)
    with open('/tmp/movie_full_src_999.json', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)
    
@app.route('/mv/', methods=['DELETE'])
def delte_record():
    record = json.loads(request.data)
    new_records = []
    with open('/tmp/movie_full_src_999.json', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for r in records:
            if r['name'] == record['name']:
                continue
            new_records.append(r)
    with open('/tmp/movie_full_src_999.json', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)

if __name__ == "__main__":
    app.run()