import discord, neuralintents, nltk, requests, json
from discord.ext import commands

nltk.download('omw-1.4')

chatbot = neuralintents.GenericAssistant("intents.json")
chatbot.train_model()
chatbot.save_model()

print("Bot is running...")

client = discord.Client()

token = "token"

def weather(city):
    base = "http://api.openweathermap.org/data/2.5/weather?"
    final = base + "appid=" + "d850f7f52bf19300a9eb4b0aa6b80f0d" + "&q=" + city
    response = requests.get(final)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]

        current_temperature = y["temp"] - 273.15
        current_temperature = int(current_temperature[0])
        z = x["weather"]

        weather_description = z[0]["description"]

        return "temperature : " + str(current_temperature) + "\n" + "description : " + str(weather_description)
    else:
        return "city not found"

def quote():
	response = requests.get("https://zenquotes.io/api/random")
	json_data = json.loads(response.text)
	quote = "* * *" + "\n" + json_data[0]['q'] + '\n' + '\n' + '(c) ' + json_data[0]['a'] + '\n' + '* * *'
	return "```" + quote + "```"

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("!ko quote"):
        await message.channel.send(quote())
    elif message.content.startswith("!ko weather"):
        await message.channel.send("```" + weather(message.content[12:]) + "```")
    elif message.content.startswith("!ko pat"):
        response = requests.get('https://some-random-api.ml/animu/pat')
        json_data = json.loads(response.text)

        embed = discord.Embed(color = 0xffdfb8)
        embed.set_image(url = json_data['link'])
        await message.channel.send(embed = embed)
    elif message.content.startswith("!ko hug"):
        response = requests.get('https://some-random-api.ml/animu/hug')
        json_data = json.loads(response.text)

        embed = discord.Embed(color = 0xff8080)
        embed.set_image(url = json_data['link'])
        await message.channel.send(embed = embed)
    elif message.content.startswith("!ko wink"):
        response = requests.get('https://some-random-api.ml/animu/wink')
        json_data = json.loads(response.text)

        embed = discord.Embed(color = 0xfafafa)
        embed.set_image(url = json_data['link'])
        await message.channel.send(embed = embed)
    elif message.content.startswith("!ko avatar"):
        content = message.content[11:]
        user = await client.fetch_user(int(content[2:-1]))
        userAvatar = user.avatar_url
        await message.channel.send(userAvatar)
    else:
        if message.content.startswith("!ko"):
            response = chatbot.request(message.content[4:])
            await message.channel.send(response)

client.run(token) 
