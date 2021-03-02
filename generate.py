# -*- coding: utf-8 -*-
# author: https://github.com/Zfour
import requests
from bs4 import BeautifulSoup
import re
import yaml
from request_data import request
import json

data_pool = []

def load_config():
    f = open('_config.yml', 'r',encoding='utf-8')
    ystr = f.read()
    ymllist = yaml.load(ystr, Loader=yaml.FullLoader)
    return ymllist

def github_issuse(data_pool):
    print('\n')
    print('------- github issues start ----------')
    baselink = 'https://github.com/'
    config = load_config()
    try:
        for number in range(1, 100):
            print(number)
            if config['issues']['label']:
                label_plus = '+label%3A' + config['issues']['label']
            else:
                label_plus = ''
            github = request.get_data('https://github.com/' +
                             config['issues']['repo'] +
                             '/issues?q=is%3A' + config['issues']['state'] + str(label_plus) + '&page=' + str(number))
            soup = BeautifulSoup(github, 'html.parser')
            main_content = soup.find_all('div',{'aria-label': 'Issues'})
            linklist = main_content[0].find_all('a', {'class': 'Link--primary'})
            if len(linklist) == 0:
                print('> end')
                break
            for item in linklist:
                issueslink = baselink + item['href']
                issues_page = request.get_data(issueslink)
                issues_soup = BeautifulSoup(issues_page, 'html.parser')
                try:
                    issues_linklist = issues_soup.find_all('pre')
                    source = issues_linklist[0].text
                    if "{" in source:
                        source = json.loads(source)
                        print(source)
                        data_pool.append(source)
                except:
                    continue
    except Exception as e:
        print('> end')

    print('------- github issues end ----------')
    print('\n')


#友链规则
github_issuse(data_pool)
filename='output.json'
with open(filename,'w',encoding='utf-8') as file_obj:
   json.dump(data_pool,file_obj,ensure_ascii=False)
