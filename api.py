# -*- coding: UTF-8 -*-
from flask import Flask, jsonify, redirect
import requests
import json
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def homepage():
    return redirect('https://github.com/xaoxuu/issues-api')

# author: https://github.com/Zfour
def github_json(owner, repo, branch):
    source_url = 'https://github.com/' + owner + '/' + repo + '/blob/' + branch + '/output.json'
    r = requests.get(source_url)
    r.encoding = 'utf-8'
    gitpage = r.text
    soup = BeautifulSoup(gitpage, 'html.parser')
    main_content = soup.find('td',id = 'LC1').text
    return jsonify({'code': 0, 'source_url': source_url, 'body': json.loads(main_content)})


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
