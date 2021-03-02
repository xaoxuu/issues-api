# -*- coding: UTF-8 -*-
from flask import Flask, jsonify, abort, url_for, redirect
import requests
import re
import json
from http.server import BaseHTTPRequestHandler
from bs4 import BeautifulSoup
import yaml

app = Flask(__name__)

@app.route('/')
def homepage():
    return redirect('https://github.com/xaoxuu/issues-api')

def load_config():
    f = open('_config.yml', 'r',encoding='utf-8')
    ystr = f.read()
    ymllist = yaml.load(ystr, Loader=yaml.FullLoader)
    return ymllist

# author: https://github.com/Zfour
def github_json(owner, repo, branch):
    source_path = 'https://github.com/' + owner + '/' + repo + '/blob/' + branch + '/output.json'
    config = load_config()
    print('config.repo: ', config['api']['repo'])
    r = requests.get(source_path)
    r.encoding = 'utf-8'
    gitpage = r.text
    soup = BeautifulSoup(gitpage, 'html.parser')
    main_content = soup.find('td',id = 'LC1').text
    result = json.loads(main_content)
    return jsonify({'code': 0, 'source_path': source_path, 'body': result})


@app.route('/<owner>', methods=['GET'])
def start_owner(owner):
    repo = 'friends'
    branch = 'main'
    return github_json(owner, repo, branch)

@app.route('/<owner>/<repo>', methods=['GET'])
def start_owner_repo(owner, repo):
    branch = 'main'
    return github_json(owner, repo, branch)

@app.route('/<owner>/<repo>/<branch>', methods=['GET'])
def start_owner_repo_branch(owner, repo, branch):
    return github_json(owner, repo, branch)
