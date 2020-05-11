import collections
import os

import work_wechat

corpid = os.environ.get("CORPID")
corpsecret = os.environ.get("CORPSECRET")
agentid = os.environ.get("AGENTID")

ww = work_wechat.WorkWeChat(corpid=corpid, corpsecret=corpsecret)

# 0获取当天的数据统计  1获取昨天应用发送数据
data = ww.message_get_statistics(0)

if isinstance(data, collections.Iterable):
    for d in data:
        print("应用: {} 发送消息次数：{}".format(d["app_name"], d["count"]))
else:
    print("应用: {} 发送消息次数：{}".format(data["app_name"], data["count"]))
