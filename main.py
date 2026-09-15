import telebot

TOKEN = '8704965523:AAEYPGvRQRi20XthfCM-VXc0IoKzB6Yi860'
ADMIN_ID = 8287138856

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.from_user.id != ADMIN_ID:
        bot.reply_to(message, "Access denied. Admin only.")
        return
    
    bot.send_message(
        message.chat.id, 
        "Welcome Admin 🦅\nBot is active and running successfully!"
    )

if __name__ == '__main__':
    print("Bot is starting...")
    bot.infinity_polling(skip_pending=True)
