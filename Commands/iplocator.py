import requests
import discord
from discord.ext import commands

rest = "http://ip-api.com/json/"

class IPLocatorCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        pass
    
    @commands.command(name = "iplocator", aliases = ["locator"])
    async def IPLocator(self, ctx, *, ip = None):
        if (ip == None):
            await ctx.reply(content = "Informe um endereço ip!", delete_after = 5.0)
            return
        
        author = ctx.message.author
        get = requests.get(rest+ip).json()
        Zip = f"""{get["zip"]}"""
        if (not Zip):
            Zip = "Não encontrado"
        else:
            Zip = Zip

        info = {
            "all": f"""Endereço ip: {get["query"]}
País: {get["country"]}
Código do país: {get["countryCode"]}
Região: {get["region"]}
Nome da região: {get["regionName"]}
Cidade: {get["city"]}
Fuso horário: {get["timezone"]}
Latitude: {get["lat"]}
Longitude: {get["lon"]}
Zip: {Zip}
Fornecedor: {get["isp"]}
Org: {get["org"]}"""
        }

        IPLocatorEmbed = discord.Embed(description = info["all"], color = discord.Color.red())
        IPLocatorEmbed.set_author(name = f"IPLocator - {ip}", icon_url = self.bot.user.avatar_url, url = rest+ip)
        IPLocatorEmbed.set_footer(text = f"Req: {ctx.message.author.name}", icon_url = ctx.message.author.avatar_url)

        await ctx.reply(content = f"IPLocator: {ip}", embed = IPLocatorEmbed)
    
    @IPLocator.error
    async def error(self, ctx, error):
        await ctx.reply(
            content = f"Ocorreu um erro!\n```py\n{error}```",
            delete_after = 10.0
        )

def setup(IPLocator):
    IPLocator.add_cog(IPLocatorCommand(IPLocator))
