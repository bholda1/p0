from urllib import response
import requests
import time
import json
import os
import random
from dotenv import load_dotenv


load_dotenv()

BOT_ID = os.getenv("BOT_ID")
GROUP_ID = os.getenv("GROUP_ID")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
LAST_MESSAGE_ID = None


def send_message(text, attachments=None):
    """Send a message to the group using the bot."""
    post_url = "https://api.groupme.com/v3/bots/post"
    data = {"bot_id": BOT_ID, "text": text, "attachments": attachments or []}
    response = requests.post(post_url, json=data)
    return response.status_code == 202


def get_group_messages(since_id=None):
    """Retrieve recent messages from the group."""
    params = {"token": ACCESS_TOKEN}
    if since_id:
        params["since_id"] = since_id

    get_url = f"https://api.groupme.com/v3/groups/{GROUP_ID}/messages"
    response = requests.get(get_url, params=params)
    if response.status_code == 200:
        # this shows how to use the .get() method to get specifically the messages but there is more you can do (hint: sample.json)
        return response.json().get("response", {}).get("messages", [])
    return []


def process_message(message):
    """Process and respond to a message."""
    global LAST_MESSAGE_ID
    text = message["text"].lower()
    sender_id = message["sender_id"]
    sender_name = message["name"]
    sender_type = message["sender_type"]
    texts = [
    "Sorry, I'm currently in a meeting with my sofa, " + sender_name + ". Priorities!",
    "Can't chat, " + sender_name + ", I'm on a treasure hunt in my backyard.",
    "Hey " + sender_name + ", I'm busy arguing with my shadow. It's winning.",
    "I'd love to talk, but I'm currently teaching my fish to whistle, " + sender_name + ".",
    "Hold that thought, " + sender_name + ", I’m trying to figure out why my phone won’t cook dinner.",
    "Shh, " + sender_name + ", I’m undercover right now. The plants almost believe I’m one of them.",
    "Hey " + sender_name + ", can't talk. I'm busy converting oxygen into carbon dioxide.",
    "Sorry, " + sender_name + ", I'm at a whispering contest. What? I can't hear you!",
    "I'm currently learning how to yodel, " + sender_name + ". Yodel-ay-hee-hoo!",
    "Right now, " + sender_name + ", I'm in a serious relationship with my bed. It's complicated.",
    "Sorry, " + sender_name + ", I'm building a fort out of couch cushions.",
    "I'm practicing my ninja skills, " + sender_name + ". You can't see me right now.",
    "Can't talk, " + sender_name + ". I'm busy being an adult. (Just kidding, I'm playing in the mud.)",
    "I'm on a quest to touch the end of the rainbow, " + sender_name + ". BRB.",
    "In a staring contest with my reflection, " + sender_name + ". It's pretty intense.",
    "Sorry, " + sender_name + ", I'm currently in a dance-off with my toaster.",
    "Can't respond, " + sender_name + ", I'm trying to see if I can hear the light.",
    "I'm at the Olympics, " + sender_name + ". Of napping. Going for gold!",
    "Shh, " + sender_name + ", I'm eavesdropping on my plants. They're plotting something.",
    "Hey " + sender_name + ", can't talk. I'm waiting to see if my fridge light actually turns off.",
    "I'm busy trying to climb a horizontal ladder, " + sender_name + ". It's tough.",
    "Hey " + sender_name + ", I'm currently in a thumb war with myself. It's a tie.",
    "I'd answer, but I'm busy searching for the ‘any’ key, " + sender_name + ".",
    "In a serious discussion with my dog about politics, " + sender_name + ". Furry interesting.",
    "Sorry, " + sender_name + ", I'm trying to solve the mystery of why socks disappear in the dryer.",
    "Can't talk, " + sender_name + ", I'm training to be a superhero. Just need to find my cape.",
    "Hey " + sender_name + ", I'm busy looking for Waldo. Have you seen him?",
    "I'm currently having a tea party with my imaginary friend, " + sender_name + ".",
    "Sorry, " + sender_name + ", I'm trying to count all the stars in the sky. Lost count again...",
    "I'm in a deep philosophical debate with Siri, " + sender_name + ". It's getting heated.",
    "Hey " + sender_name + ", I can't talk. I'm chasing rainbows. Literally.",
    "I'm busy trying to figure out how to get square balloons, " + sender_name + ".",
    "Sorry, " + sender_name + ", I'm in a cookie-eating contest with myself. I'm winning.",
    "Hey " + sender_name + ", I'm currently trying to figure out how to walk through walls.",
    "I'm busy making a sandwich, " + sender_name + ". It’s a piece of art.",
    "Can't chat, " + sender_name + ", I'm trying to teach my cat to bark.",
    "In the middle of a marathon, " + sender_name + ". A TV show marathon, that is.",
    "I'm trying to break the world record for blinking, " + sender_name + ". Almost there!",
    "Hey " + sender_name + ", I'm currently trying to decipher my handwriting. It's ancient script.",
    "Sorry, " + sender_name + ", I'm stuck in an epic battle with a spider. It's huge!",
    "I'm trying to knit a sweater with spaghetti, " + sender_name + ". It's... going.",
    "Can't respond, " + sender_name + ", I'm on a secret mission. Code name: 'Nap Time'.",
    "Hey " + sender_name + ", I'm busy inventing a new language. Blargh means hello!",
    "I'm currently auditioning for the role of a statue, " + sender_name + ". Nailed it.",
    "Sorry, " + sender_name + ", I'm trying to write a book on how to procrastinate.",
    "I'm in the midst of a heated debate with my Alexa, " + sender_name + ". Tech stuff.",
    "Hey " + sender_name + ", can't talk. I'm practicing for the world sighing championship.",
    "I'm busy creating a new dance move, " + sender_name + ". It's called 'The Flailing Flamingo'.",
    "Can't talk now, " + sender_name + ", I'm trying to see if I can fly. Spoiler: I can't.",
    "Sorry, " + sender_name + ", I'm trying to make an ice cube igloo. It's a chill project.",
    "Hey " + sender_name + ", I'm currently on a quest to find the end of a circle."
]
    select_text = random.choice(texts)
    # i.e. responding to a specific message (note that this checks if "hello bot" is anywhere in the message, not just the beginning)
    if sender_type == "bot":
        pass

    elif "good morning" in text:
        send_message("good morning, " + sender_name)

    elif "good night" in text:
        send_message("good night, " + sender_name)

    elif "tell me about" in text and sender_id == os.getenv("sender_id"):
        text.replace('tell me about ', '')
        apiKey = os.getenv("API_KEY")
        response = requests.request("GET", f"https://newsapi.org/v2/everything?q={text}&from=2023-12-16&language=en&sortBy=publishedAt&apiKey={apiKey}")
        jsdata = json.loads(response.text)
        if 'articles' in jsdata and jsdata['articles']:
            first_article = jsdata['articles'][0]
            description = first_article['description']
            link = first_article['url']
            
            send_message(f"Description: {description}")
            send_message(f"Link:{link}")
        else:
            print("No articles found in the response.")

    elif text and sender_id == os.getenv("sender_id"):
        send_message(select_text)

    elif "hello bot" in text:
        send_message("sup")


    LAST_MESSAGE_ID = message["id"]

def main():
    global LAST_MESSAGE_ID
    recent_messages = get_group_messages()
    if recent_messages:
        LAST_MESSAGE_ID = recent_messages[0]['id']
    # this is an infinite loop that will try to read (potentially) new messages every 10 seconds, but you can change this to run only once or whatever you want
    while True:
        messages = get_group_messages(LAST_MESSAGE_ID)
        for message in reversed(messages):
            process_message(message)
        time.sleep(10)


if __name__ == "__main__":
    main()
