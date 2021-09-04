from telethon import TelegramClient, sync, events
from telethon.tl.functions.messages import (
    GetHistoryRequest,
    GetBotCallbackAnswerRequest,
)
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors import FloodWaitError
from time import sleep
import json, re, sys, os
import keyboard
from datetime import datetime
try:
    import webbrowser
    import requests
    from bs4 import BeautifulSoup
except:
    print(
        "\033[1;30m# \033[1;31mHmmm Sepertinya Modul Requests Dan Bs4 Belum Terinstall\n\033[1;30m# \033[1;31mTo install Please Type pip install requests and pip install bs4"
    )
    sys.exit



c = requests.session()

for i in range(5000000):
        sys.stdout.write("\r")
        sys.stdout.write("\x1b[1;33m▂▃▅▇█▓▒░SUB N lLike..!")
        sys.stdout.flush() 
        sleep(2)
        os.system("clear")
        break

    



banner = """Gaber"""

if not os.path.exists("session"):
    os.makedirs("session")

print(banner)
if len(sys.argv) < 2:
    print("\n\n\n\033[1;32mUsage : python main.py +62")
    sys.exit(1)

def OpenLink(link): 
        os.system("termux-open-url https://m.youtube.com/channel/UCbl-IZhURECrVWa4qF9GV5g#searching")

