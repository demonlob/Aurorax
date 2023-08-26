HELP_1 = """ **<u>Admin commands:</u>**

Just added **c** in the starting of the commands to use them for channel.

/pause : Pause the current playing stream.

/resume : Resume the paused stream.

/skip : Skip the current  playing stream and start streaming the next track in queue.

/end ᴏʀ /stop : Clears the queue and end the current playing stream.

/player : Get an interactive player panel.

/queue : Shows the queued tracks list."""

HELP_2 = """ **<u>Auth users :</u>**
Auth users can use admin rights in the bot without admin rights in the chat. [Only admins]

/auth [Username] : Add a user to auth list of the bot.

/unauth [Username] : Remove a auth users from the auth users list.

/authusers : Shows the auth users list of the group."""

HELP_3 = """<b>Blacklist feature</b> [Only sudoes]
 **<u>Blacklist chat :</u>**

/blacklistchat [chat id] : Blacklist a chat from using the bot.

/whitelistchat [chat id] : Whitelist the blacklisted chat.

/blacklistedchat : Shows the list of blacklisted chats.


 **<u>Block users:</u>**

/block  : Block a  user,  [ Username or replay to user ].

/unblock  : Unblock the blocked user.[username or replay to user]

/blockedusers : Shows the list of blocked users."""

HELP_4 = """ **<u>Broadcast feature</u>** [Sudoes only] :

/broadcast  : Broadcast a message to served chats of the bot.

<u>Broadcasting modes:</u>
**-pin** : pins your broadcast message in served chats.
**-pinloud** : pins for broadcasted message in served chats and send notifications to the members.
**-user** : Broadcasts the message to the users who have started your bot.
**-assistant** : Broadcast your message from the assistant accounts of the bot.
**-nobot** : Forces the bot to not broadcast the message..

**Examble:** `/broadcast -user -assistant -pin Testing broadcast`
"""
HELP_5 = """ **<u>Extras :</u>**

/loop [Disable/Enable] ᴏʀ [between 1:10] 
: When activated bot will play the current playing stream in loop for 10 times or the number of requested loops.

/shuffle : Shuffle the queued tracks.

/seek : Seek the stream to the given duration.

/seekback : Backward seek the stream to the given duration.

/lyrics [Song name] : Search lyrics for the requested song and send the results."""

HELP_6 = """ **<u>Server playlists :</u>**

/playlist : Check your saved playlist on servers.

/deleteplaylist : Delete any saved tracks in your playlist.

/play : Starts playing from your saved playlist on server."""

HELP_7 = """ **Ping command :**

/ping : Show the ping and system stats of the bot.

/stats : Get 10 track global stats, Top 10 users of the bot, Top 10 Chats on the bot, Top 10 Played in the chat and many more..."""

HELP_8 = """ **<u>Play commands:</u>**

**c** Stands fir channel play.
**v** Stands for video play.
**force** Stands for force play.

/play or /vplay or /cplay : Starts streaming the requested track on videochat.

/playforce or /vplayforce or /cplayforce : **Force play** stops the ongoing stream and starts streaming the requested track.

/channelplay [Chat user or id] or [disable] : connect channel to a group and starts streaming tracks by the help of commands sent in group."""

HELP_9 = """**<u>Sudoers and owner commands :</u>**

 **<u>Add & remove sudoers :</u>**

/addsudo [Username or replay to a user]
/delsudo [Username or replay to a user.]

 **<u>Heroku :</u>**

/usage : shows the dyno usage of the month.

 **<u>Config variables:</u>**

/get_var : get a config var from heroku or env.
/del_var : delete a config var on heroku or env.
/set_var [var name] [value] : set or update a config var on heroku or env.

 **<u>Bot commands:</u>**

/restart : Restarts your bot.

/update : updates the bot from the upstream repo.

/speedtest : check bots server .

/maintenance [enable/disable] : enable or disable maintanace mode of your bot.

/logger [enable/disable] : Bot will start logging the activities happen on bot.

/get_log [number of lines] : get logs of your bot [default value  100 lines]

 **<u>For private bot only :</u>**

/authorize [chat id] : Allows a chat for using the bot.
/unauthorize [chat id] : Disallows the allowed chat.
/authorized : shows the list of allowed chats."""

HELP_10 = """ **<u>Active voicechats :</u>**

/activevoice : shows the list of active voicechats on the bot.
/activevideo : shows the list of active videochats on bot.
/autoend [Enable|Disable] : enable stream auto end if no one is listerning."""

HELP_11 = """**<u>Get started with bot</u>**
/start : Starts the music bot.

/help : Get help menu with explanation of commands.

/reboot : Reboots the bot for your chat.

/settings : shows the group settings with an interactive inline menu.

/sudolist : shows the sudo users of music bot."""

HELP_12 = """**<u>Gban feature</u>** [Sudoes only] :

/gban [Username or replay to a user ] : Globally bans the user from all the served chats and blacklist him for using the bot.

/ungban [Username or user id ] : Globally unbans the banned user.

/gbannedusers : Shows list of globally banned users."""
