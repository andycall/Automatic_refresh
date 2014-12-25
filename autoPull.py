#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'andycall'

import subprocess, os, logging, time

def checkIfGit(str):
    if '.git' in str and os.path.isdir(str):
        return True
    else:
        return False

paths = []

def find(path):
    if not os.path.exists(path):
        return

    dir_list = os.listdir(path)

    for dir in dir_list:
        new_path = os.path.join(path, dir)
        if(checkIfGit(new_path)):
            paths.append(new_path.replace('/.git', ''))
        else:
            if os.path.isdir(new_path):
                find(new_path)

def RunPull(paths):
    now_path = os.path.abspath('.')
    log_path = os.path.join(now_path, 'log')
    now_time = time.strftime('%Y-%m-%d %H:%m',time.localtime(time.time()))

    if not os.path.exists(log_path):
        os.mkdir(log_path)

    with open(os.path.join(log_path, 'error.log'), 'a') as f:
        f.write('--------------- ' + now_time + ' ----------------\n')

    for i in paths:
        name = i.split('/')[-1]
        try:
            os.chdir(i)
            now_branch = subprocess.check_output(['git', 'branch']).split(' ')[-1].strip('\n') or 'master'
            now_origin = subprocess.check_output(['git', 'remote']).strip('\n') or 'origin'
            output = subprocess.check_output(['git', 'pull', now_origin, now_branch])
            with open(os.path.join(log_path ,'{name}.log'.format(name=name)), 'a') as f:
                f.write("---------- " + now_time + ' ' + name + ' ------------\n' + output + '\n')
        except subprocess.CalledProcessError, e:
            logging.exception(e)
            with open(os.path.join(now_path,'log/error.log'), 'a') as f:
                f.write("Failed :" +  name + '\n')

if __name__ == "__main__":

    now_path = os.path.abspath(".")
    find(now_path)
    path_length = len(paths)
    RunPull(paths)