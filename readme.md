# Bot for Reminder a task every minute until someone select

This a bot for users, the user should write /start + task, after sending the message the bot send a message every minute until someone replies to the original message with /onit.

After that, the bot has a window of 10 minutes for the user to finish the task, or the bot will start sending a reminder to the user that sends the /onit messages. When the user completes the tasks, when the users finish the task must replies the original messages with /done 

# You need isntall the requirements.txt


## Structure of DB
id,
chat_id,message_id,
user_name_requested,
user_id_requested,
request_date,
user_id_procesed,
user_name_procesed,
date_procesed,date_done
