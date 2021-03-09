# -*- coding: UTF-8 -*-
from flask import Flask, jsonify, redirect, make_response
import requests
import json
from bs4 import BeautifulSoup
import re

app = Flask(__name__)

# author: https://github.com/Zfour
def github_json(owner, repo, branch):
    source_url = 'https://raw.githubusercontent.com/' + owner + '/' + repo + '/' + branch + '/generator/output/v1/data.json'
    req = requests.get(source_url)
    content = []
    if req.content:
        content = json.loads(req.content.decode())

    resp = make_response(jsonify({'code': 0, 'source_url': source_url, 'content': content}))
    resp.status = '200'
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
    resp.headers['Content-Type'] = 'application/json; charset=utf-8'
    return resp

@app.route('/v1/<owner>', methods=['GET'])
def start_owner(owner):
    repo = 'issues-api'
    branch = 'main'
    return github_json(owner, repo, branch)

@app.route('/v1/<owner>/<repo>', methods=['GET'])
def start_owner_repo(owner, repo):
    branch = 'main'
    return github_json(owner, repo, branch)

@app.route('/v1/<owner>/<repo>/<branch>', methods=['GET'])
def start_owner_repo_branch(owner, repo, branch):
    return github_json(owner, repo, branch)
