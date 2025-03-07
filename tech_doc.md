# Техническая документация телеграмм бота AISID 2025

## 1. Введение

### 1.1 Назначение

AISID 2025 Telegram Bot – это бот для Telegram, предназначенный для предоставления информации о разработчиках, технической документации и презентации проекта.

### 1.2 Основные функции

- 📌 Отправка списка разработчиков
- 📄 Отправка ссылки и файла с технической документацией
- 🎥 Отправка ссылки и файла с презентацией проекта
- 🔙 Кнопка "Главное меню" для удобной навигации

---

## 2. Технические требования

### 2.1 Среда выполнения

- Python 3.8+
- `aiogram` для работы с Telegram API
- Файлы документации и презентации в формате PDF/MD

### 2.2 Зависимости

Перед запуском установите все необходимые библиотеки:

```bash
pip install aiogram
```

---

## 3. Архитектура проекта

### 3.1 Общая схема взаимодействия

1. Пользователь отправляет команду или нажимает кнопку в боте.
2. Бот принимает сообщение через Telegram API.
3. Обработчик `aiogram` анализирует сообщение.
4. В зависимости от команды бот отправляет нужную информацию.

### 3.2 Используемые технологии

- **Python 3.8+** – основной язык программирования
- **Aiogram** – асинхронная библиотека для работы с Telegram API
- **SQLite/PostgreSQL** (при необходимости) – база данных для хранения информации

---

## 4. Установка и запуск

### 4.1 Получение API-токена

1. Написать [@BotFather](https://t.me/BotFather) в Telegram.
2. Создать нового бота и получить `TOKEN`.
3. Вставить `TOKEN` в код.

### 4.2 Запуск бота

```bash
python bot.py
```

---

## 5. Структура проекта

```
/aisid2025_bot
│── bot.py                # Код Telegram-бота
│── tech_doc.md           # Техническая документация в MD
│── aisid2025_presentation.pdf # Презентация проекта в PDF
│── README.md             # Документация проекта
│── requirements.txt      # Список зависимостей
│── Procfile              # Файл для деплоя на Heroku
```

---

## 6. Логика работы бота

### 6.1 Описание команд

Бот использует библиотеку `aiogram`. При запуске `/start` отправляется клавиатура с тремя кнопками:

- 🛠 **"Разработчики"** – выводит список разработчиков
- 📄 **"Техническая документация"** – отправляет ссылку и MD-файл
- 🎥 **"Презентация проекта"** – отправляет ссылку и PDF-файл
- 🔙 **"Главное меню"** – возвращает пользователя к основному меню

### 6.2 Описание работы обработчиков

| Команда/Кнопка             | Действие                                                           |
| -------------------------- | ------------------------------------------------------------------ |
| /start                     | Отправляет клавиатуру с кнопками                                   |
| "Разработчики"             | Выводит список разработчиков                                       |
| "Техническая документация" | Показывает меню с возможностью открыть ссылку или скачать MD-файл  |
| "Презентация проекта"      | Показывает меню с возможностью открыть ссылку или скачать PDF-файл |
| "Главное меню"             | Возвращает пользователя к основному меню                           |

---

## 7. Принцип работы

1. **Главное меню**
   - Пользователь вводит `/start`.
   - Бот отправляет клавиатуру с основными кнопками.
2. **Разработчики**
   - Пользователь нажимает кнопку "Разработчики".
   - Бот отправляет список разработчиков с кнопкой "🔙 Главное меню".
3. **Техническая документация**
   - Пользователь нажимает кнопку "Техническая документация".
   - Бот отправляет клавиатуру с кнопками "🌐 Открыть документацию", "📄 Скачать документацию" и "🔙 Главное меню".
   - При выборе "Скачать документацию" бот отправляет MD-файл.
4. **Презентация проекта**
   - Пользователь нажимает кнопку "Презентация проекта".
   - Бот отправляет клавиатуру с кнопками "🌐 Открыть презентацию", "📥 Скачать презентацию" и "🔙 Главное меню".
   - При выборе "Скачать презентацию" бот отправляет PDF-файл.
5. **Возвращение в главное меню**
   - В каждом разделе есть кнопка "🔙 Главное меню", которая возвращает пользователя в начальное меню.

---

## 8. Код программы

```python
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
import logging

TOKEN = "NULL"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

def main_menu():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("Разработчики", callback_data="developers"),
        InlineKeyboardButton("Техническая документация", callback_data="docs"),
        InlineKeyboardButton("Презентация проекта", callback_data="presentation")
    )
    return keyboard

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Выберите действие:", reply_markup=main_menu())

@dp.callback_query_handler(lambda call: call.data == "developers")
async def send_developers(call: types.CallbackQuery):
    developers = "👨‍💻 Проект разрабатывали:\n1. Айтбаев Жеңіс Жұмабайұлы\n2. Сундет Сумая Байжанқызы"
    keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton("🔙 Главное меню", callback_data="back"))
    await call.message.edit_text(developers, reply_markup=keyboard)

@dp.callback_query_handler(lambda call: call.data == "docs")
async def send_docs_menu(call: types.CallbackQuery):
    doc_link = "https://github.com/nimble365/aisid2025_bot/blob/main/tech_doc.md"
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("🌐 Открыть документацию", url=doc_link),
        InlineKeyboardButton("📄 Скачать документацию", callback_data="download_docs"),
        InlineKeyboardButton("🔙 Главное меню", callback_data="back")
    )
    await call.message.edit_text("📑 Выберите действие:", reply_markup=keyboard)

@dp.callback_query_handler(lambda call: call.data == "download_docs")
async def send_docs_file(call: types.CallbackQuery):
    with open("tech_doc.md", "rb") as file:
        await call.message.answer_document(file, caption="📄 Техническая документация")
    await call.message.answer("Выберите действие:", reply_markup=main_menu())

@dp.callback_query_handler(lambda call: call.data == "presentation")
async def send_presentation_menu(call: types.CallbackQuery):
    presentation_link = "https://github.com/nimble365/aisid2025_bot/blob/main/aisid2025_presentation.pdf"
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("🌐 Открыть презентацию", url=presentation_link),
        InlineKeyboardButton("📥 Скачать презентацию", callback_data="download_presentation"),
        InlineKeyboardButton("🔙 Главное меню", callback_data="back")
    )
    await call.message.edit_text("🎞 Выберите действие:", reply_markup=keyboard)

@dp.callback_query_handler(lambda call: call.data == "download_presentation")
async def send_presentation_file(call: types.CallbackQuery):
    with open("aisid2025_presentation.pdf", "rb") as file:
        await call.message.answer_document(file, caption="📥 Презентация проекта")
    await call.message.answer("🔙 Вернуться в главное меню:", reply_markup=main_menu())

@dp.callback_query_handler(lambda call: call.data == "back")
async def go_back(call: types.CallbackQuery):
    await call.message.edit_text("Выберите действие:", reply_markup=main_menu())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
```
