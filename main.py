import json
import os.path
import re
import time

import requests
import pandas as pd

import config
import utils


class Spider:
    def __init__(self, query, max_page):
        self.url = config.URL
        self.query = query
        self.max_page = max_page
        self.params = config.PARAMS
        self.cursor_re = re.compile('"Top"}}}}}},.*{"cursor":{"value":"(.*?)","cursorType":"Bottom"',)

    def get_response(self, cursor=None, type=None):
        if type is None or type.lower() == "top":
            self.params.update({"query_source": "trend_click"})
        if cursor is not None:
            self.params.update({"cursor": cursor})

        self.params.update({"q": self.query})
        response = requests.get(url=self.url,
                                     headers=config.HEADERS,
                                     params=self.params,
                                     proxies=config.PROXIES)
        response_json = response.json()
        response_text = response.text
        return response_json, response_text

    def save_json(self, dict, name):
        with open(name, "w") as f:
            json.dump(dict, f)

    def load_json(self, name):
        with open(name, "r") as f:
            return json.load(f)

    def parsers(self, data):
        tweets = data["globalObjects"]["tweets"]
        users = data["globalObjects"]["users"]
        for tweet in tweets:
            tweet = tweets[tweet]
            full_text = tweet["full_text"]
            created_at = tweet["created_at"]
            user_id_str = tweet["user_id_str"]
            user = users[user_id_str]
            user_name = user["name"]
            location = user["location"]
            yield {"full_text": full_text,
                   "created_at": created_at,
                   "user_name": user_name,
                  "location": location}


    def parser_cursor(self, response_json):
        # cursor = self.cursor_re.search(response_text).group(1)
        try:
            cursor = response_json["timeline"]["instructions"][-1]["addEntries"]["entries"][-1]["content"]["operation"]["cursor"]["value"]
        except KeyError as e:
            cursor = response_json["timeline"]["instructions"][-1]["replaceEntry"]["entry"]["content"]["operation"]["cursor"]["value"]
        # print(cursor)
        return cursor

def start():
    s = Spider(config.KEY, config.MAX_PAGE)
    cursor = None
    items_list = []
    if not os.path.exists(config.OUTPUT_FILE):
        df = pd.DataFrame()
        df.to_excel(config.OUTPUT_FILE, index=False, header=False)

    for i in range(0, s.max_page):
        print(f"正在获取关键词{config.KEY} 的第 {i}页")
        res_json, res_text = s.get_response(cursor)
        time.sleep(1)
        cursor = s.parser_cursor(res_json)
        items = s.parsers(res_json)
        items_list += list(items)
        print(len(items_list))
        if len(items_list) > 1000:
            utils.write_to_exist_excel2(config.OUTPUT_FILE, "Sheet1", items_list)
            items_list = []
    utils.write_to_exist_excel2(config.OUTPUT_FILE, "Sheet1", items_list)





if __name__ == '__main__':
    start()




