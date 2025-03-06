import asyncio
import os
from twikit import Client
from configparser import ConfigParser


# Initialize client
client = Client('en-US')

config = ConfigParser()
config.read('config.ini')

username = config['X']['username']
email = config['X']['email']
password = config['X']['password']


async def main():

    if os.path.exists('cookies.json'):
        client.load_cookies('cookies.json')
    else:
        await client.login(
            auth_info_1=username,
            auth_info_2=email,
            password=password
        )
        client.save_cookies('cookies.json')
    
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