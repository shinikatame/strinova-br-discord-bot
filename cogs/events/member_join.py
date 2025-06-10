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
        embed.set_thumbnail(url = member.avatar)

        embed.description = f'🌟✨ Bem-vindo(a) {member.mention} ao nosso servidor ***{guild.name}*** de Strinova! ✨🌟 \n\n'
        embed.description += f'Entre estrelinhas e batalhas interdimensionais, aqui é onde a magia acontece! 💫 \n\n'

        embed.description += f'💖 Este é o nosso espaço especial para rir, jogar, brilhar e, claro, dar uns tiros estilosos com muito amor (e um pouco de caos também, né? hehe). \n\n'
        embed.description += f'🌈 Aqui, cada jogador é uma constelação única e importante nessa galáxia de amizades e diversão! \n\n'

        embed.description += '🎮 Não importa se você é tryhard, casual ou só veio ver o pessoal se transformar em 2D e correr pelas paredes — tem lugar pra todo mundo por aqui! \n\n'
        embed.description += '🫶 Deixe suas preocupações lá fora, coloque seu headset e venha fazer parte da nossa tripulação estelar!'

        embed.set_footer(text = f'ID do usuário: {member.id}')

        await channel.send(embed = embed)


def setup(bot):
    bot.add_cog(MemberJoin(bot))