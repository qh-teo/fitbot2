import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, callbackcontext
from config import TOKEN

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text(main_menu_message(),
                              reply_markup=main_menu_keyboard())


def main_menu(update,context):
    query = update.callback_query
    context.bot.edit_message_text(chat_id=query.message.chat_id,
                                  message_id=query.message.message_id,
                                  text=main_menu_message(),
                                  reply_markup=main_menu_keyboard())


def first_menu(update, context):
    query = update.callback_query
    # print(context.match)
    context.bot.edit_message_text(chat_id=query.message.chat_id,
                                  message_id=query.message.message_id,
                                  text=first_menu_message(),
                                  reply_markup=first_menu_keyboard())

def second_menu(update, context):
    query = update.callback_query
    # print(context.match)
    context.bot.edit_message_text(chat_id=query.message.chat_id,
                                  message_id=query.message.message_id,
                                  text=second_menu_message(),
                                  reply_markup=second_menu_keyboard())


# def second_menu(update, context):
#     query = update.callback_query
#     context.bot.edit_message_text(chat_id=query.message.chat_id,
#                                   message_id=query.message.message_id,
#                                   text=second_menu_message(),
#                                   reply_markup=second_menu_keyboard())


# and so on for every callback_data option
def first_submenu(bot, update):
    pass


def second_submenu(bot, update):
    pass


################ Keyboard #######################
def main_menu_keyboard():
    keyboard = [[InlineKeyboardButton("Option 1", callback_data='m1'),
                 InlineKeyboardButton("Option 2", callback_data='m2')],
                [InlineKeyboardButton("Option 3", callback_data='m3')]]
    return InlineKeyboardMarkup(keyboard)


def first_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Submenu 1-1', callback_data='m1_1')],
              [InlineKeyboardButton('Submenu 1-2', callback_data='m1_2')],
              [InlineKeyboardButton('Main menu', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)


def second_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Submenu 2-1', callback_data='m2_1')],
              [InlineKeyboardButton('Submenu 2-2', callback_data='m2_2')],
              [InlineKeyboardButton('Main menu', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)




####### Messages ############
def main_menu_message():
    return 'Choose the option in main menu:'


def first_menu_message():
    return 'Choose the submenu in first menu:'


def second_menu_message():
    return 'Choose the submenu in second menu:'

######## Other commands ###############


def help(update, context):
    update.message.reply_text("Use /start to test this bot.")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
    updater.dispatcher.add_handler(CallbackQueryHandler(first_menu, pattern='m1'))

    updater.dispatcher.add_handler(CallbackQueryHandler(second_menu, pattern='m2'))

    updater.dispatcher.add_handler(CallbackQueryHandler(first_submenu, pattern='m1_1'))
    updater.dispatcher.add_handler(CallbackQueryHandler(second_submenu, pattern='m2_1'))

    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    updater = Updater(TOKEN, use_context=True)
    main()

