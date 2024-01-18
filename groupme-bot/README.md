# GroupMe Bot

## Bot features

- Replies to anyone if good morning/ good night is texted in chat
- Bot will resond to only you with a random text about why it is busy and cant respond whenever you text
- Ignores messages from itself as well as other bots so it wont get stuck in a loop
- If you text "tell me about ____" the bot uses the news api to find recent articles related to youre search, it will provide a description as well as a url

## Set Up 

1. Please make sure that python3 as well as 'pip' is installed on youre machine
- python3 can be instaleld [Here](https://www.python.org/downloads/)
2. Set up your '.env' file based on your information. create a file called '.env' to hold your environment variables:
```bash BOT_ID = ...       # your GroupMe Bot ID
GROUP_ID = ...      # your GroupMe group ID where you want the bot to be
ACCESS_TOKEN = ...  # your GroupMe Developer acess token
sender_id= ...      # your personl group me sender ID
API_KEY = ...       # your API key for news api 
```
[Here](https://dev.groupme.com/bots) is where you can find the ID of your bot

## Run Bot
1. To run the bot use the command 'python3 bot.py' inside of the groupme-bot directory

enjoy
