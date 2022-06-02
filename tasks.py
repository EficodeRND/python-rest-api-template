from os import path

from invoke import run as invoke_run, task


@task
def devserver(context):
    CURRENT_DIR = path.abspath(path.dirname(__file__))
    print(CURRENT_DIR)
    invoke_run('app/server.py devserver', env={'PYTHONPATH': './', 'PYTHONUNBUFFERED': 'TRUE'})
