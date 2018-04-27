from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
# from linebot.models import (
#     MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
# )
from linebot.models import *
# add food
import random
food1=['金拱門','肯德基','摩斯漢堡','對面早餐店','宮口街蘿蔔糕米腸','喜德嘆烤三明治','Q Burger','吃自己','甲~土~豆~~','吃土','不告訴你','你有障礙我也幫不了你']
food2=['金拱門','肯德基','摩斯漢堡','炒飯炒麵','火鍋','快炒','牛排','自助餐','牛肉麵','腿庫飯','吃自己','甲~土~豆~~','吃土','不告訴你','你有障礙我也幫不了你']
food3=['金拱門','肯德基','摩斯漢堡','炒飯炒麵','火鍋','滷味','夜市','快炒','秦記','鐵板燒','牛排','牛肉麵','腿庫飯','自助餐','雞排','麻油雞','拿坡里','吃自己','甲~土~豆~~','吃土','不告訴你','你有障礙我也幫不了你']
food4=['金拱門','肯德基','摩斯漢堡','火鍋','夜市','阿婆','阿國','快炒','鐵板燒','牛排','牛肉麵','雞排','麻油雞','烤三小','吃自己','甲~土~豆~~','吃土','不告訴你','你有障礙我也幫不了你']
# google sheet start
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials

# scope=['https://spreadsheets.google.com/feeds']
# creds=ServiceAccountCredentials.from_json_keyfile_name('pythontest_clientsecret.json',scope)
# clients=gspread.authorize(creds)
# sheet=clients.open('pythontestupolad').sheet1

# google sheet end

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('5oAMkWBeFqMZgz8mxTZwVAp92H+MMo1LUjtH4B8BxD1QB3IVEcfZ+lgkXBODBnoqWjXcL/Te6Q4Qt2iPdKcbKg2nNl2CSSUaKD2TZCA/nTvU7Tt5mDyY+HzJnzqaLwMlaOXG2FfiGqnn1ELFDQdn8AdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('afa95c3baf13786604bcb5ab7da4dc2c')

# 監聽所有來自 /callback 的 Post Request
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
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event.message.text)
    if event.message.text=='吃':
        buttons_template = TemplateSendMessage(
            alt_text='eat template',
            template=ButtonsTemplate(
                title='選三餐有障礙嗎?',
                text='請選擇哪餐',
                #thumbnail_image_url='',
                actions=[
                    MessageTemplateAction(
                        label='早餐',
                        text='早餐'
                    ),
                    MessageTemplateAction(
                        label='午餐',
                        text='午餐'
                    ),
                    MessageTemplateAction(
                        label='晚餐',
                        text='晚餐'
                    ),
                    MessageTemplateAction(
                        label='宵夜',
                        text='宵夜'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text=='早餐':
        get=random.sample(food1,1)
        answer=get[0]
        print(answer)
        message = TextSendMessage(text='誠心建議:'+answer)
        line_bot_api.reply_message(
            event.reply_token,
            message)
        return 0
    if event.message.text=='午餐':
        get=random.sample(food2,1)
        answer=get[0]
        print(answer)
        message = TextSendMessage(text='誠心建議:'+answer)
        line_bot_api.reply_message(
            event.reply_token,
            message)
        return 0
    if event.message.text=='晚餐':
        get=random.sample(food3,1)
        answer=get[0]
        print(answer)
        message = TextSendMessage(text='誠心建議:'+answer)
        line_bot_api.reply_message(
            event.reply_token,
            message)
        return 0
    if event.message.text=='宵夜':
        get=random.sample(food4,1)
        answer=get[0]
        print(answer)
        message = TextSendMessage(text='誠心建議:'+answer)
        line_bot_api.reply_message(
            event.reply_token,
            message)
        return 0
    else:
        message = TextSendMessage(text='安安')
        print(message)
        line_bot_api.reply_message(
            event.reply_token,
             message)
        return 0

    # if event.message.text.find('吃')!=-1:
    #     message = TextSendMessage(text='甲~土~豆~~')
    #     line_bot_api.reply_message(
    #         event.reply_token,
    #         message)
    # else:
    #     message = TextSendMessage(text=event.message.text)
    #     line_bot_api.reply_message(
    #         event.reply_token,
    #         message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
