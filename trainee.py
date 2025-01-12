import disnake
from disnake.ext import commands

intents = disnake.Intents.default()
bot = commands.Bot(disnake.ext.commands.when_mentioned)

@bot.event
async def on_ready():
    print("Ботинок готов работать")


embed_t = {}
member = {}
take_user = {}
deny_user = {}

# Свой int
global role_id
role_id = 

@bot.slash_command()
async def send(inter):
    global user_id, member
    user = inter.author
    user_id = user.id
    view = disnake.ui.View()
    take_user[user_id] = disnake.ui.Button(style=disnake.ButtonStyle.success, label="Принять")
    deny_user[user_id]=disnake.ui.Button(style=disnake.ButtonStyle.danger, label="Отклонить")
    view.add_item(take_user[user_id])
    view.add_item(deny_user[user_id])

    async def take_callback(inter:disnake.Interaction):
        guild = inter.guild
        role = guild.get_role(role_id)
        await inter.user.add_roles(role)
        embed_t[user_id].add_field(name="Принят",value=" ")
        embed_t[user_id].color = disnake.Color.green()
        await inter.response.edit_message(embed=embed_t[user_id], components=[])

    async def deny_callback(inter: disnake.Interaction):
        embed_t[user_id].add_field(name="Отклонен", value=" ")
        embed_t[user_id].color = disnake.Color.red()
        await inter.response.edit_message(embed=embed_t[user_id], components=[])
    deny_user[user_id].callback = deny_callback
    take_user[user_id].callback = take_callback
    global embed_t
    embed_t[user_id] = disnake.Embed(title="Анкета", description=user.mention, color=disnake.Color.gold())
    await inter.response.send_message(embed=embed_t[user_id], view=view)
    
# Свой токен
token = " "

bot.run(token)