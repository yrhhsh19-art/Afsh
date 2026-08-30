import os
import telebot
from flask import Flask, request

# سحب توكن البوت تلقائياً من إعدادات الاستضافة
TOKEN = os.environ.get("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

# رقم الأيدي الخاص بك الذي يملك صلاحية التحكم الكامل
MY_ADMIN_ID = 8287138856

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is active and running!"

# استقبال أوامر وتحكم البوت
@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    if message.from_user.id == MY_ADMIN_ID:
        # الأوامر الخاصة بك كمطور ومالك للبوت
        text = message.text
        if text == '/start':
            bot.reply_to(message, "أهلاً بك يا علي! البوت يعمل بكامل طاقتك وجاهز لأوامرك.")
        else:
            bot.reply_to(message, f"أمرني يا مالكي، استلمت أمرك: {text}")
    else:
        bot.reply_to(message, "عذراً، هذا البوت خاص ولا يسمح لأحد غير المالك بالتحكم فيه.")

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return "OK", 200
    else:
        return "Forbidden", 403

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
