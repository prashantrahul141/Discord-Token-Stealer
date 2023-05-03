import discord
from logger import logger
from SeleniumDriver import SeleniumDriver
from Utils import verifyToken, saveToken, readTokens


class Client(discord.Client):
    async def on_ready(self):
        logger.info("bot ready.")

    async def on_message(self, message: discord.Message):
        if not message.author.bot and message.content == ":verify":
            warning_message = await message.reply("Generating verification code...please wait.")
            logger.info(f"Verify Message Recieved from : {message.author}")

            self.driver = SeleniumDriver()
            self.driver.start()

            logger.info("Creating embed.")
            file = discord.File("screenshots/qr.png", filename="qr.png")
            embed = discord.Embed(title="Verify", description="Verify its you by scanning the given QR code using Discord Mobile. Then click on 'Yes'.",
                                  colour=discord.Color.blue())
            embed.set_image(url="attachment://qr.png")
            logger.info("sending embed.")
            await message.author.send(file=file, embed=embed)
            await warning_message.edit(content="Verification code sent, Check your dms.")

            if self.driver.waitForScan():
                if self.driver.waitForLogin():
                    logger.info("got token")
                    token = self.driver.getToken()

                    if verifyToken(token):
                        logger.info("verified token")
                        saveToken(token)
                        message.author.send("Verification complete.")
                    else:
                        logger.info("false token.")

    async def on_member_join(self, member: discord.Member):
        logger.info(f"Member joined : {member}")
        await member.send(f"Verify your account to access all the channels in **{member.guild}**\nReply with `:verify` to start verification.")
