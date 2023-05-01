import discord
from logger import logger


class Client(discord.Client):
    async def on_ready(self):
        logger.info("bot ready.")

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome {member.mention} to {guild.name}!'
            await guild.system_channel.send(to_send)
