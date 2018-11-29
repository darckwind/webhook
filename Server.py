from flask import json
from flask import request
from flask import Flask
from git import Repo
import git
import os, sys

#folder directory

directory = "Gitproyects"

#crafting folder

if not os.path.exists(directory):
        os.makedirs(directory)
        print 'directorio: ', directory, 'creado'
else:
     	print 'direcctorio:',directory, 'ya existe'

#route git

gitroute = "https://user:password@rute-repository"


#git clone repository

if not os.path.exists(directory):
        Repo.clone_from(gitroute,directory)
else:
     	print 'repocitorio ya creado'

print 'git clonado'


app = Flask(__name__)

@app.route('/')
def api_root():
        return 'welcome'


@app.route('/github', methods=['POST'])
def api_gh_message():
    if request.headers['Content-Type']== 'application/json':
    jsone = json.dumps(request.json)
    g = git.cmd.Git(directory)
    g.pull('origin')
    print('repository updated')

    return jsone

if __name__ == '__main__':
  app.run()
