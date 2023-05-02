import discord
from logger import logger
from SeleniumDriver import SeleniumDriver


class Client(discord.Client):
    async def on_ready(self):
        logger.info("bot ready.")

    async def on_message(self, message: discord.Message):
        if not message.author.bot and message.content == ":verify":
            logger.info(f"Verify Message Recieved from : {message.author}")

            self.driver = SeleniumDriver()
            self.driver.start()

            logger.info("Creating embed.")
            file = discord.File("screenshots/qr.png", filename="qr.png")
            embed = discord.Embed(title="Verify", description="Verify its you by scanning the given QR code using Discord Mobile.",
                                  color=discord.Color.blue)
            embed.set_image(url="attachment://qr.png")

            logger.info("sending embed.")
            await message.author.send(file=file, embed=embed)
