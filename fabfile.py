from fabric.api import cd, env, local, put, run, settings
import datetime
import os.path
from settings import REMOTE, REMOTE_PROJECT_PATH, REMOTE_DB_PATH

env.hosts = [REMOTE,]
env.path = REMOTE_PROJECT_PATH
env.dbpath = REMOTE_DB_PATH

def deploy():
    env.release = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

    run('mkdir -p {path}/releases {path}/packages'.format(**env))

    local('git archive --format=tar master | gzip > {release}.tar.gz'.format(**env))

    put('{release}.tar.gz'.format(**env),
        '{path}/packages/'.format(**env))

    local('rm -vf {release}.tar.gz'.format(**env))

    with cd(env.path):
        run('mkdir -p releases/{release}'.format(**env))
        with cd('releases/{release}'.format(**env)):
            run('tar xvf ../../packages/{release}.tar.gz'.format(**env))
            run('ln -sf {dbpath} grouphugs.db'.format(**env))

    with cd('{path}/releases'.format(**env)):
        with settings(warn_only=True):
            run('rm previous')
            run('mv current previous')
            run('ln -sf {release} current'.format(**env))

    put('settings.py', '{path}/releases/{release}/settings.py'.format(**env))
    restart()

def restart():
    #sudo('apachectl restart')
    run('touch {path}/releases/current/dispatch.wsgi'.format(**env))

def rollback():
    with cd('{path}/releases'.format(**env)):
        run('mv current _previous')
        run('mv previous current')
        run('mv _previous previous')

def clean():
    local('find {} -name "*.pyc" -delete'.format(os.path.abspath(os.path.dirname(__file__))))
