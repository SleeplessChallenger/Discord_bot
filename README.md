<h2>Discrod_bot</h2>

This is a bot that I initially made on https://replit.com/~ 
<br>

<h5>Caveat:</h5>
I used `replit` built in NoSQL db, hence if you want to use it,
be aware of it.

<h3>Description</h3>

<ul>
  It's a bot that will send encouraging messages to the user and grants
  user the option to add/remove words from its storage
  <br>
  
  <li>`main.py` is a file that comprises overall logic. Bot can react
      to certain commands to do various things like
   <ol>
     <li>give `quotes` from https://zenquotes.io </li>
      <li>allow user to add/remove words from DB </li>
      <li>responds to user if there is sad/depressed word in the phrase with ebullient one </li>
      <li>enables user to turn onn/off above mentioned feature </li>
      <li>make some other things </li>
  </ol>
 </li>
 
 <li>`NoSQL_model.py` is a file with class that keeps <i>happe and sad</i> phrases in stock
      and makes possible various manipulations like adding/removing
 </li>
 
 <li>`Quotes_model.py` is a file with class that makes possible for user to receive quotes
      from command line. Either by receiving **random quote** or **quote of the day**
 </li>
 
 <li>`trigger_bot.py` is a file that makes bot alive and not allow it to go into sleep.
      It is possible also due to https://uptimerobot.com
 </li>
</ul>

![Alt text](D_bot.png?raw=true)
                 
