from flask import Flask
from threading import Thread
# server will run on a separate
# Thread from our our bot
# so as both can run at the
# same time

app = Flask('')


@app.route('/')
def home():
  return 'はい！僕はここ'

def run():
  app.run(host='0.0.0.0', port=8000)

def keep_alive():
  t = Thread(target=run)
  t.start()
