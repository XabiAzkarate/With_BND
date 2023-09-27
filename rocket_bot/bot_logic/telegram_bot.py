from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackContext, Updater, CallbackQueryHandler
from . import BisectionSearch
from decouple import config

TOKEN = config('XABIER_ROCKET_BOT_API_TOKEN')
VIDEO_NAME = config('VIDEO_NAME')

bisection_logic = BisectionSearch(VIDEO_NAME)

def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_text(f'Hi {user.first_name}! Ready to find the rocket launch frame?')

    frame = bisection_logic.get_mid_frame()
    frame_url = bisection_logic.retrieve_frame(frame)

    ask_user_about_frame(update, frame_url)

def ask_user_about_frame(update: Update, frame_url: str):

    # Check if this is a callback or a new message
    if update.callback_query:
        message = update.callback_query.message
    else:
        message = update.message

    message.reply_photo(photo=frame_url, caption="Examine the frame above.")
    
    keyboard = [
        [InlineKeyboardButton("Rocket has launched", callback_data='launched'),
         InlineKeyboardButton("Rocket has not launched", callback_data='not_launched')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    message.reply_text('Has the rocket launched in this frame?', reply_markup=reply_markup)

def handle_user_feedback(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    if query.data == 'launched':
        bisection_logic.update_bounds(True)
    else:
        bisection_logic.update_bounds(False)

    if bisection_logic.low == bisection_logic.high:
        query.message.reply_text(f"The rocket launch frame is identified as frame number {bisection_logic.low}.")
    else:
        next_frame = bisection_logic.get_mid_frame()
        next_frame_data = bisection_logic.retrieve_frame(next_frame)
        ask_user_about_frame(update, next_frame_data)

def main() -> None:
    if not TOKEN:
        raise ValueError("Telegram bot token is not set!")

    updater = Updater(token=TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(handle_user_feedback))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
