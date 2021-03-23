from logging import Handler, LogRecord

import telegram


class TelegramBotHandler(Handler):
    def __init__(self, token: str, chat_id: str):
        super().__init__()
        self.token = token
        self.chat_id = chat_id

    def emit(self, record: LogRecord):
        bot = telegram.Bot(self.token)
        bot.send_message(
            chat_id=self.chat_id,
            text=self.format(record)
        )
