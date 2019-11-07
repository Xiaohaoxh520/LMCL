# Lite Aria2c-JsonRPC Lib for Lite Minecraft Launcher
# Author: Xiao_Jin
# RPC-Port: 6801

from urllib import request
import json
import os

__version = '19-11-07'
print("Lite Aria2c-JsonRPC Lib, built on " + __version)


def version():
    print("Lite Aria2c-JsonRPC Lib, built on " + __version)
    return __version


def start():
    if not os.path.isfile('aria2c.conf'):
        aria2c_conf = open('aria2c.conf', 'w+')
        aria2c_conf.write('''continue=true
        max-connection-per-server=16
        enable-rpc=true
        rpc-listen-port=6801''')
        aria2c_conf.close()
    print('[aria2c] RPC-Port: 6801')
    os.popen("aria2c --conf-path=aria2c.conf")


def adduri(uris, save_dir):
    json_req = json.dumps({'jsonrpc': '2.0',
                          'id': 'LMCL',
                           'dir': save_dir,
                          'method': 'aria2.addUri',
                          'params': [[uris], {'dir': save_dir}]}).encode()
    c = request.urlopen('http://localhost:6801/jsonrpc', json_req)
    returned = c.read().decode()
    # print(returned)
    json_ret = json.loads(returned)
    gid = json_ret['result']
    return gid


def tellstatus(gid):
    json_req = json.dumps({'jsonrpc': '2.0', 'id': 'LMCL',
                          'method': 'aria2.tellStatus',
                          'params': [gid]}).encode()
    c = request.urlopen('http://localhost:6801/jsonrpc', json_req)
    returned = c.read().decode()
    # print(returned)
    json_ret = json.loads(returned)
    return json_ret


def shutdown():
    json_req = json.dumps({'jsonrpc': '2.0', 'id': 'LMCL',
                          'method': 'aria2.shutdown'}).encode()
    c = request.urlopen('http://localhost:6801/jsonrpc', json_req)
    returned = c.read().decode()
    # print(returned)
    json_ret = json.loads(returned)
    if json_ret['result'] == 'OK':
        ok = True
        print('[aria2c] has been shutdown successfully!')
    else:
        ok = False
        print('[aria2c] hasn\'t been shutdown successfully! Please kill the process!')
    return ok
