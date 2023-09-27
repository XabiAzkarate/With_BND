import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackContext, Updater
from . import BisectionSearch

TOKEN = os.environ.get('XABIER_ROCKET_BOT_API_TOKEN')
VIDEO_NAME = os.environ.get('VIDEO_NAME')

search = BisectionSearch(VIDEO_NAME)

def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_text(f'Hi {user.first_name}! Ready to find the rocket launch frame?')

    # Start the bisection process
    frame = search.get_mid_frame()
    frame_data = search.retrieve_frame(frame)

    # You can now send the frame_data to the user and ask them if the rocket has launched.

def main() -> None:
    updater = Updater(token=TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    # Add more handlers to process user's feedback about the rocket launch
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

def ask_user_about_frame(update: Update, frame_data: dict):
    # Show the frame to the user (however you've planned, maybe as an image or a link)
    keyboard = [
        [InlineKeyboardButton("Rocket has launched", callback_data='launched'),
         InlineKeyboardButton("Rocket has not launched", callback_data='not_launched')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Has the rocket launched in this frame?', reply_markup=reply_markup)

def handle_user_feedback(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()  # End the loading state of the button
    if query.data == 'launched':
        search.update_bounds(True)
    else:
        search.update_bounds(False)
    next_frame = search.get_mid_frame()
    next_frame_data = search.retrieve_frame(next_frame)
    ask_user_about_frame(update, next_frame_data)
