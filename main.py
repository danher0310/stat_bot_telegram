import os
import environ
from telegram.ext import Updater, CommandHandler,MessageHandler, Filters
import logging
import backend as back




env = environ.Env()
environ.Env()
environ.Env.read_env()
ENVIROMENT = env
token = str(os.environ.get('TOKEN'))

def start(update, context):
    print(update)
    update.message.reply_text('Im here')

def stat(update, context):
    args = context.args
    if len(args) == 0:
        update.message.reply_text('Invalid command, you need to write the message after the command "/stat"')
    elif len(args) >= 1:
        
        chat  = update.message.chat.id
        message = update.message.message_id
        user_id = update.message.from_user.id
        user_name = update.message.from_user.first_name        
        insert= back.registerStat(chat, message, user_id, user_name)
        if insert != None:
            update.message.reply_text(insert)
        
    
def onit(update, context):
    if(update.message.reply_to_message):
        chat_id = update.message.chat_id
        reply_id = update.message.reply_to_message.message_id
        reply_user_id = update.message.from_user.id
        reply_user_name = update.message.from_user.first_name    
        updating = back.updateStatusStat(chat_id, reply_id, reply_user_id , reply_user_name)
        if updating != None:
            update.message.reply_text(updating)  


def done(update, context):
    if(update.message.reply_to_message):
        chat_id = update.message.chat_id
        reply_id = update.message.reply_to_message.message_id
        reply_user_id = update.message.from_user.id
        reply_user_name = update.message.from_user.first_name
        updating = back.doneStatusStat(chat_id, reply_id, reply_user_id , reply_user_name)
        if updating != None:
            update.message.reply_text(updating)

def checkStats(context):
    
    select = back.checkStats()
    
    if (select != None):
        for row in select:
            msg = "Hey team we have a STAT message without response from ["+row[1]+"](tg://user?id="+str(row[2])+")"
            context.bot.send_message(
                chat_id = row[0],
                text = msg, parse_mode="Markdown"
            )


def checkProcessStat(context):
    select = back.checkProcessedStats()
    if (select != None):
        for row in select:           
            if int(row[0])>=10:
                msg = "Hey ["+row[5]+"](tg://user?id="+str(row[4])+") you have a STAT message without process from ["+row[2]+"](tg://user?id="+str(row[3])+")"
                context.bot.send_message(
                    chat_id = row[1],
                    text = msg, parse_mode="Markdown"
                )
                
    



if __name__ == '__main__':
    updater = Updater(token=token, use_context = True)
    dispacher = updater.dispatcher 
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    # Command Handler
    dispacher.add_handler(CommandHandler('start', start))
    dispacher.add_handler(CommandHandler('stat', stat))
    dispacher.add_handler(CommandHandler('onit', onit))
    dispacher.add_handler(CommandHandler('done', done))
    dispacher.add_handler(CommandHandler('test', done))

    # Job queue
    jobStat = updater.job_queue
    jobStat.set_dispatcher(dispacher)
    jobStat.run_repeating(callback=checkStats, interval=60)    
    jobProcessStat = updater.job_queue
    jobProcessStat.set_dispatcher(dispacher)
    jobProcessStat.run_repeating(callback=checkProcessStat, interval=60)

    #started
    jobStat.start()
    jobProcessStat.start()
    updater.start_polling()
    print("---Bot Started---")
    updater.idle()




    
# {'message': {
#     'date': 1668448231, 
#     'entities': [
#         {'length': 5, 
#         'offset': 0, 
#         'type': 'bot_command'}
#         ], 
#     'chat': {
#         'type': 'group', 
#         'all_members_are_administrators': True, 
#         'id': -718891298, 
#         'title': 'test-sender'
#         }, 
#         'caption_entities': [], 
#         'channel_chat_created': False, 
#         'photo': [], 
#         'text': '/onit', 
#         'supergroup_chat_created': False,
#         'new_chat_members': [], 
#         'new_chat_photo': [], 
#         'message_id': 51, 
#         'group_chat_created': False, 
#         'delete_chat_photo': False, 
#         'reply_to_message': {
#             'date': 1668447727, 
#             'entities': [
#                 {'length': 5, 
#                 'offset': 0, 
#                 'type': 'bot_command'}
#                 ], 
#                 'chat': {
#                     'type': 'group', 
#                     'all_members_are_administrators': True, 
#                     'id': -718891298, 
#                     'title': 'test-sender'
#                     }, 
#                     'caption_entities': [], 
#                     'channel_chat_created': False, 
#                     'photo': [], 
#                     'text': '/stat probando funciones', 
#                     'supergroup_chat_created': False, 
#                     'new_chat_members': [], 
#                     'new_chat_photo': [], 
#                     'message_id': 50, 
#                     'group_chat_created': False, 
#                     'delete_chat_photo': False, 
#                     'from': {
#                         'last_name': 'Herrera', 
#                         'username': 'Danielherrerar', 
#                         'id': 593221542, 
#                         'is_bot': False, 
#                         'first_name': 'Daniel', 
#                         'language_code': 'es'
#                         }
#                         }, 
#     'from': {
#         'last_name': 'Herrera', 
#         'username': 'Danielherrerar', 
#         'id': 593221542, 'is_bot': False, 
#         'first_name': 'Daniel', 
#         'language_code': 'es'
#         }
#         }, 
#         'update_id': 85290505}