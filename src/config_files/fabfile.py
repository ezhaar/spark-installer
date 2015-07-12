#!/usr/bin/env python
# -*- coding: utf-8 -*- #


from __future__ import with_statement
from fabric.api import (
    run, local, parallel, put, env, roles,
    cd, lcd, task, abort
)
from fabric.tasks import execute
from fabric.contrib.files import exists


# Set the user to use for ssh
env.user = "ubuntu"
env.add_unknown_hosts = True


HADOOP_CONF_DIR = '/usr/local/hadoop/etc/hadoop/'
HADOOP_DATA_DIR = '/home/ubuntu/data/hadoop/hdfs/'
SPARK_CONF_DIR = '/usr/local/spark/conf/'

# build the list of slaves from slaves file
with open(HADOOP_CONF_DIR + "slaves", 'r + ') as f:
        slaves = f.readlines()

f.close()
env.roledefs = {'slave': slaves}


@task
@roles('slave')
def test_conn():
    try:
        run('hostname -f')
    except:
        abort("All slaves not up yet.. Try again in a moment")

@task
@roles('slave')
@parallel
def deploy_conf_files():
    put(HADOOP_CONF_DIR + "slaves", HADOOP_CONF_DIR + "slaves")
    put(HADOOP_CONF_DIR + "core-site.xml", HADOOP_CONF_DIR + "core-site.xml")
    put(HADOOP_CONF_DIR + "hdfs-site.xml", HADOOP_CONF_DIR + "hdfs-site.xml")
    put(HADOOP_CONF_DIR + "mapred-site.xml", HADOOP_CONF_DIR +
        "mapred-site.xml")
    put(HADOOP_CONF_DIR + "yarn-site.xml.slave", HADOOP_CONF_DIR +
        "yarn-site.xml")
    put(SPARK_CONF_DIR + "slaves", SPARK_CONF_DIR + "slaves")
    put(SPARK_CONF_DIR + "spark-env.sh", SPARK_CONF_DIR + "spark-env.sh")
    put(SPARK_CONF_DIR + "spark-defaults.conf", SPARK_CONF_DIR + "spark-defaults.conf")


@task
def set_conf_files():
    with lcd(HADOOP_CONF_DIR):
        local('sed -i "s/XXXX/$(hostname)/g" core-site.xml')
        local('sed -i "s/XXXX/$(hostname)/g" yarn-site.xml')
        local('sed -i "s/XXXX/$(hostname)/g" yarn-site.xml.slave')
        local('cp slaves /usr/local/spark/conf/')


@task
@roles('slave')
def create_hdfs_dirs():
    run('mkdir -p ' + HADOOP_DATA_DIR)
    local('mkdir -p ' + HADOOP_DATA_DIR)


@roles('slave')
def reset_hdfs_dirs():
    with lcd('/home/ubuntu/data/hadoop/hdfs'):
        local('rm -rf dn nn snn')
        local('mkdir dn && mkdir nn && mkdir snn')
    with cd(HADOOP_DATA_DIR):
        run('rm -rf dn nn snn')
        run('mkdir dn && mkdir nn && mkdir snn')


def format_hdfs():
    execute(reset_hdfs_dirs)
    local('hdfs namenode -format')
    local('start-dfs.sh')
    local('hdfs dfs -mkdir /user')
    local('hdfs dfs -mkdir /user/ubuntu')
    local('stop-dfs.sh')


@task 
def init_local():
    execute(set_conf_files)
    execute(format_hdfs)
    execute(start_hadoop)
    execute(start_spark)


@task
def init_cluster():
    execute(test_conn)
    execute(set_conf_files)
    execute(deploy_conf_files)
    execute(format_hdfs)
    execute(start_hadoop)


@task
def stop_hadoop():
    local('stop-dfs.sh')
    local('stop-yarn.sh')


@task
def start_hadoop():
    local('start-dfs.sh')
    local('start-yarn.sh')

@task
def start_spark():
    local('/usr/local/spark/sbin/start-all.sh')

@task
def stop_spark():
    local('/usr/local/spark/sbin/stop-all.sh')

@task
def reset_cluster():
    execute(stop_hadoop)
    execute(reset_hdfs_dirs)
    execute(deploy_conf_files)
    execute(format_hdfs)
    execute(start_hadoop)
