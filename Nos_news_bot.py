import telebot
import nosConst


from telegram import Bot
from telegram import Update
from telegram import ParseMode
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import CallbackQueryHandler


bot = telebot.TeleBot(nosConst.TOKEN)


def get_keyboard_st():

    keyboard = [[InlineKeyboardButton(nosConst.GUIDE[nosConst.callback_start], callback_data="button_start")]]
    return InlineKeyboardMarkup(keyboard)


def get_keyboard_interest():
    keyboard = [
        [InlineKeyboardButton(nosConst.TITELES[nosConst.callback_news], callback_data="button_news"),
         InlineKeyboardButton(nosConst.TITELES[nosConst.callback_music], callback_data="button_music")],
        [InlineKeyboardButton(nosConst.TITELES[nosConst.callback_18], callback_data="button_18"),
         InlineKeyboardButton(nosConst.TITELES[nosConst.callback_crypto], callback_data="button_crypto")],
        [InlineKeyboardButton(nosConst.TITELES[nosConst.callback_art], callback_data="button_art"),
         InlineKeyboardButton(nosConst.TITELES[nosConst.callback_study], callback_data="button_study")],
        [InlineKeyboardButton(nosConst.TITELES[nosConst.callback_sport], callback_data="button_sport"),
         InlineKeyboardButton(nosConst.TITELES[nosConst.callback_tech], callback_data="button_tech")],
        [InlineKeyboardButton(nosConst.TITELES[nosConst.callback_sale], ccallback_data="button_sale"),
         InlineKeyboardButton(nosConst.TITELES[nosConst.callback_politics], callback_data="button_politics")],
        [InlineKeyboardButton(nosConst.TITELES[nosConst.callback_video], callback_data="button_video"),
         InlineKeyboardButton(nosConst.TITELES[nosConst.callback_travel], callback_data="button_travel")],
        [InlineKeyboardButton(nosConst.TITELES[nosConst.callback_fashion], callback_data="button_fashion"),
         InlineKeyboardButton(nosConst.TITELES[nosConst.callback_psy], callback_data="button_psy")],
        [InlineKeyboardButton(nosConst.TITELES[nosConst.callback_games], callback_data="button_games"),
         InlineKeyboardButton(nosConst.TITELES[nosConst.callback_books], callback_data="button_books")],
        [InlineKeyboardButton(nosConst.TITELES[nosConst.callback_markating], callback_data="button_markating"),
         InlineKeyboardButton(nosConst.TITELES[nosConst.callback_cars], callback_data="button_cars")],
        [InlineKeyboardButton(nosConst.TITELES[nosConst.callback_cook], callback_data="button_cook"),
         InlineKeyboardButton(nosConst.TITELES[nosConst.callback_economy], callback_data="button_economy")],
        [InlineKeyboardButton(nosConst.TITELES[nosConst.callback_telegram], callback_data="button_telegram"),
         InlineKeyboardButton(nosConst.TITELES[nosConst.callback_lingvo], callback_data="button_lingvo")],
        [InlineKeyboardButton(nosConst.TITELES[nosConst.callback_family], callback_data="button_family"),
         InlineKeyboardButton(nosConst.TITELES[nosConst.callback_design], callback_data="button_design")],
        [InlineKeyboardButton(nosConst.TITELES[nosConst.callback_med], callback_data="button_med"),
         InlineKeyboardButton(nosConst.TITELES[nosConst.callback_handmade], callback_data="button_handmade")],
        [InlineKeyboardButton(nosConst.TITELES[nosConst.callback_animal], callback_data="button_animal"),
         InlineKeyboardButton(nosConst.TITELES[nosConst.callback_apps], callback_data="button_apps")],
        [InlineKeyboardButton(nosConst.TITELES[nosConst.callback_interesting], callback_data="button_interesting"),
         InlineKeyboardButton(nosConst.TITELES[nosConst.callback_films], callback_data="button_films")],
        [InlineKeyboardButton(nosConst.GUIDE[nosConst.callback_next], callback_data="button_next")]
                ]
    return InlineKeyboardMarkup(keyboard)

kek =get_keyboard_interest()

def get_keyboard_country():
    keyboard = [
        [InlineKeyboardButton(nosConst.TITELES[nosConst.callback_az], callback_data="button_az")],
        [InlineKeyboardButton(nosConst.TITELES[nosConst.callback_ar], callback_data="button_ar"),
         InlineKeyboardButton(nosConst.TITELES[nosConst.callback_be], callback_data="button_be")],
        [InlineKeyboardButton(nosConst.TITELES[nosConst.callback_gr], callback_data="button_gr"),
         InlineKeyboardButton(nosConst.TITELES[nosConst.callback_ka], callback_data="button_ka")],
        [InlineKeyboardButton(nosConst.TITELES[nosConst.callback_ki], callback_data="button_ki"),
         InlineKeyboardButton(nosConst.TITELES[nosConst.callback_la], callback_data="button_la")],
        [InlineKeyboardButton(nosConst.TITELES[nosConst.callback_li], callback_data="button_li"),
         InlineKeyboardButton(nosConst.TITELES[nosConst.callback_mo], callback_data="button_mo")],
        [InlineKeyboardButton(nosConst.TITELES[nosConst.callback_ro], callback_data="button_ro"),
         InlineKeyboardButton(nosConst.TITELES[nosConst.callback_uz], callback_data="button_uz")],
        [InlineKeyboardButton(nosConst.TITELES[nosConst.callback_uk], callback_data="button_uk"),
         InlineKeyboardButton(nosConst.TITELES[nosConst.callback_es], callback_data="button_es")],
        [InlineKeyboardButton(nosConst.GUIDE[nosConst.callback_next], callback_data="button_next")]
              ]
    return InlineKeyboardMarkup(keyboard)


def get_keyboard_source():
    keyboard=[
        [InlineKeyboardButton(nosConst.TITELES[nosConst.callback_channel], callback_data="button_channel")],
        [InlineKeyboardButton(nosConst.TITELES[nosConst.callback_bot], callback_data="button_bot"),
         InlineKeyboardButton(nosConst.TITELES[nosConst.callback_chat], callback_data="button_chat")],
        [InlineKeyboardButton(nosConst.GUIDE[nosConst.callback_next], callback_data="button_next")]
              ]
    return InlineKeyboardMarkup(keyboard)


@bot.message_handler(commands=["start"])
def handle_text(message):
    bot.send_message(
        chat_id=message.chat.id,
        text="Привет! Отправь мне что-нибудь"
    )


@bot.message_handler(commands=["1"])
def handle_text(message):
    bot.send_message(message.chat.id, 'YRA nos')


bot.polling(none_stop=True, interval=0)