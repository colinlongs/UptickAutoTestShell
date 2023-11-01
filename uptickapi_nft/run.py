 # -*- coding: utf-8 -*-
import  unittest
import  unittestreport
import requests
import datetime
import schedule
import time



def run_test():

    suite = unittest.defaultTestLoader.discover(r"/Users/starrymedia/PycharmProjects/upticknetwork/uptickapi_nft")
    runner = unittestreport.TestRunner(suite, tester="colin_chen", title="Uptick接口自动化测试报告" + datetime.date.today().strftime("%Y-%m-%d"), filename="upticknftapireport"+ datetime.date.today().strftime("%Y-%m-%d"), templates=2)
    runner.run()

    runner.send_email(host="smtp.exmail.qq.com",
                      port=465,
                      user="long.chen@starrymedia.com",
                      password="stHahERaHvsNEGSd",
                      to_addrs=["brian@uptickproject.com", "xianxian.zhou@starrymedia.com", "qia.fang@starrymedia.com",
                                "weidong.zhang@starrymedia.com", "chuantong.yang@starrymedia.com","xiaolei.wang@starrymedia.com","xiaoyan.qu@starrymedia.com"])


def send_feishu_message(url):
    # 飞书群机器人配置
    webhook_url = 'https://open.feishu.cn/open-apis/bot/v2/hook/14492d43-df60-4f67-beb2-bb3a5e3d2455'
    # 提到的人员列表
    mentioned_users = ["@陈龙","@周鲜鲜","@杨传桐"]

    # 构造飞书消息内容
    message = f"【Uptick API 测试报告】\n\n" \
              f"测试报告已生成，请相关人员查看,邮箱可查看或点击链接直接查看。\n" \
              f"{', '.join(mentioned_users)}\n" \
              f"测试报告链接：{url}"
    data = {
        "msg_type": "text",
        "content": {
            "text": message,
            "mentioned_list": [user[1:] for user in mentioned_users]
        }
    }

    try:
        # 发送飞书群消息
        response = requests.post(webhook_url, json=data)
        response.raise_for_status()
        print("飞书群消息发送成功")
    except requests.exceptions.RequestException as e:
        print("飞书群消息发送失败:", str(e))

def job():
    print("开始执行测试...")
    run_test()
    print("测试执行完成.")
# 推送消息到飞书群

    report_url = "http://192.168.111.23:8848/reports/upticknftapireport"+ datetime.date.today().strftime("%Y-%m-%d")+".html"
    send_feishu_message(report_url)

hour = "11"
minute = "00"

schedule.every().day.at(f"{hour}:{minute}").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

