# A lite Paper API of Lite Minecraft Launcher
# Author: Xiao_Jin
from urllib import request
import json
import aria2c
import threading
import time

__version = '19-11-07'
print("Lite Paper-API Lib, built on " + __version)

UA = "Mozilla/5.0 (Windows 10; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
done = False


def version():
    print("Lite Paper-API Lib, built on " + __version)
    return __version


class Poll(threading.Thread):
    def __init__(self, thread_id, gid):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = gid

    def run(self):
        global done
        print('Start polling...')
        status = aria2c.tellstatus(self.name)
        while status['result']['status'] == 'active':
            status = aria2c.tellstatus(self.name)
            returned = aria2c.tellstatus(self.name)
            print(returned)
            time.sleep(1)
        aria2c.shutdown()
        done = True


def get_latest():
    print("[Paper] Checking, please wait...")
    mc_ver_json_req = request.Request(url="https://papermc.io/api/v1/paper", headers={"User-Agent": UA})
    mc_ver_byte = request.urlopen(mc_ver_json_req)
    mc_ver_json = mc_ver_byte.read().decode()
    mc_ver_py = json.loads(str(mc_ver_json))
    latest_mc_ver = mc_ver_py['versions'][0]

    paper_bid_json_req = request.Request(url="https://papermc.io/api/v1/paper/" + latest_mc_ver + "/latest",
                                         headers={"User-Agent": UA})
    paper_bid_byte = request.urlopen(paper_bid_json_req)
    paper_bid_json = paper_bid_byte.read().decode()
    paper_bid_py = json.loads(str(paper_bid_json))
    paper_latest_bid = paper_bid_py['build']
    print("[Paper] Done! The latest Build of Paper-" + latest_mc_ver + " is >>> Build " + paper_latest_bid)
    # 返回数据
    latest_paper_ver = paper_latest_bid
    return latest_paper_ver


def get(mc_ver):
    print("[Paper] Checking, please wait...")
    paper_bid_json_req = request.Request(url="https://papermc.io/api/v1/paper/" + mc_ver + "/latest",
                                         headers={"User-Agent": UA})
    paper_bid_byte = request.urlopen(paper_bid_json_req)
    paper_bid_json = paper_bid_byte.read().decode()
    paper_bid_py = json.loads(str(paper_bid_json))
    paper_latest_bid = paper_bid_py['build']
    print("[Paper] Done! The latest Build of Paper-" + mc_ver + " is >>> Build " + paper_latest_bid)
    # 返回数据
    paper_ver = paper_latest_bid
    return paper_ver


def get_download_url(mc_ver):
    url = 'https://papermc.io/api/v1/paper/' + mc_ver + '/latest/download'
    return url


def download(mc_ver, path_to_save):
    aria2c.start()
    time.sleep(1)
    gid = aria2c.adduri(get_download_url(mc_ver), path_to_save)
    # 轮询
    poll_thread = Poll(1, gid)
    poll_thread.start()
