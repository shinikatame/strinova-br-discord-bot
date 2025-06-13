from discord.ext.commands.bot import Bot
from discord.ext.commands import Cog

from discord import Member, Embed, Colour

from components.rank_roles import RankRoles

sl = [
    # 'SBR_BOOST',
    # 'SBR_PONTO_REGRA',
    # 'SBR_RANKED',
    'SBR_SUBSTANCIA',
    'SBR_MOLECULA',
    'SBR_ATOMO',
    'SBR_PROTON',
    'SBR_NEUTRO',
    'SBR_ELETRON',
    'SBR_QUARK',
    'SBR_SUPERCORDA',
    'SBR_SINGULARIDADE',
    # 'SBR_TROFEU',
    # 'SBR_Trophy_fixed',
    # 'SBR_Skull',
]

class Ready(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot


    @Cog.listener('on_ready')
    async def ready(self):
        guild = await self.bot.fetch_guild(1381743234015035547)
        channel = await guild.fetch_channel(1381781974821113887)
        message = await channel.fetch_message(1383187450339524681)

        # embed = Embed()

        # embed.colour = Colour.green()

        # embed.description = f'{emojis["SBR_BOOST"]} Seja bem vindos(as) ao canal de cargos relacionado ao Strinova. \n\n'

        # embed.description += f'{emojis["SBR_PONTO_REGRA"]} Antes de explicar como você vai adquirir esse cargos, um aviso rápido que com o tempo podemos adicionar uns cargos mais pra frente, fique atento para não perder nenhum cargo limitado. \n\n'
        
        # embed.description += f'{emojis["SBR_RANKED"]} Aqui estão alguns cargos do modo competitivo: \n\n'

        # embed.description += f'{emojis["SBR_SUBSTANCIA"]} <@&1382839190005485579> \n'
        # embed.description += f'{emojis["SBR_MOLECULA"]} <@&1382839179003564083> \n'
        # embed.description += f'{emojis["SBR_ATOMO"]} <@&1382839197953560666> \n'
        # embed.description += f'{emojis["SBR_PROTON"]} <@&1382839233001160795> \n'
        # embed.description += f'{emojis["SBR_NEUTRO"]} <@&1382839239204671620> \n'
        # embed.description += f'{emojis["SBR_ELETRON"]} <@&1382839204563779716> \n'
        # embed.description += f'{emojis["SBR_QUARK"]} <@&1382839209710190712> (Necessário abrir um ticket <#1382211207779586079>) \n'
        # embed.description += f'{emojis["SBR_SUPERCORDA"]} <@&1382839216081469593> (Necessário abrir um ticket <#1382211207779586079>) \n'
        # embed.description += f'{emojis["SBR_SINGULARIDADE"]} <@&1382839223639343235> (Necessário abrir um ticket <#1382211207779586079>) \n\n'

        # embed.description += f'{emojis["SBR_TROFEU"]} Segue abaixo os cargos que podem ser adquiridos participando dos nossos torneios: \n\n'

        # embed.description += f'{emojis["SBR_Trophy_fixed"]} <@&1383149666098614343> (Seja campeão da edição semanal do torneio) \n'
        # embed.description += f'{emojis["SBR_Skull"]} <@&1383166371973828729> (Faça 30 kills durante as partidas MD3 do torneio semanal) \n'

        await message.edit(view = RankRoles())


def setup(bot):
    bot.add_cog(Ready(bot))
