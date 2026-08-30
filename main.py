
import os
import telebot

# سحب توكن البوت تلقائياً من إعدادات الاستضافة
bot = telebot.TeleBot("8901696840:AAGnqo20y0jnPdCdTAvEfB_QXVHx7YwsOS4")




# رقم الأيدي الخاص بك الذي يملك صلاحية التحكم الكامل
MY_ADMIN_ID = 8287138856

# استقبال أوامر وتحكم البوت
@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    if message.from_user.id == MY_ADMIN_ID:
        text = message.text
        if text == '/start':
            bot.reply_to(message, "أهلاً بك يا علي! البوت يعمل بكامل طاقتك وجاهز لأوامرك.")
        else:
            bot.reply_to(message, f"أمرني يا مالكي، استلمت أمرك: {text}")
    else:
        bot.reply_to(message, "عذراً، هذا البوت خاص ولا يسمح لأحد غير المالك بالتحكم فيه.")

if __name__ == '__main__':
    # إزالة أي ويبهوك قديم عالق وتشغيل البوت مباشرة
    bot.remove_webhook()
    print("Bot is running with polling...")
    bot.infinity_polling()
