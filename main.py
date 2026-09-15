import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '8901696840:AAGnqo20y0...'
ADMIN_ID = 8287138856

bot = telebot.TeleBot(TOKEN)

def is_admin(user_id):
    return user_id == ADMIN_ID

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if not is_admin(message.from_user.id):
        bot.reply_to(message, "Access denied. Admin only.")
        return
    
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("Screenshot", callback_data='get_screenshot'),
        InlineKeyboardButton("Files", callback_data='get_files'),
        InlineKeyboardButton("Camera", callback_data='get_camera'),
        InlineKeyboardButton("Device Info", callback_data='get_info')
    )
    
    bot.send_message(
        message.chat.id, 
        "Welcome Admin 🦅\nChoose an option below:", 
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.from_user.id != ADMIN_ID:
        return
    
    if call.data == 'get_screenshot':
        bot.answer_callback_query(call.id, "Requesting screenshot...")
        bot.send_message(call.message.chat.id, "Capturing screen...")
    elif call.data == 'get_files':
        bot.answer_callback_query(call.id, "Accessing files...")
        bot.send_message(call.message.chat.id, "Fetching file list...")
    elif call.data == 'get_camera':
        bot.answer_callback_query(call.id, "Accessing camera...")
        bot.send_message(call.message.chat.id, "Taking camera snapshot...")
    elif call.data == 'get_info':
        bot.answer_callback_query(call.id, "Getting info...")
        bot.send_message(call.message.chat.id, "Device is online.")

if __name__ == '__main__':
    print("Bot is running...")
    bot.infinity_polling()
