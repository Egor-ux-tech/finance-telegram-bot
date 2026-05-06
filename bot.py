from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from main import load_data, add_expense
import os
#TOKEN = os.getenv("8501080390:AAEAx6plEL1MvhkE7jXtsAlQ0C8qDzMGD78")
TOKEN = "8501080390:AAEAx6plEL1MvhkE7jXtsAlQ0C8qDzMGD78"
print("TOKEN:", TOKEN)
file_name = "expenses.json"

keyboard = [
    ["Добавить расход"],
    ["Показать расходы"],
    ["Общая сумма расходов"]
]
markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет, я трекер расходов\n\n Выбери действие:",
        reply_markup=markup
    )
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "Добавить расход":
        await update.message.reply_text("Введи категорию и цену\n")

    elif text == "Показать расходы":
        data = load_data()
        if not data:
            await update.message.reply_text("Нет расходов")
            return 
        result = "Твои расходы:\n"
        for item in data:
            result += f"{item['category']} - {item['price']}\n"
        await update.message.reply_text(result)

    elif text == "Общая сумма расходов":
        data = load_data()
        total = sum(item["price"] for item in data)
        await update.message.reply_text(f"Общая сумма: {total}")
    
    else:
        try:
            parts = text.split()
            category = parts[0]
            price = float(parts[1])
        except:
            await update.message.reply_text("Ошибка. Введи категорию и цену")
            return
        data = load_data()
        add_expense(data, category, price)
        await update.message.reply_text("Расход добавлен")
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, handle_message))
app.run_polling()
print("TOKEN =", TOKEN)