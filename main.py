import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# التوكن ومعرف المدير الخاص بك
TOKEN = '8901696840:AAGnqo20y0...'
ADMIN_ID = 8287138856

bot = telebot.TeleBot(TOKEN)

# التحقق من أن المستخدم هو المالك
def is_admin(user_id):
    return user_id == ADMIN_ID

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if not is_admin(message.from_user.id):
        bot.reply_to(message, "عذراً، هذا البوت خاص للمالك فقط.")
        return
    
    # إنشاء لوحة مفاتيح تفاعلية (أزرار)
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("📸 صورة شاشة", callback_data='get_screenshot'),
        InlineKeyboardButton("📁 الملفات", callback_data='get_files'),
        InlineKeyboardButton("📷 الكاميرا", callback_data='get_camera'),
        InlineKeyboardButton("ℹ️ معلومات الجهاز", callback_data='get_info')
    )
    
    bot.send_message(
        message.chat.id, 
        "أهلاً بك يا مالك النظام 🦅\nاختر العملية المطلوبة من القائمة أدناه:", 
        reply_markup=markup
    )

# التعامل مع الضغط على الأزرار
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.from_user.id != ADMIN_ID:
        return
    
    if call.data == 'get_screenshot':
        bot.answer_callback_query(call.id, "جاري طلب لقطة الشاشة...")
        bot.send_message(call.message.chat.id, "⏳ جاري التقاط الشاشة من الجهاز المستهدف...")
    elif call.data == 'get_files':
        bot.answer_callback_query(call.id, "جاري فتح تصفح الملفات...")
        bot.send_message(call.message.chat.id, "📁 قائمة الملفات قيد الجلب...")
    elif call.data == 'get_camera':
        bot.answer_callback_query(call.id, "جاري طلب الكاميرا...")
        bot.send_message(call.message.chat.id, "📷 يتم الآن التقاط الصورة...")
    elif call.data == 'get_info':
        bot.answer_callback_query(call.id, "جاري جلب المعلومات...")
        bot.send_message(call.message.chat.id, "📱 معلومات الجهاز: متصل وجاهز.")

# تشغيل البوت
if __name__ == '__main__':
    print("البوت يعمل الآن ويستقبل الأوامر...")
    bot.infinity_polling()
