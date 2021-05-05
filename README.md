<h2>Discrod_bot</h2>

This is a bot that I initially made on [Link to replit](https://replit.com/~)
<br>

<h5>Caveat:</h5>
I used `replit` built in NoSQL db, hence if you want to use my bot,
be aware of it.

<h3>Description</h3>

It's a bot that will send encouraging messages to the user and grants
user the option to add/remove words from its storage
<br>
  
1. `main.py` is a file that comprises overall logic. Bot can react
      to certain commands to do various things like: 
   
    - gives quotes from [Link to zenquotes](https://zenquotes.io)
    - allows user to add/remove words from DB
    - responds to user if there is sad/depressed word in the phrase with ebullient one
    - enables user to turn onn/off above mentioned feature
    - makes some other things
 
2. `NoSQL_model.py` is a file with class that keeps <i>happy and sad</i> phrases in stock
      and makes possible various manipulations like adding/removing
 
3. `Quotes_model.py` is a file with class that makes possible for user to receive quotes
      from command line. Either by receiving **random quote** or **quote of the day**
 
4. `trigger_bot.py` is a file that makes bot alive and not allow it to go into sleep.
      It is possible also due to [Link to uptimerobot](https://uptimerobot.com)


![Alt text](D_bot.png?raw=true)
                 
