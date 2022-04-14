import discord
from flask_oauthlib.client import OAuth
from flask import Flask
import threading
import os
from dotenv import load_dotenv
load_dotenv()


def discord_bot():
    discord_token = os.getenv('DISCORD_TOKEN')
    client = discord.Client()
    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')
    @client.event
    async def on_message(message):
       if message.content == "$hello":
           await message.channel.send("Hello!")
    client.run(discord_token)


def get_vendor():
    



def web_server():
    d2oauth = OAuth()
    destiny2 = d2oauth.remote_app('bungie',
                                    base_url='https://www.bungie.net/Platform/',
                                    request_token_url='https://www.bungie.net/Platform/App/OAuth/token/',
                                    access_token_url='https://www.bungie.net/Platform/App/OAuth/Token/',
                                    authorize_url='https://www.bungie.net/en/OAuth/Authorize',
    )
    print("thread 2")




if __name__ == "__main__":
   discord_bot()

