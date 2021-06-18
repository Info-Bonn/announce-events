import discord
from discord.ext import commands

from utils import utils as ut
from environment import EVENT_ROLE, EVENT_CHANNEL, PREFIX, ROLE_EVENT_HOST


class AnnounceEvents(commands.Cog):
    """
    Make an announcement
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='announce', aliases=['an', "anc"], help="Check if Bot available")
    async def announce(self, ctx: commands.Context, *input_text):
        """!
        ping to check if the bot is available

        @param ctx Context of the message
        """

        host_role = ctx.guild.get_role(ROLE_EVENT_HOST)
        if host_role not in ctx.author.roles and not ctx.author.guild_permissions.administrator:
            await ctx.send(
                embed=ut.make_embed(
                    color=ut.yellow,
                    name="You can't do that",
                    value=f"The role {host_role.mention} is needed to make an announcement. "
                          f"Please contact the server team if you think that this is an error."
                )
            )
            return

        text = ctx.message.content.replace(f"{PREFIX}{ctx.invoked_with} ", "")

        while True:

            pos = text.find("\@")

            if pos == -1:
                break

            text = text.replace("\@", "@")

        text = text.replace("@", "\@")

        ping_role = ctx.guild.get_role(EVENT_ROLE)
        event_channel = ctx.guild.get_channel(EVENT_CHANNEL)

        try:
            await event_channel.send(
                f'{ping_role.mention}\n\n 📨 Ankündigung von {ctx.author.mention} 📨\n\n'
                f'{text}'
            )

        except discord.Forbidden:
            await ctx.author.send(
                embed=ut.make_embed(
                    color=ut.red,
                    name="Error on sending your message",
                    value=f"Hey, I wasn't able to send your message into {event_channel.mention}\n"
                          f"This is probably an permission error, please check my permissions in this channel "
                          f"or inform an administrator."
                )
            )

        except Exception:
            await ctx.author.send(
                embed=ut.make_embed(
                    color=ut.red,
                    name="Error on sending your message",
                    value=f"Hey, I wasn't able to send your message into {event_channel.mention}\n"
                          f"I can only send messages up to 2000 characters, "
                          f"please check the length of your announcement"
                )
            )


def setup(bot):
    bot.add_cog(AnnounceEvents(bot))
