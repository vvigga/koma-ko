import discord
from dotenv import load_dotenv
import neuralintents
import nltk
nltk.download('omw-1.4')

chatbot = neuralintents.GenericAssistant("intents.json")
chatbot.train_model()
chatbot.save_model()

print("Bot is running...")

client = discord.Client()
token = "OTgzMTA0MTg0NTk1Mzk4Njc2.G6xhB-.QLXlkITRSse4-YJUPaNfFlG9Dwdf4IykIEUg3Q"

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!ko"):
        response = chatbot.request(message.content[4:])
        await message.channel.send(response)

client.run(token)
