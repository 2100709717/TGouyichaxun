import os
import logging
import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from telegram.ext import MessageHandler, Filters

TOKEN = '6422333905:AAETWOz25Ctil7BFaD7HS4LLdPh5t5tMjQw'

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('bot_log.txt'), logging.StreamHandler()])
logger = logging.getLogger(__name__)

# 获取卖出列表的函数
def get_sell_list():
    headers = {
        'referer': 'https://www.okx.com/zh-hans/p2p-markets/cny/buy-usdt',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    }

    response = requests.get(
        'https://www.okx.com/v3/c2c/tradingOrders/books?quoteCurrency=CNY&baseCurrency=USDT&side=sell&paymentMethod=all&userType=all&receivingAds=false',
        headers=headers)

    if response.status_code == 200:
        data = response.json()
        sell_list = data['data']['sell'][:10]  # 只取前10个数据

        result = []

        for item in sell_list:
            if 'nickName' in item and 'price' in item:
                result.append(f"💎{item['price']}   {item['nickName']}")


            else:
                result.append("缺少 nickName 或 price 属性")

        return "\n".join(result)
    else:
        return "无法获取数据，请稍后再试。"

def get_sell_list2():
    headers = {
        'referer': 'https://www.okx.com/zh-hans/p2p-markets/cny/buy-usdt',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    }

    response = requests.get(
        'https://www.okx.com/v3/c2c/tradingOrders/books?quoteCurrency=CNY&baseCurrency=USDT&side=sell&paymentMethod=bank&userType=all&receivingAds=false',
        headers=headers)

    if response.status_code == 200:
        data = response.json()
        sell_list = data['data']['sell'][:10]  # 只取前10个数据
        result = []

        for item in sell_list:
            if 'nickName' in item and 'price' in item:
                result.append(f"💎{item['price']}   {item['nickName']}")
            else:
                result.append("缺少 nickName 或 price 属性")

        return "\n".join(result)
    else:
        return "无法获取数据，请稍后再试。"

def get_sell_list3():
    headers = {
        'referer': 'https://www.okx.com/zh-hans/p2p-markets/cny/buy-usdt',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    }

    response = requests.get(
        'https://www.okx.com/v3/c2c/tradingOrders/books?quoteCurrency=CNY&baseCurrency=USDT&side=sell&paymentMethod=aliPay&userType=all&receivingAds=false',
        headers=headers)

    if response.status_code == 200:
        data = response.json()
        sell_list = data['data']['sell'][:10]  # 只取前10个数据
        result = []

        for item in sell_list:
            if 'nickName' in item and 'price' in item:
                result.append(f"💎{item['price']}   {item['nickName']}")
            else:
                result.append("缺少 nickName 或 price 属性")

        return "\n".join(result)
    else:
        return "无法获取数据，请稍后再试。"

def get_sell_list4():
    headers = {
        'referer': 'https://www.okx.com/zh-hans/p2p-markets/cny/buy-usdt',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    }

    response = requests.get(
        'https://www.okx.com/v3/c2c/tradingOrders/books?quoteCurrency=CNY&baseCurrency=USDT&side=sell&paymentMethod=wxPay&userType=all&receivingAds=false',
        headers=headers)

    if response.status_code == 200:
        data = response.json()
        sell_list = data['data']['sell'][:10]  # 只取前10个数据
        result = []

        for item in sell_list:
            if 'nickName' in item and 'price' in item:
                result.append(f"💎{item['price']}   {item['nickName']}")
            else:
                result.append("缺少 nickName 或 price 属性")

        return "\n".join(result)
    else:
        return "无法获取数据，请稍后再试。"

# 处理开始命令
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('欢迎使用本机器人！请输入“查询”以获取卖出列表。')

# 处理按钮点击
def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    user = update.effective_user
    logger.info(f"User {user.first_name} clicked on {query.data}")

    menu1_text = "全部"
    menu2_text = "银行卡"
    menu3_text = "支付宝"
    menu4_text = "微信"

    if query.data == 'menu1':
        menu1_text = "✅ " + menu1_text
        sell_list = get_sell_list()
    elif query.data == 'menu2':
        menu2_text = "✅ " + menu2_text
        sell_list = get_sell_list2()
    elif query.data == 'menu3':
        menu3_text = "✅ " + menu3_text
        sell_list = get_sell_list3()
    elif query.data == 'menu4':
        menu4_text = "✅ " + menu4_text
        sell_list = get_sell_list4()

    keyboard = [
        [
            InlineKeyboardButton(menu1_text, callback_data='menu1'),
            InlineKeyboardButton(menu2_text, callback_data='menu2'),
            InlineKeyboardButton(menu3_text, callback_data='menu3'),
            InlineKeyboardButton(menu4_text, callback_data='menu4'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text(text=sell_list, reply_markup=reply_markup)

    if query.data == 'menu1':
        # 调用获取卖出列表的函数
        sell_list = get_sell_list()
        query.edit_message_text(text=sell_list, reply_markup=reply_markup)
    elif query.data == 'menu2':
        sell_list = get_sell_list2()
        query.edit_message_text(text=sell_list, reply_markup=reply_markup)
    elif query.data == 'menu3':
        sell_list = get_sell_list3()
        query.edit_message_text(text=sell_list, reply_markup=reply_markup)
    elif query.data == 'menu4':
        sell_list = get_sell_list4()
        query.edit_message_text(text=sell_list, reply_markup=reply_markup)

def message_handler(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    message = update.message.text
    logger.info(f"User {user.first_name} sent message: {message}")
    if message == "查询":
        # 获取卖出列表
        sell_list = get_sell_list()
        # 创建键盘
        keyboard = [
            [
                InlineKeyboardButton("全  部", callback_data='menu1'),
                InlineKeyboardButton("银行卡", callback_data='menu2'),
                InlineKeyboardButton("支付宝", callback_data='menu3'),
                InlineKeyboardButton("微  信", callback_data='menu4'),
            ],
        ]
        # 创建回复标记
        reply_markup = InlineKeyboardMarkup(keyboard)
        # 发送带有按钮的消息
        update.message.reply_text(sell_list, reply_markup=reply_markup)
    else:
        update.message.reply_text('请输入“查询”以获取卖出列表。')

def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler))  # 添加这个处理器

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
