# save this as app.py
# Hello World
from flask import *
from linebot import *
from linebot.models import *
import sqlite3
import datetime
import requests

app = Flask(__name__)
line_bot_api = LineBotApi('1N/b770dxp0RGhcUgQVg/dGH3PLuq74n/BMSgJEm8dpqu16dKCPOxLLp856/E3UbQGBfoiLp+m41MqZjIpTc4fsWJ7Jb7Fo1UUWB52Q8C5aoMirMQLnLIgxLIFSUIB8PhoDF22fGKTS2IxYYN15k5wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('ed7025837ae891bd0bc288f3601caa6c')

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/webhook',methods=['POST'])
def hello():
    req = request.get_json(silent=True, force=True)
    intent = req['queryResult']['intent']['displayName']
    id_user = req['originalDetectIntentRequest']['payload']['data']['source']['userId']
    reply_token = req['originalDetectIntentRequest']['payload']['data']['replyToken']
    print(req)
    reply(intent, reply_token, req, id_user)
    return req

def reply(intent, reply_token, req, id_user):
    if intent == 'Intent-Buy - custom':
        id_item = str(req['queryResult']['outputContexts'][0]['parameters']['id_item.original']) # Database is string table , So chang id_item is string
        count_number = str(req['queryResult']['outputContexts'][0]['parameters']['count_number.original']) # Database is string table , So chang count_number is string same
        print(id_item, count_number)
        conn = sqlite3.connect('product.db')
        c = conn.cursor()
        c.execute("SELECT * FROM items WHERE id_item == '{}'".format(id_item))
        product = c.fetchall() # keeping selected  Database

        # User enters a product code that "does not" exist in Database
        if product == []:
            text_message = TextSendMessage(text='ไม่มีรหัสสินค้านี้ครับ')
            line_bot_api.reply_message(reply_token,text_message)

        # User enters a product code that "does" exist in Database
        else:
            confirm_template_message = TemplateSendMessage(
                alt_text='Confirm template',
                template=ConfirmTemplate(
                    text='ต้องการซื้อรหัสสินค้า {} จำนวน {} ใช่หรือไม่'.format(id_item, count_number),
                    actions=[
                         MessageAction(
                        label='ใช่',
                        text='ซื้อสินค้ารหัส {} จำนวน {}'.format(id_item, count_number)
                    ),
                    MessageAction(
                        label='ไม่ใช่',
                        text='สั่งซื้อสินค้า'
                    )
                ]
            )
        )
        line_bot_api.reply_message(reply_token,confirm_template_message)

    # Check good in store
    if intent == 'Intent-Buy - custom - yes':
        id_item = str(req['queryResult']['outputContexts'][0]['parameters']['id_item.original']) # Database is string table , So chang id_item is string
        count_number = str(req['queryResult']['outputContexts'][0]['parameters']['count_number.original']) # Database is string table , So chang count_number is string same
        conn = sqlite3.connect('product.db')
        c = conn.cursor()
        c.execute("SELECT * FROM items WHERE id_item == '{}' ".format(id_item))
        product = c.fetchall()
        if int(count_number) > int(product[0][2]):
            text_message = TextSendMessage(text='จำนวนสินค้าไม่เพียงพอครับ')
            line_bot_api.reply_message(reply_token,text_message)

        # update database when user is buying
        else:
            total = int(product[0][2]) - int(count_number)
            conn = sqlite3.connect('product.db')
            c = conn.cursor()
            c.execute("""Update items set sum = ? WHERE id_item = ?""",
                      (total, id_item))
            conn.commit()

            # insert data buying in order table
            id = None
            date = datetime.datetime.now()
            conn = sqlite3.connect('product.db')
            c = conn.cursor()
            c.execute("""INSERT INTO oder VALUES(?,?,?,?,?)""",
                      (id, id_user, id_item, count_number, date))
            conn.commit()
            text_message = TextSendMessage(text='บันทึกการสั่งซื้อสำเร็จครับ')
            line_bot_api.reply_message(reply_token,text_message)
    # Check Order in Store Database
    if intent == 'Intent-order':
        conn = sqlite3.connect('product.db')
        c = conn.cursor()
        c.execute("""SELECT * FROM oder WHERE id_user == '{}'""".format(id_user))
        product = c.fetchall()
        if product == []:
            text_message = TextSendMessage(text='คุณลูกค้ายังไม่เคยสั่งนะครับ')
            line_bot_api.reply_message(reply_token,text_message)

        # user used to buy order is store
        else:
            textlist = ''
            for i in product:
                textstring = 'รหัส {} จำนวณ {} เวลา {} \n'.format(i[2], i[3], i[4])
                textlist = textlist + textstring
            text_message = TextSendMessage(text=textlist)
            line_bot_api.reply_message(reply_token, text_message)

    # show all order in store
    if intent == 'Intent-Items':
        conn = sqlite3.connect('product.db')
        c = conn.cursor()
        c.execute("""SELECT * FROM Items""")
        product = c.fetchall()
        if product == []:
            text_message = TextSendMessage(text='ไม่มีสินค้าเหลืออยู่ในตอนนี้')
            line_bot_api.reply_message(reply_token, text_message)

        # case order have in stored
        else:
            textlist = ''
            for i in product:
                textstring = 'รหัส {} จำนวณ {} \n'.format(i[1], i[2])
                textlist = textlist + textstring
            text_message = TextSendMessage(text=textlist)
            line_bot_api.reply_message(reply_token, text_message)

     # Chat
    if intent == 'Intent-Chat':
        line_bot_api.link_rich_menu_to_user(id_user, 'richmenu-75b7b1b107d1c3617593fce43b3e3000')
        text_message = TextSendMessage(text='พูดคุยกับเราได้เลยครับ')
        line_bot_api.reply_message(reply_token, text_message)

    if intent == 'Intent-Chat-out':
        confirm_template_message = TemplateSendMessage(
                alt_text='Confirm template',
                template=ConfirmTemplate(
                    text='ต้องการหยุดการสนทนาหรือไม่',
                    actions=[
                         MessageAction(
                        label='ใช่',
                        text='ใช่'
                    ),
                    MessageAction(
                        label='ไม่ใช่',
                        text='พูดคุยทั่วไป'
                    )
                ]
            )
        )
        line_bot_api.reply_message(reply_token, confirm_template_message)

    if intent == 'Intent-Chat-out - yes':
        line_bot_api.unlink_rich_menu_from_user(id_user)

    if intent == 'Intent-Covid19':
        data = requests.get('https://covid19.ddc.moph.go.th/api/Cases/today-cases-all') # request to API
        json_data = json.loads(data.text) # change json to .text
        print(json_data)
        Confirmed = json_data[0]['total_case'] # total human have virus
        Recovered = json_data[0]['total_recovered'] # total human healed
        Excludeabroad = json_data[0]['total_case_excludeabroad'] # total human healing
        Deaths = json_data[0]['total_death'] # total human die
        Newconfirmed = json_data[0]['new_case'] # total new human have virus
        Update_date = json_data[0]['update_date'] # total new update date

        text_message = TextSendMessage(
            text='ยอดผู้ติดเชื้อสะสม : {}\nหายแล้ว : {}\nยอดผู้ติดเชื้อทั้งหมด(ไม่รวมชาวต่างขาติ) : {}\nยอดผู้เสียชีวิต : {}\nติดเชื้อเพิ่ม : {}\nวันที่ : {}'.format(
                Confirmed, Recovered, Excludeabroad, Deaths, Newconfirmed, Update_date))
        line_bot_api.reply_message(reply_token, text_message)

    if intent == 'intent-liff':
        text_message = TextSendMessage(text='https://liff.line.me/1656745423-vkmZNkro')
        line_bot_api.reply_message(reply_token, text_message)

if __name__=='__main__':
    app.run(debug=True)

