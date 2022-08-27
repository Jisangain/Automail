from telegram.ext import Updater


def send(filename):
    updater = Updater("5100946328:AAGB7wKNXFf2ROLNWwo2F9-maQ6SDgkZRbw", use_context=True)
    updater.bot.send_document("847547511,", open(filename, 'rb'))
