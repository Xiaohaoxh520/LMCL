import json
import os


def get_current_ver_by_json(server_path):
    if os.path.isfile(server_path + "\\version_history.json"):
        bid_and_ver = {'bid': 0, 'ver': '1.8.8', 'string': '1.8.8 #443 (EXAMPLE)'}

        current_bid_json = open(server_path + "\\version_history.json", "r+")
        current_bid = current_bid_json.read()
        current_bid_json.close()
        current_bid_py = json.loads(current_bid)
        current_build = str(current_bid_py["currentVersion"]).replace("git-Paper-", "").find(" (")
        current_build_id = str(current_bid_py["currentVersion"]).replace("git-Paper-", "")[0:current_build]
        current_mc_ver = str(current_bid_py["currentVersion"]).replace("git-Paper-", "").find("(MC: ")
        current_without_unless = str(current_bid_py["currentVersion"]).replace("git-Paper-", "")

        bid_and_ver['bid'] = current_build_id
        bid_and_ver['ver'] = current_without_unless[current_mc_ver + 5:-1]
        bid_and_ver['string'] = current_without_unless[current_mc_ver + 5:-1] + " #" + str(current_build_id)

        return bid_and_ver
    else:
        raise Exception('version_history.json not found!')
