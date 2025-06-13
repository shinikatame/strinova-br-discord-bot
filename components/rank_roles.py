from discord import Interaction
from discord.ui import View, Button, button

from asyncio import create_task, gather

ROLES = {
    'substance': {'role_id': 1382839190005485579, 'emoji': '<:SBR_SUBSTANCIA:1381884665027231764>'},
    'molecule': {'role_id': 1382839179003564083, 'emoji': '<:SBR_MOLECULA:1381884851560386571>'},
    'atom': {'role_id': 1382839197953560666, 'emoji': '<:SBR_ATOMO:1381885081978671177>'},
    'proton': {'role_id': 1382839233001160795, 'emoji': '<:SBR_PROTON:1381885176971530280>'},
    'neutral': {'role_id': 1382839239204671620, 'emoji': '<:SBR_NEUTRO:1381885249679786044>'},
    'electron': {'role_id': 1382839204563779716, 'emoji': '<:SBR_ELETRON:1381885341815930953>'}
}


class RankRoles(View):
    def __init__(self):
        super().__init__(timeout = None)


    @button(emoji = ROLES['substance']['emoji'], custom_id = 'substance')
    async def substance(self, button: Button, inter: Interaction):
        await self.remove_roles(inter)
        
        role = inter.guild.get_role(ROLES['substance']['role_id'])
        await inter.user.add_roles(role)


    @button(emoji = ROLES['molecule']['emoji'], custom_id = 'molecule')
    async def molecule(self, button: Button, inter: Interaction):
        await self.remove_roles(inter)
        
        role = inter.guild.get_role(ROLES['molecule']['role_id'])
        await inter.user.add_roles(role)


    @button(emoji = ROLES['atom']['emoji'], custom_id = 'atom')
    async def atom(self, button: Button, inter: Interaction):
        await self.remove_roles(inter)
        
        role = inter.guild.get_role(ROLES['atom']['role_id'])
        await inter.user.add_roles(role)


    @button(emoji = ROLES['proton']['emoji'], custom_id = 'proton')
    async def proton(self, button: Button, inter: Interaction):
        await self.remove_roles(inter)
        
        role = inter.guild.get_role(ROLES['proton']['role_id'])
        await inter.user.add_roles(role)


    @button(emoji = ROLES['neutral']['emoji'], custom_id = 'neutral')
    async def neutral(self, button: Button, inter: Interaction):
        await self.remove_roles(inter)

        role = inter.guild.get_role(ROLES['neutral']['role_id'])
        await inter.user.add_roles(role)


    @button(emoji = ROLES['electron']['emoji'], custom_id = 'electron')
    async def electron(self, button: Button, inter: Interaction):
        await self.remove_roles(inter)
        
        role = inter.guild.get_role(ROLES['electron']['role_id'])
        await inter.user.add_roles(role)


    async def remove_roles(self, inter: Interaction):
        get_role = inter.guild.get_role
        roles = [get_role(role['role_id']) for role in ROLES.values()]

        await inter.user.remove_roles(*roles)

        await inter.response.send_message('Nível alterado', ephemeral = True)
