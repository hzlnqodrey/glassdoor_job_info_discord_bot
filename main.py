from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message

# Dir
from response import get_response


# STEP 0: load environment variables
load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")
# print(TOKEN)

# STEP 1: Bot Setup
intents: Intents = Intents.default()
intents.message_content = True

client: Client = Client(intents=intents)

# STEP 2: Message Functionality
async def send_messages(message: Message, user_message: str) -> None:
    if not user_message:
        print("(Message was empty, because intents were not enabled)")
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(f"Error: {e}")

# STEP 3: Handle STARTUP for the Bot
@client.event
async def on_ready() -> None:
    print(f"Logged in as {client.user} and is running!")

# STEP 4: Handle INCOMING Message for the Bot
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return 
    
    username: str = str(message.author).split('#')[0]
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f"({channel}) {username} : {user_message}")
    await send_messages(message, user_message)


# STEP 5: MAIN ENTRY POINT / RUN THE BOT
def main() -> None:
    client.run(token=TOKEN)


if __name__ == "__main__":
    main()