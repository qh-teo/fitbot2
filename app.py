import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from config import TOKEN

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    # keyboard = [[InlineKeyboardButton("Option 1", callback_data='1'),
    #              InlineKeyboardButton("Option 2", callback_data='2')],
    #             [InlineKeyboardButton("Option 3", callback_data='3')]]
    #
    # reply_markup = InlineKeyboardMarkup(keyboard)
    #
    # update.message.reply_text('Please choose:', reply_markup=reply_markup)
    update.message.reply_text(main_menu_message(),
                              reply_markup=main_menu_keyboard())


def main_menu(update,context):
    print(update.callback_query.data)
    query = update.callback_query
    print(query)
    context.edit_message_text(chat_id=query.message.chat_id,
                                  message_id=query.message.message_id,
                                  text=main_menu_message(),
                                  reply_markup=main_menu_keyboard())



# def first_menu(context, update):
#     query = update.callback_query
#     print(query)
#     query.edit_message_text(chat_id=query.message.chat_id,
#                                 message_id=query.message.message_id,
#                                 text=first_menu_message(),
#                                 reply_markup=first_menu_keyboard())
#     print("hello")
#
# # and so on for every callback_data option
# def first_submenu(bot, update):
#     pass
#
#
# def second_submenu(bot, update):
#   pass


################ Keyboard #######################
def main_menu_keyboard():
    keyboard = [[InlineKeyboardButton("Option 1", callback_data='1'),
                 InlineKeyboardButton("Option 2", callback_data='m2')],
                [InlineKeyboardButton("Option 3", callback_data='m3')]]
    return InlineKeyboardMarkup(keyboard)


# def first_menu_keyboard():
#     keyboard = [[InlineKeyboardButton('Submenu 1-1', callback_data='m1_1')],
#               [InlineKeyboardButton('Submenu 1-2', callback_data='m1_2')],
#               [InlineKeyboardButton('Main menu', callback_data='main')]]
#     return InlineKeyboardMarkup(keyboard)


####### Messages ############
def main_menu_message():
    return 'Choose the option in main menu:'


def first_menu_message():
    return 'Choose the submenu in first menu:'


def button(update, context):
    query = update.callback_query
    print(query)
    # name = context
    print(update.callback_query.message.chat.first_name)
    if query.data == "1":
        menu_1 = [[InlineKeyboardButton('Submenu 1-1', callback_data='m1_1')],
                  [InlineKeyboardButton('Submenu 1-2', callback_data='m1_2')]]
        reply_markup = InlineKeyboardMarkup(menu_1)
        context.bot.edit_message_text(chat_id=query.message.chat_id,
                                      message_id=query.message.message_id,
                                      text='Choose the option:',
                                      reply_markup=reply_markup)


def help(update, context):
    update.message.reply_text("Use /start to test this bot.")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
    # updater.dispatcher.add_handler(CallbackQueryHandler(first_menu, pattern='m1'))
    # updater.dispatcher.add_handler(CallbackQueryHandler(first_submenu,
    #                                                     pattern='m1_1'))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
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

