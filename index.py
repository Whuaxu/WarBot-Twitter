import asyncio
import os
from twikit import Client
from configparser import ConfigParser
from modules.io import readJson, writeJson

config = ConfigParser()
config.read('./private/config.ini')

username = config['X']['username']
email = config['X']['email']
password = config['X']['password']


# Initialize client
client = Client('en-US')


async def main():

    if os.path.exists('./private/cookies.json'):
        client.load_cookies('./private/cookies.json')
    else:
        await client.login(
            auth_info_1=username,
            auth_info_2=email,
            password=password
        )

        client.save_cookies('./private/cookies.json')

    # Upload media files and obtain media_ids
    media_ids = [
        await client.upload_media('./images/template.jpg')
    ]
    

    # Create a tweet with the provided text and attached media
    await client.create_tweet(
        text='Example Text',
        media_ids=media_ids
    )
    
asyncio.run(main())