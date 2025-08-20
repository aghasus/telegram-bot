from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Substitua pelo token que o BotFather deu
TOKEN = "8498269643:AAFvVJHluwwWrYdmf27mb1pVfc3tjsloWss"

async def start(update, context):
    await update.message.reply_text("👋 Olá! Eu sou um bot hospedado no Render.")

async def echo(update, context):
    text = update.message.text.lower()
    if text == "oi":
        await update.message.reply_text("Oi! Tudo bem?")
    elif text == "menu":
        await update.message.reply_text("📌 Opções:\n1 - Ajuda\n2 - Informações\n3 - Sair")
    else:
        await update.message.reply_text("Não entendi 🤔")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    app.run_polling()

if __name__ == '__main__':
    main()