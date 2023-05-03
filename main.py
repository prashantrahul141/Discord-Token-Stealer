def main():
    from os import getenv
    from logger import logger
    logger.debug("loading env.")
    from dotenv import load_dotenv
    load_dotenv()
    from Bot import Client
    from discord import Intents
    intents = Intents.default()
    intents.message_content = True
    intents.members = True
    client = Client(intents=intents)
    client.run(getenv("DISCORD_BOT_TOKEN"))


if __name__ == '__main__':
    main()
