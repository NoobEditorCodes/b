class script(object):
    CMD_LIST = """ðð¢ {},
â¢ /id - get id of a specifed user. 
â¢ /info  - get information about a user. 
â¢ /imdb  - get the film information from IMDb source. 
â¢ /search  - get the film information from various sources. 
â¢ /whois :-give a user full details 

 á´ÊÉªs Éªs Òá´Ê á´á´á´ÉªÉ´s 

â¢ /logs - to get the rescent errors 
â¢ /stats - to get status of files in db. 
â¢ /delete - to delete a specific file from db. 
â¢ /users - to get list of my users and ids. 
â¢ /chats - to get list of the my chats and ids 
â¢ /leave  - to leave from a chat. 
â¢ /disable  -  do disable a chat. 
â¢ /ban  - to ban a user. 
â¢ /unban  - to unban a user. 
â¢ /channel - to get list of total connected channels 
â¢ /broadcast - to broadcast a message to all users. 
â¢ /connect  - connect a particular chat to your PM. 
â¢ /disconnect  - disconnect from a chat. 
â¢ /connections - list all your connections. 
â¢ /pin :- Pin The Message You Replied To Message To Send A Notification To Group Members. 
â¢ /unpin :- Unpin The Current Pinned Message. If Used As A Reply, Unpins The Replied To Message. 
â¢ /filter - add a filter in chat. 
â¢ /filters - list all the filters of a chat. 
â¢ /del - delete a specific filter in chat. 
â¢ /delall - delete the whole filters in a chat (chat owner only)"""

    HELP_TXT = """ð·ð´ð {}
ð·ð´ðð´ ð¸ð ðð·ð´ ð·ð´ð»ð¿ ðµð¾ð ð¼ð ð²ð¾ð¼ð¼ð°ð½ð³ð."""

    BOT_TXT = """ðð¢ {},
âª How To Use This Bot

/update - To Join Our Main Channel, You can use this ð"""
    UPDATE_CMD = """ðð¢ {}, 
âª To Working of This Bot, Join the Main Channel Below 

âª Joining Because of Updates of Bots and All Others are through Main Channel

âª It is because of Copyright Issue is Very Low Compairing to Other Channels ð"""
    START_TXT = """Há´Ê {},
MÊ É´á´á´á´ Éªê± <a href=https://t.me/{}>{}</a>, I á´á´ á´á´sá´ á´É´ á´á´á´ á´É´á´á´á´ Aá´á´á´ÒÉªÊá´á´Ê Bá´á´ WÉªá´Ê á´xá´Êá´ á´á´á´á´ÊÉªÊÉªá´Éªá´s.Aá´á´ á´á´ á´á´ Êá´á´Ê É¢Êá´á´á´ á´s á´á´á´ÉªÉ´ á´É´á´ I'ÊÊ á´Êá´á´ Éªá´á´ á´á´á´ Éªá´s á´Êá´Êá´ ð

âª /bot - You can use this Command, how it is Working ð"""
    SOURCE_TXT = """<b>NOTE:</b>
- This is an open source project. 

<b>âââ ðð°ðªð¯ â ðð©ð¢ð³ð¦ â ðð¶ð±ð±ð°ð³ðµ âââ
â»ï¸ á´á´ÉªÉ´ :- <a href=https://t.me/+7AyTKA_SqdsyNWNl><b>âï¸ Backup Channel âï¸</b></a>
â»ï¸ á´á´ÉªÉ´ :- <a href=https://t.me/KC_Films><b>ð° Main Group ð°</b></a>
â»ï¸ á´á´ÉªÉ´ :- <a href=https://t.me/KC_Filmz><b>ð§² Backup Group ð§²</b></a>
âââ ðð°ðªð¯ â ðð©ð¢ð³ð¦ â ðð¶ð±ð±ð°ð³ðµ âââ</b>

<b>ð Team â <a href=https://t.me/KCFilmss>ð« KC Filmss ð«</a>\nâ¯ âââââ â§ âââââ â¯</b>\n"""

    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. KC Eva Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
â¢ /filter - <code>add a filter in chat</code>
â¢ /filters - <code>list all the filters of a chat</code>
â¢ /del - <code>delete a specific filter in chat</code>
â¢ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""

    BUTTON_TXT = """Help: <b>Buttons</b>

- This Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. KC Eva Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/KCFilmss)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
â¢ /connect  - <code>connect a particular chat to your PM</code>
â¢ /disconnect  - <code>disconnect from a chat</code>
â¢ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features

<b>Commands and Usage:</b>
â¢ /id - <code>get id of a specified user.</code>
â¢ /info  - <code>get information about a user.</code>
â¢ /imdb  - <code>get the film information from IMDb source.</code>
â¢ /search  - <code>get the film information from various sources.</code>"""

    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
â¢ /logs - <code>to get the rescent errors</code>
â¢ /stats - <code>to get status of files in db.</code>
â¢ /delete - <code>to delete a specific file from db.</code>
â¢ /users - <code>to get list of my users and ids.</code>
â¢ /chats - <code>to get list of the my chats and ids </code>
â¢ /leave  - <code>to leave from a chat.</code>
â¢ /disable  -  <code>do disable a chat.</code>
â¢ /ban  - <code>to ban a user.</code>
â¢ /unban  - <code>to unban a user.</code>
â¢ /channel - <code>to get list of total connected channels</code>
â¢ /broadcast - <code>to broadcast a message to all users</code>"""

    ABOUT_TXT = """âº ðð² ððð¦ð: {}
âº ðð¢ðð«ðð«ð²: Pyrogram
âº ððð­ðððð¬ð: MongoDB
âº ððð«ð¯ðð«: Heroku"""

    STATUS_TXT = """ð ÒÉªÊá´s sá´á´ á´á´: <code>{}</code>
ð¤ á´sá´Ês: <code>{}</code>
ð¥ É¢Êá´á´á´s: <code>{}</code>
ðï¸ á´á´á´á´á´Éªá´á´: <code>{}</code> """
 
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
 
