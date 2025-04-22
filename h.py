import requests
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Telegram bot token
TOKEN = '7365934709:AAGdw4hGwbKSExQopyLnprleV2GCBE-LrEw'
# OMDb API endpoint and key (free public key)
OMDB_API_URL = 'http://www.omdbapi.com/'
OMDB_API_KEY = 'thewdb'  # You can get your own free key from http://www.omdbapi.com/apikey.aspx

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Send me a movie name or series and I will fetch its poster(s) for you!')

def get_movie_posters(query):
    # First, search for all movies matching the query
    params = {
        's': query,
        'apikey': OMDB_API_KEY
    }
    response = requests.get(OMDB_API_URL, params=params)
    data = response.json()
    posters = []
    if data.get('Response') == 'True' and data.get('Search'):
        for movie in data['Search']:
            poster_url = movie.get('Poster')
            title = movie.get('Title')
            year = movie.get('Year')
            if poster_url and poster_url != 'N/A':
                posters.append((poster_url, f"{title} ({year})"))
    return posters

def handle_message(update: Update, context: CallbackContext):
    query = update.message.text
    posters = get_movie_posters(query)
    if posters:
        for poster_url, caption in posters:
            update.message.reply_photo(poster_url, caption=caption)
    else:
        update.message.reply_text(f"Sorry, I couldn't find any posters for '{query}'.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
