# -*- coding: UTF-8 -*-
import json

import requests
from flask import Flask, jsonify, make_response

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


# author: https://github.com/Zfour
def github_json(owner, repo, branch, path) -> requests.Response:
    """获取友链信息

    :param owner: GitHub 用户名
    :param repo: GitHub 仓库名
    :param branch: GitHub 仓库分支名
    :return: Response
    """
    source_url = f'https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{branch}'
    try:
        req = requests.get(source_url)
        resp = make_response(jsonify(
            {'code': 0, 'source_url': source_url,
             'content': json.loads(req.content.decode()) if req.content else []}))
        resp.status = '200'
    except requests.exceptions.ConnectionError:
        resp = make_response(jsonify({'code': 500, 'content': '连接超时'}))
        resp.status = '500'
    except Exception as e:
        resp = make_response(jsonify({'code': 500, 'content': f'发生未知错误 - {e}'}))
        resp.status = '500'
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
    resp.headers['Content-Type'] = 'application/json; charset=utf-8'
    return resp


@app.route('/v2/<owner>', methods=['GET'])
@app.route('/v2/<owner>/<repo>', methods=['GET'])
@app.route('/v2/<owner>/<repo>/<branch>', methods=['GET'])
@app.route('/v2/<owner>/<repo>/<branch>/<path>', methods=['GET'])
def start_owner_repo_branch(owner, repo='issues-api', branch='main', path='generator/output/v2/data.json'):
    """获取友链信息

    :param owner: GitHub 用户名(必填)
    :param repo: GitHub 仓库名(默认为: issues-api)
    :param branch: GitHub 仓库分支名(默认为: main)
    :return: Response
    """
    return github_json(owner, repo, branch, path)
