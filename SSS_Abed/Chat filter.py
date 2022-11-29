
from email import message
import telebot
from telebot import types
from telebot.async_telebot import AsyncTeleBot
from datetime import datetime, timedelta, time
import asyncio
from apscheduler.schedulers.background import BackgroundScheduler
import json
import schedule
import math
import time
from telebot.types import ReplyKeyboardRemove




pollID = []
pollID.append(message)
pollID.append(message)
pollID.append(message)
#nonushta poll
breakfastPollTime = "14:00"
breakfastEndPollTime = "16:00"
breakfastTime = "02:30"
#abed poll
lunchPollTime = "02:00"
lunchEndPollTime = "04:00"
lunchTime = "07:30"
#tushlik poll
dinnerPollTime = "08:00"
dinnerEndPollTime = "10:00"
dinnerTime = "13:30"

risposte = ['Men', 'Men emas']
token="5484337646:AAHuupgWpbqT6_5CrOH27Vi9KSWMxkFyH6I"
active_chat_ids = ['-1001824498165'] # SS -392686344 test -851115866 #SSS oshpaz -1001824498165
admin_user_ids = ['Lorntz']
bot = telebot.TeleBot(token)
add = False

minuteInterval = 2
recentmassage = []
wfmessage = bot.send_message
breakfastEvent = bot.send_message
lanchEvent = bot.send_message
dinnerEvent = bot.send_message
risposte = ['Men', 'Men emas']
sysDate = datetime.now()



class  member_users:
    def __init__(self ,name, id, username, status):
        self.name = name
        self.id = id
        self.username = username
        self.status = status
    def isID(self, Id):
        if Id == self.id:
            return True

f = open('personal.json')
aData = json.loads(f.read())
f.close()
print("Json ma'lumotlar o'qildi")
a = []

for x in aData:
    a.append(member_users(x['name'],x['id'],x['username'],x['status']))

class dayLanchMember:
    def __init__(self, date, type, allowCount, deniedCount):
        self.date = date
        self.type = type
        self.allowcount = allowCount
        self.deiedcount = deniedCount
     




#a.append(member_users("Group",active_chat_ids[0],"Group_name","allow"))

@bot.message_handler(commands=['start', 'help'])
def start(message):
   
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Aktiv')
    item2 = types.KeyboardButton('Jimlik')
    item3 = types.KeyboardButton('Ovqat tayyor')
    item4 = types.KeyboardButton('So\'rov kechlik')
    item5 = types.KeyboardButton('So\'rov abed')
    item5 = types.KeyboardButton('So\'rov nonushta')
    if message.chat.username  in  admin_user_ids:
        markup.add(item1, item3, item4, item5)
    else:
        if message.chat.type == 'private':
            markup.add(item1, item2)
        else:
          markup = ReplyKeyboardRemove()

    bot.send_message(message.chat.id, 'Salom {0.first_name}!'.format(message.from_user), reply_markup = markup)
    print('{0.first_name}'.format(message.from_user))

@bot.message_handler(regexp="Aktiv")
def Yordam(message):
    if not any([team.id == message.chat.id for team in a]):
      a.append(member_users(message.chat.first_name,message.chat.id,message.chat.username,"allow"))

    for x in a:
        if x.id == message.chat.id and x.status == "denied":
            x.status = "allow"
    bot.send_message(message.chat.id, 'Javobingiz uchun rahmat. Sizni habardor qilib turamiz.')
    aJson = json.dumps([x.__dict__  for x in a])
    print(aJson)
    with open('personal.json', 'w') as json_file:
            json.dump([x.__dict__  for x in a], json_file)
            json_file.close()

  

    


@bot.message_handler(regexp="Jimlik")
def Yemayman(message):
    if not any([team.id == message.chat.id for team in a]):
      a.append(member_users(message.chat.first_name,message.chat.id,message.chat.username,"denied"))
   
    for x in a:
        if x.id == message.chat.id and x.status== "allow":
            x.status = "denied"
 
    bot.send_message(message.chat.id, 'Javobingiz uchun rahmat. Sizni bezovta qilmaymiz.')
    aJson = json.dumps([x.__dict__  for x in a])
    print(aJson)
    with open('personal.json', 'w') as json_file:
            json.dump([x.__dict__  for x in a], json_file)
            json_file.close()
        

from apscheduler.schedulers.background import BackgroundScheduler

