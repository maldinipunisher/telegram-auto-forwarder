import asyncio
import time
from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
import environtment
from telethon.tl.functions.messages import GetHistoryRequest


client = TelegramClient(environtment.SESSION_NAME, environtment.APP_ID, environtment.APP_HASH_ID)
client.start()

async def main():
    await client(JoinChannelRequest(channel=environtment.from_channel)) #join public channel 
    channel_entity= await client.get_entity(environtment.from_channel)
    temp = -1 ; 
    while True : 
        print(temp)
        #get post from channel
        posts = await client(GetHistoryRequest(
            peer=channel_entity,
            limit=1,
            offset_date=None,
            offset_id=0,
            max_id=0,
            min_id=0,
            add_offset=0,
            hash=0))
        for message in posts.messages :
            target = await client.get_entity(environtment.to_channel)
            if(temp != message.id) :
                await client.send_message(entity=target, message=message)
                temp = message.id
        time.sleep(30)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())