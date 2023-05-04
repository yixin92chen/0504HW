from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('ExOBSOPApdGavT3XgkJGgyK1YhXSjkltQJIJMgcNw2yctGl4kzFenb3gJc5zufk3np6ZezBT6U+vbtUvHbhgyuH7RmUMVySv0QzoBfMygx7wjCKKmfHE5+l4qt90EeRtQ+9HrszMfOQK+ml8aaG5SwdB04t89/1O/w1cDnyilFU=**')
handler = WebhookHandler('fe4dba9003f1288b360feac3135139d6')

@app.route("/")
def home():
    return"LINE BOT API SERVER IS RUNNING"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()