from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

app = Flask(__name__)

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi('pXjiePH6FQbZUb9HfySy7Z4N9UskbxR/oeqSyAhlpge9Ckev3im+gknVWbDlyhWqKqjwgrJtE4epbOqlGkgZaGXmzwxXuSH7Kx2hMzi4BINws6n0T4BD7lV6hlRdp4Hrhk9rhsDjOLYXA/yTS79zVAdB04t89/1O/w1cDnyilFU=
')
handler = WebhookHandler('10f166d1105c29a3c8e6cd43086d8cef')

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

if __name__ == "__main__":
    app.run()
