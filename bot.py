from fbchat import  Client, log
import fbchat,sys
from fbchat.models import *
import fileinput
def send_massage(ide,massage):
    sent = client.send(fbchat.models.Message(massage),ide)
class punkjj(Client):
    def onMessage(self, author_id=None, message_object=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
        toggle = client.fetchThreadMessages(thread_id=client.uid, limit=1)
        msgText = message_object.text.lower()
        if(msgText=="hi" or msgText=="hii" or msgText=="hiii" or msgText=="yo" or msgText=="hi there" or msgText=="hey" or msgText=="heyy"):
            send_massage(thread_id,"Hello :D")
        elif(msgText=="hello" or msgText=="hellow" or msgText=="heloo" or msgText=="hlo" or msgText=="hellow"):
            send_massage(thread_id,"Hello :D")
        elif(msgText=="hy" or msgText=="hyy"):
            send_massage(thread_id,"Hello :D")
        elif msgText == 'how are you':send_massage(thread_id,"I am fine and you?:D")
        elif(msgText=="whatsup" or msgText=="wassup" or msgText=="what's up" or msgText=="wtsup" or msgText=="watsup" or msgText=="whats up" or "how are you" in msgText or "hw r u" in msgText):
            send_massage(thread_id,"Awesome. What about you? :D")
        elif(msgText=="test" or msgText=="debug" or msgText=="aboutme" or msgText=="about" or msgText=="bot"):
            send_massage(thread_id,"Hi, I'm a bot written in Python. Created by Pankaj Sheoran")
        elif("birthday" in msgText or "bday" in msgText or "hbd" in msgText):
            send_massage(thread_id,"Thank you! :D")
        elif("what you doing" in msgText):
            send_massage(thread_id,"Idling, I'm a bot afterall. I work for my creator")
        elif("bye" in msgText or msgText=="byye" or msgText=="byee"):
            send_massage(thread_id,"Ok bye! :D")
        else:
            send_massage(thread_id,"Thank you for contacting me. I'm currently not online, I was replying using a Python Script. I will reach out to you shortly.")
            sys.exit()
client = punkjj("Your gamil \ number", "password")
client.listen()
