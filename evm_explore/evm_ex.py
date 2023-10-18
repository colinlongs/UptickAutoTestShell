import requests
import schedule
import time

url = "https://evm-explorer.uptick.network"

webhook_url = "https://open.feishu.cn/open-apis/bot/v2/hook/14492d43-df60-4f67-beb2-bb3a5e3d2455"

def check_website():
    try:
        response = requests.get(url)

        if response.status_code == 200:
            message = "EVM浏览器网页正常运行"
        else:
            message = f"EVM浏览器网页异常，速查看！状态码: {response.status_code}"

        data = {
            "msg_type": "text",
            "content": {
                "text": message
            }
        }


        response = requests.post(webhook_url, json=data)
        response.raise_for_status()
        print("消息已发送到飞书")


    except requests.exceptions.RequestException as e:
        print("无法连接到网页:", str(e))

schedule.every(2).hours.do(check_website)

while True:
    schedule.run_pending()
    time.sleep(7200)