def timeChecker():

    sysDate = datetime.now()
    if sysDate.minute == 24 and sysDate.hour ==1:
        
       # dinnerEndTimeInt = 
        GoToDinnerPoll(message)
        
        print (sysDate)

    if sysDate.minute == 57 and sysDate.hour == 22:
        for i in recentmassage:
            bot.delete_message(i.chat.id, i.id)
            recentmassage.pop(i.index)
            
def testTimer():
 
       GoToDinnerPoll(message)
       print (sysDate)

def runTrigger():
    schedule.run_pending()






    




@bot.message_handler(regexp="Ovqat tayyor")
def testMessage(message):
    GoToKitchen( "Test")


def GoToKitchen(  text):
    mess = text
    recentmassage =  bot.send_message(active_chat_ids[0], mess )
    for x in a:
        if x.status == "allow":
            bot.send_message(x.id, mess )
    

@bot.message_handler(regexp="So\'rov kechlik")
def GoToDinnerPoll(message):
   EndTime = sysDate.now()
   EndTime +=timedelta(hours=2)
   timeUNIX = math.trunc(EndTime.timestamp())
   wfmessage = bot.send_poll(active_chat_ids[0], 'Bugun kim kechki ovqatga qoladi ?', risposte, is_anonymous=False, allows_multiple_answers = False)
   recentmassage.append(wfmessage) 
   
   
   
   for x in a:
        if x.status == "allow":
          recentmassage.append(  bot.forward_message( x.id,  wfmessage.chat.id, wfmessage.id ))

   return wfmessage

          

@bot.message_handler(regexp="So\'rov abed")
def GoToLunchPoll(message):
   EndTime = sysDate.now()
   EndTime +=timedelta(hours=2)
   timeUNIX = math.trunc(EndTime.timestamp())
   wfmessage = bot.send_poll(active_chat_ids[0], 'Bugun kim abed qiladi ?', risposte, is_anonymous=False, allows_multiple_answers = False)
   recentmassage.append(wfmessage )
   for x in a:
        if x.status == "allow":
           recentmassage.append(bot.forward_message( x.id,  wfmessage.chat.id, wfmessage.id ))
   return wfmessage

@bot.message_handler(regexp="So\'rov nonushta")
def GoToBreakfestPoll(message):
   EndTime = sysDate.now()
   EndTime +=timedelta(hours=2)
   timeUNIX = math.trunc(EndTime.timestamp())
   wfmessage = bot.send_poll(active_chat_ids[0], 'Ertaga kim nonushta qiladi ?', risposte, is_anonymous=False, allows_multiple_answers = False )
   recentmassage.append (wfmessage)
   for x in a:
        if x.status == "allow":
           recentmassage.append(bot.forward_message( x.id,  wfmessage.chat.id, wfmessage.id ))  
   return wfmessage

@bot.poll_answer_handler()
def MenYeyman(message):
    print("Answer!")


def goToBPoll():
   global pollID
   pollID[0] =( GoToBreakfestPoll(message))


def goToLPoll():
   global pollID
   pollID[1] =( GoToLunchPoll(message))
    
   
    

def goToDPoll():
   
   global pollID
   pollID[2] =( GoToDinnerPoll(message))
    
    
def stopBPoll():
   global pollID
   bot.stop_poll(pollID[0].chat.id, pollID[0].id )


def stopLPoll():
   global pollID
   bot.stop_poll(pollID[1].chat.id, pollID[1].id )

def stopDPoll():
   global pollID
   bot.stop_poll(pollID[2].chat.id, pollID[2].id )

def GoToB():
    GoToKitchen( "Nunushta tayyor !")

def GoToL():
    GoToKitchen( "Tushlik tayyor !")

def GoToD():
    GoToKitchen("Kechlik tayyor !")

schedule.every().day.at(breakfastPollTime).do(goToBPoll)
schedule.every().day.at(lunchPollTime).do(goToLPoll)
schedule.every().day.at(dinnerPollTime).do(goToDPoll)
schedule.every().day.at(breakfastEndPollTime).do(stopBPoll)
schedule.every().day.at(lunchEndPollTime).do(stopLPoll)
schedule.every().day.at(dinnerEndPollTime).do(stopDPoll)
schedule.every().day.at(dinnerTime).do(GoToD)
schedule.every().day.at(breakfastTime).do(GoToB)
schedule.every().day.at(lunchTime).do(GoToL)

scheduler = BackgroundScheduler(timezone="Etc/GMT+5")
scheduler.add_job(runTrigger, trigger='interval', seconds=5)
scheduler.start()


print("Dastur ishga tushti ..... \n")
print("Sikl boshlandi ...\n")
bot.polling(non_stop=True)