def tunggu(x):
    sys.stdout.write("\r")
    sys.stdout.write("                                                               ")
    for remaining in range(x, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write(
            "\x1b[1;30m{:2d} \x1b[1;32mseconds remaining".format(remaining)
        )
        sys.stdout.flush()
        sleep(1)


ua = {
    "User-Agent":"Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36"
}


api_id = 717425
api_hash = "322526d2c3350b1d3530de327cf08c07"
phone_number = sys.argv[1]

client = TelegramClient("session/" + phone_number, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    try:
        client.send_code_request(phone_number)
        me = client.sign_in(phone_number, input("\n\n\n\033[1;0mEnter Your Code : "))
    except SessionPasswordNeededError:
        passw = input("\033[1;0mYour 2fa Password : ")
        me = client.start(phone_number, passw)
myself = client.get_me()
os.system("clear")
print(banner)
print(
    "\x1b[1;32mWELCOME..\033[1;0m:",
    myself.first_name,
    "\n\x1b[1;0mBot Mining BCH Click Bot",
)


#password()
print("\n\n\033[1;37m▂▃▅▇█▓▒░۩۞۩ Start Mining......!")
try:
    channel_entity = client.get_entity("@BCH_clickbot")
    channel_username = "@BCH_clickbot"
    for i in range(5000000):
        sys.stdout.write("\r")
        sys.stdout.write(
            "                                                              "
        )
        sys.stdout.write("\r")
        sys.stdout.write("\x1b[1;32mMencoba Mengambil URL")
        sys.stdout.flush()
        client.send_message(entity=channel_entity, message="🖥 Visit sites")
        sleep(1)
        posts = client(
            GetHistoryRequest(
                peer=channel_entity,
                limit=1,
                offset_date=None,
                offset_id=0,
                max_id=0,
                min_id=0,
                add_offset=0,
                hash=0,
            )
        )
        if (
            posts.messages[0].message.find("Sorry, there are no new ads available")
            !=  -1
        ):
            try:
              print("\n\033[1;30m# \033[1;31mIklan Sudah Habis ..Next\n")
              client.send_message(entity=channel_entity, message="💰 Balance")
              sleep(2)
              posts = client(
                  GetHistoryRequest(
                      peer=channel_entity,
                      limit=1,
                      offset_date=None,
                      offset_id=0,
                      max_id=0,
                      min_id=0,
                      add_offset=0,
                      hash=0,
                  )
              )
              message = posts.messages[0].message
              now = datetime.now()

              current_time = now.strftime("%H:%M:%S")
              print("Current Time =", current_time)
              print(message ,current_time)
              print ("Bot is searching for mining chances ")
              #channel_entity = client.get_entity("@BCH_clickbot")
              #channel_username = "@BCH_clickbot"
              client.disconnect()
              tunggu (24)
              
              os.system ('cmd /k "py -m DOGE01133.py +201097409718" ' )
            except:
             pass
            else:
             pass
         
        else:
            try:
                url = posts.messages[0].reply_markup.rows[0].buttons[0].url
                sys.stdout.write("\r")
                sys.stdout.write("\033[1;32mVisit " + url)
                sys.stdout.flush()
             
                os.system("termux-open-url \""+url+"\"")

            
                id = posts.messages[0].id
                r = c.get(url, headers=ua, timeout=19, allow_redirects=True)
                soup = BeautifulSoup(r.content, "html.parser")
                if (
                    soup.find("div", id="headbar") is None
                ):
                    sleep(2)
                    posts = client(
                        GetHistoryRequest(
                            peer=channel_entity,
                            limit=1,
                            offset_date=None,
                            offset_id=0,
                            max_id=0,
                            min_id=0,
                            add_offset=0,
                            hash=0,
                        )
                    )
                    message = posts.messages[0].message
                    if (
                        posts.messages[0].message.find("You must stay") == -1
                        or posts.messages[0].message.find("Please stay on") == -1
                    ):
                        sec = re.findall (r"([\d.]*\d+)", message)
                        tunggu(16)
                        sleep(1)
                        posts = client(
                            GetHistoryRequest(
                                peer=channel_entity,
                                limit=2,
                                offset_date=None,
                                offset_id=0,
                                max_id=0,
                                min_id=0,
                                add_offset=0,
                                hash=0,
                            )
                        )
                        messageres = posts.messages[1].message
                        sleep(2)
                        #sys.stdout.flush()
                        #webbrowser.open_new( "bbbb" )
                        keyboard.press_and_release('ctrl+w') # closes the last tab
                        #keyboard.press_and_release('ctrl+w') # closes the last tab
                        sys.stdout.write("\r\033[1;30m# \033[1;32m" + messageres + "\n")
                    else:
                        pass

                elif soup.find("div", id="headbar") is not None:
                    for dat in soup.find_all("div", class_="container-fluid"):
                        code = dat.get("data-code")
                        timer = dat.get("data-timer")
                        print (timer)
                        tokena = dat.get("data-token")
                        tunggu(11)
                        r = c.post(
                            "https://dogeclick.com/reward",
                            data={"code": code, "token": tokena},
                            headers=ua,
                            timeout=15,
                            allow_redirects=True,
                        )
                        js = json.loads(r.text)
                        sys.stdout.write(
                            "\r\033[1;30m# \033[1;32m earnhhhhed  "
                            + js["reward"]
                            + " BCH !\n"
                        )
                else:
                    sys.stdout.write("\r")
                    sys.stdout.write(
                        "                                                                "
                    )
                    sys.stdout.write("\r")
                    sys.stdout.write("\033[1;30m# \033[1;31mCaptcha Detected")
                    sys.stdout.flush()
                    sleep(2)
                    client(
                        GetBotCallbackAnswerRequest(
                            channel_username,
                            id,
                            data=posts.messages[0].reply_markup.rows[1].buttons[1].data,
                        )
                    )
                    sys.stdout.write(
                        "\r\033[1;30m# \033[1;31mSkip Captcha...!       \n"
                    )
                    sleep(2)
            except:
                sleep(3)
                posts = client(
                    GetHistoryRequest(
                        peer=channel_entity,
                        limit=1,
                        offset_date=None,
                        offset_id=0,
                        max_id=0,
                        min_id=0,
                        add_offset=0,
                        hash=0,
                    )
                )
                message = posts.messages[0].message
                if (
                    posts.messages[0].message.find("You must stay") == -1
                    or posts.messages[0].message.find("Please stay on") == -1
                ):
                    sec = re.findall(r"([\d.]*\d+)", message)
                    tunggu(11)
                    sleep(1)
                    posts = client(
                        GetHistoryRequest(
                            peer=channel_entity,
                            limit=2,
                            offset_date=None,
                            offset_id=0,
                            max_id=0,
                            min_id=0,
                            add_offset=0,
                            hash=0,
                        )
                    )
                    messageres = posts.messages[1].message
                    sleep(2)
                    sys.stdout.write("\r\033[1;30m# \033[1;32m" + messageres + "\n")
                else:
                    pass

finally:
    client.disconnect()
