import interactions
from interactions import ClientPresence, ChannelType, Image

from config.secrets import token

bot = interactions.Client(token=token)

# ideia do que fazer
# prmeira mensagem apenas com os dois botoes, para tirar ou por
# ou uma invocacao ephimeral dessa merda, mas um default sem esse ephm
# o resto e ephemeral
# dps disso o bot manda um novo select menu para escolher
# e dps apply

# region debug category
@bot.command(name="debug", )
async def debug(ctx):
    pass


# region error handling
@debug.error
async def debug_error(ctx, error: Exception):
    await ctx.send(f"Error: {error}")


# endregion

# region PingPong

@debug.subcommand(name="ping", description="answers with pong")
async def ping(ctx: interactions.CommandContext):
    await ctx.send("Pong!")


# endregion

# region commandArgs
@debug.subcommand(name="command-args", description="interact with the bot")
@interactions.option()
@interactions.option()
async def textCommand(ctx: interactions.CommandContext, text: str, text2: str):
    await ctx.send(f"You said '{text}'!")


# endregion

# region change username or avatar
@debug.subcommand(name="change-user", description="change the username or avatar of the bot")
@interactions.option(name="username", description="the new username of the bot")
@interactions.option(name="avatar", description="the link to the new avatar of the bot")
async def changeUser(ctx: interactions.CommandContext, username: str = None, avatar: str = None):
    if username:
        await bot.modify(username=username)
    if avatar:
        await bot.modify(avatar=Image(avatar))

#endregion

# endregion

# region help category
@bot.command(name="help", description="dms commands")
async def help(ctx):
    await ctx.send("TODO")


# endregion

# region role self choose category

# region components
addGameButton = interactions.Button(
    label="Add game",
    style=interactions.ButtonStyle.PRIMARY,
    custom_id="add_game",
)
removeGameButton = interactions.Button(
    label="Remove game",
    style=interactions.ButtonStyle.SECONDARY,
    custom_id="remove_game",
)
addAndRemoveRow = interactions.ActionRow(
    components=[removeGameButton, addGameButton]
)

options = [
        interactions.SelectOption(
            label="League of Legends",
            value="league_of_legends",
            default=False,
        ),
        interactions.SelectOption(
            label="Overwatch",
            value="overwatch",
            default=False,
        ),
        interactions.SelectOption(
            label="Valorant",
            value="valorant",
            default=False,
        ),
        interactions.SelectOption(
            label="MineCraft",
            value="minecraft",
            default=False,
        ),
        interactions.SelectOption(
            label="Among us",
            value="among_us",
            default=False,
        ),
        interactions.SelectOption(
            label="Free games",
            value="free_games",
            default=False,
        ),
    ]


gameChoices = [
    interactions.Choice() #TODO
]

# endregion

@bot.command(name="get-pinged",
             description="choose games to get pinged for when someone is looking to game, or for patches")
async def roleMain(ctx):
    pass

@roleMain.subcommand(name="gui", description="gui for choosing games")
@interactions.option()
async def roleStart(ctx, ephemeral:bool = True):
    # channels = [channel for guild in bot.guilds for channel in guild.channels if channel.type == ChannelType.GUILD_TEXT]
    await ctx.send("Add or remove role?", components=[
        addAndRemoveRow
    ] ,ephemeral= ephemeral)

# region addRole
@bot.component('add_game')
async def addGame(ctx: interactions.ComponentContext):
    # get the info of the clicker (roles not in), and send scroller (ephemeral)
    selectGameAdder = interactions.SelectMenu(
        custom_id="select_game_add",
        options=options, #TODO change depending on author info
    )
    await ctx.send(ctx.author.name + ", Select a game to add", components=[
        interactions.ActionRow(
         components=[selectGameAdder],
        ),
    ], ephemeral=True)

@bot.component('select_game_add')
async def selectGameChoosenAdd(ctx: interactions.ComponentContext, valueSelected : list[str]):
    match valueSelected[0]:
        # TODO add roles
        case "league_of_legends":
            await ctx.send("league_of_legends")
        case "overwatch":
            await ctx.send("overwatch")
        case "valorant":
            await ctx.send("valorant")
        case "minecraft":
            await ctx.send("minecraft")
        case "among_us":
            await ctx.send("among_us")
        case "free_games":
            await ctx.send("free_games")
        case _:
            await ctx.send("no role found")

#endregion

#region removeRole
@bot.component('remove_game')
async def removeGame(ctx: interactions.ComponentContext):
    # get the info of the clicker (roles in), and send scroller (ephemeral)
    selectGameRemover = interactions.SelectMenu(
        custom_id="select_game_remove",
        options=options, #TODO change depending on author info
    )
    await ctx.send(ctx.author.name + ", Select a game to remove", components=[
        interactions.ActionRow(
         components=[selectGameRemover],
        ),
    ], ephemeral=True)

@bot.component('select_game_remove')
async def selectGameChoosenRemove(ctx: interactions.ComponentContext, valueSelected : list[str]):
    match valueSelected[0]:
        # TODO remove roles
        case "league_of_legends":
            await ctx.send("league_of_legends")
        case "overwatch":
            await ctx.send("overwatch")
        case "valorant":
            await ctx.send("valorant")
        case "minecraft":
            await ctx.send("minecraft")
        case "among_us":
            await ctx.send("among_us")
        case "free_games":
            await ctx.send("free_games")
        case _:
            await ctx.send("no role found")
#endregion


# endregion

# pres = ClientPresence()
# pres.status = "shut up"
# bot.change_presence(presence=pres)

bot.start()
