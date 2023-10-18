import  unittest
import  unittestreport
import requests
import datetime

suite =unittest.defaultTestLoader.discover(r"/Users/starrymedia/PycharmProjects/upticknetwork/uptickapi_nft")
runner =unittestreport.TestRunner(suite,tester="colin_chen",title="Uptick接口自动化测试报告"+datetime.date.today().strftime("%Y-%m-%d"),filename="upticknftapireport.html",templates=2)
runner.run()
runner.send_email(host="smtp.exmail.qq.com",
                  port=465,
                  user="long.chen@starrymedia.com",
                  password="stHahERaHvsNEGSd",
                  to_addrs=["brian@uptickproject.com","xianxian.zhou@starrymedia.com","qia.fang@starrymedia.com","weidong.zhang@starrymedia.com","chuantong.yang@starrymedia.com"])




# import requests
#
# # 设置访问令牌和群组ID
# access_token = "YOUR_ACCESS_TOKEN"
# group_id = "YOUR_GROUP_ID"
#
# # 上传文件
# file_path = "path/to/your/file.html"
# file_name = "file.html"
# file_type = "text/html"
#
# upload_url = f"https://open.feishu.cn/open-apis/drive/explorer/v2/upload/file?access_token={access_token}"
# files = {
#     "file": (file_name, open(file_path, "rb"), file_type)
# }
# response = requests.post(upload_url, files=files)
# file_id = response.json()["data"]["file_id"]
#
# # 发送消息
# message_url = f"https://open.feishu.cn/open-apis/message/v4/send?access_token={access_token}"
# data = {
#     "chat_id": group_id,
#     "msg_type": "post",
#     "content": {
#         "post": {
#             "zh_cn": {
#                 "title": "HTML文件",
#                 "content": [
#                     [
#                         {
#                             "tag": "a",
#                             "text": "点击查看文件",
#                             "href": f"https://open.feishu.cn/open-apis/drive/explorer/v2/file/{file_id}"
#                         }
#                     ]
#                 ]
#             }
#         }
#     }
# }
# response = requests.post(message_url, json=data)


# import requests
#
#
# def send_link_to_feishu(webhook_url, group_id, title, url):
#     # 构建消息内容
#     content = {
#         "title": title,
#         "text": url
#     }
#     message = {
#         "msg_type": "post",
#         "content": content
#     }
#
#     # 发送请求
#     headers = {"Content-Type": "application/json"}
#     payload = {
#         "msg_type": "post",
#         "content": {
#             "post": message
#         },
#         "group_id": group_id
#     }
#     response = requests.post(webhook_url, json=payload, headers=headers)
#
#     # 打印响应结果
#     if response.status_code == 200:
#         print("链接已成功推送至飞书群组！")
#     else:
#         print("推送链接至飞书群组失败，错误代码：", response.status_code)
#
#
# # 调用函数发送链接至飞书群组
# webhook_url = "https://open.feishu.cn/open-apis/bot/v2/hook/f8222d54-ff14-47e2-9d27-af4e48cc4556"
# group_id = "xxxxxxxxxxxxxxxxxxxx"
# title = "推送链接示例"
# url = "https://wormhole.app/BjZlB#slmIXEP1bFue-11MvYgisg"
# send_link_to_feishu(webhook_url, group_id, title, url)