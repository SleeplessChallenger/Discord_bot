from random import choice
from Quotes_model import Quotes
import os
import discord
from trigger_bot import keep_alive
from NoSQL_model import dbClass


client = discord.Client()
db = dbClass.dbInit()


def get_quote(phrase):
  if phrase == 'random':
    quote = Quotes('random')
  elif phrase == 'today':
    quote = Quotes('today')

  return quote.obj
  
# on_ready and on_message are named like that
# as it's required by docs
@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('$quote'):
    quote = get_quote('random')
    await message.channel.send(quote)
  
  elif message.content.startswith('$todayQuote'):
    quote = get_quote('today')
    await message.channel.send(quote)
  
  if message.content.startswith('$del'):
    ebullient = []
    if len(db.words['ebullient']) < 1:
      await message.channel.send('No words to delete:(')
      raise IndexError('Blank list')
    if 'ebullient' in db.words:
      idx = int(message.content.split('$del', 1)[1])
      value = db.delete_ebullient(idx)
      ebullient = db.words['ebullient']
    await message.channel.send(f"All: {ebullient}, Deleted {value}")

  if db.respond:
    base = db.default_words['happy']
    baseTwo = db.default_words['grim']
    if 'ebullient' in db.words:
      # base = base + list(db['ebullient'])
      baseHappy = base + db.words['ebullient']

    if 'severe' in db.words:
      baseGrim = baseTwo + db.words['severe']
    if any(word in message.content for word in baseGrim):
      await message.channel.send(choice(baseHappy))
  
  if message.content.startswith('$new'):
    msg = message.content.split('$new ', 1)[1]
    db.update_ebullient(msg)
    await message.channel.send('New message was added!')
  
  if message.content.startswith('$all'):
    ebullient = []
    if 'ebullient' in db.words:
    # if 'ebullient' in db.keys():
    # if db used instead of class
      ebullient = db.words['ebullient']
    await message.channel.send(ebullient if len(ebullient) > 1 
                                         else ebullient[0])
  
  if message.content.startswith('$checkState'):
    await message.channel.send(db.respond)
  # below chunk will TURN ON/OFF
  # feature of responding to sad
  # words of the user with ebullient ones
  if message.content.startswith('$respond'):
    try:
      val = message.content.split('$respond ', 1)[1]
    except IndexError:
      await message.channel.send("Impossible to make an action "
                                   "without 'true' or some drop "
                                   "variable")
      raise IndexError('No value provided')
  
    else:
      if val.lower() == 'true':
        db.respond = True
        await message.channel.send('Responding is ON')
      else:
        db.respond = False
        await message.channel.send('Responding is OFF')


keep_alive()
client.run(os.getenv('TOKEN'))
