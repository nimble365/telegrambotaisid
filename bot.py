import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputFile

TOKEN = "8069908154:AAHZUeNvEwxVaVLFa4zwn6TocRa7i0cySfo"
bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

def main_menu():
    keyboard = InlineKeyboardMarkup()
    keyboard.row(InlineKeyboardButton("Разработчики", callback_data="developers"))
    keyboard.row(InlineKeyboardButton("Техническая документация", callback_data="docs"))
    keyboard.row(InlineKeyboardButton("Презентация проекта", callback_data="presentation"))
    return keyboard

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=main_menu())

@bot.callback_query_handler(func=lambda call: call.data == "developers")
def send_developers(call: CallbackQuery):
    developers = "👨‍💻 Проект разрабатывали:\n1. <b>Айтбаев Жеңіс Жұмабайұлы</b>\n2. <b>Сундет Сумая Байжанқызы</b>"
    keyboard = InlineKeyboardMarkup().row(InlineKeyboardButton("🔙 Главное меню", callback_data="back"))
    bot.edit_message_text(developers, call.message.chat.id, call.message.message_id, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == "docs")
def send_docs_menu(call: CallbackQuery):
    doc_link = "https://github.com/nimble365/aisid2025_bot/blob/main/tech_doc.md"
    keyboard = InlineKeyboardMarkup()
    keyboard.row(InlineKeyboardButton("🌐 Открыть документацию", url=doc_link))
    keyboard.row(InlineKeyboardButton("📄 Скачать документацию", callback_data="download_docs"))
    keyboard.row(InlineKeyboardButton("🔙 Главное меню", callback_data="back"))
    bot.edit_message_text("📑 Выберите действие:", call.message.chat.id, call.message.message_id, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == "download_docs")
def send_docs_file(call: CallbackQuery):
    bot.send_document(call.message.chat.id, InputFile("tech_doc.md"), caption="📄 Техническая документация")
    bot.send_message(call.message.chat.id, "Выберите действие:", reply_markup=main_menu())

@bot.callback_query_handler(func=lambda call: call.data == "presentation")
def send_presentation_menu(call: CallbackQuery):
    presentation_link = "https://github.com/nimble365/aisid2025_bot/blob/main/aisid2025_presentation.pdf"
    keyboard = InlineKeyboardMarkup()
    keyboard.row(InlineKeyboardButton("🌐 Открыть презентацию", url=presentation_link))
    keyboard.row(InlineKeyboardButton("📥 Скачать презентацию", callback_data="download_presentation"))
    keyboard.row(InlineKeyboardButton("🔙 Главное меню", callback_data="back"))
    bot.edit_message_text("🎞 Выберите действие:", call.message.chat.id, call.message.message_id, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == "download_presentation")
def send_presentation_file(call: CallbackQuery):
    bot.send_document(call.message.chat.id, InputFile("aisid2025_presentation.pdf"), caption="📥 Презентация проекта")
    bot.send_message(call.message.chat.id, "🔙 Вернуться в главное меню:", reply_markup=main_menu())

@bot.callback_query_handler(func=lambda call: call.data == "back")
def go_back(call: CallbackQuery):
    bot.edit_message_text("Выберите действие:", call.message.chat.id, call.message.message_id, reply_markup=main_menu())

if __name__ == "__main__":
    bot.polling(none_stop=True)