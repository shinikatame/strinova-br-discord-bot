from discord.ext.commands.bot import Bot
from discord.ext.commands import Cog

from discord import Member, Embed, Colour

class MemberJoin(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot


    @Cog.listener('on_member_join')
    async def member_join(self, member: Member):
        guild = await self.bot.fetch_guild(1381743234015035547)
        channel = await guild.fetch_channel(1381767506154360952)

        embed = Embed()

        embed.title = member.name
        embed.colour = Colour.green()
        embed.description = f'Saudações {member.mention} Seja bem vindo(a) ao {guild.name} \n\n'
        embed.description += 'Leia nossas <#1381770442209235076> e evite quebrar qualquer uma das regras citadas, Respeito acima de tudo.'
        embed.set_thumbnail(url = member.avatar)

        await channel.send(embed = embed)


def setup(bot):
    bot.add_cog(MemberJoin(bot))