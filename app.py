from telegram.ext import MessageHandler, CommandHandler, filters, CallbackQueryHandler
from config.telegram_bot import application 
from handlers.message_handlers import chatgpt_reply 
from handlers.command_handlers import start_reply, explain_reply, mode_reply, joke_reply, mode
from handlers.audio_handlers import audio_reply

# Регистрация обработчика текстовых сообщений
message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, chatgpt_reply)
application.add_handler(message_handler)

# Регистрация обработчика аудио сообщений
audio_handler = MessageHandler(filters.VOICE, audio_reply)
application.add_handler(audio_handler)

# Регистрация обработчика команд
start_command_handler = CommandHandler("start", start_reply)
application.add_handler(start_command_handler)

explain_command_handler = CommandHandler("explain", explain_reply)
application.add_handler(explain_command_handler)

mode_command_handler = CommandHandler("mode", mode_reply)
application.add_handler(mode_command_handler)

mode_1_type_command_handler = CommandHandler("Intern", mode)
application.add_handler(mode_1_type_command_handler)
mode_2_type_command_handler = CommandHandler("DS", mode)
application.add_handler(mode_2_type_command_handler)
mode_3_type_command_handler = CommandHandler("DA", mode)
application.add_handler(mode_3_type_command_handler)
mode_4_type_command_handler = CommandHandler("Buddy", mode)
application.add_handler(mode_4_type_command_handler)

joke_command_handler = CommandHandler("joke", joke_reply)
application.add_handler(joke_command_handler)

# Запуск бота
application.run_polling()

