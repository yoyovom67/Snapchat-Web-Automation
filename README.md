# Snapchat-Web-Automation

A small program to automate Snapchat on browser thanks to selenium and undetected chromedriver

## First connexion
```py
from main import SnapchatBot
if __name__ == "__main__":
    bot = SnapchatBot(first_connection=True)
```
> Note: You must then manually enter your credentials and accept on the mobile application. As long as you don't log out, you won't have to do this again.

## Send a message
```py
bot = SnapchatBot()
bot.send_message("message","target",group= True or False)
```
> Note: ⚠ You have to precise if the target is a group or not 

## get group members 
```py
bot.get_group_members("group_name")
```

## get friends  and list
```py
print(bot.get_friends_list())
print(bot.get_groups_list())
```

N.B.: please note that I am a beginner and that my code is not always written "cleanly". So please be indulgent.
