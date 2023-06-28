import discord
from discord.ext import commands
import BotFunctions
from BotFunctions import *


# instantiate bot object
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)


# event listener for starting the bot
@bot.event
async def on_ready():
    # greet everyone on wakeup
    print('Client Ready!')
    test_channel_code = BotFunctions.get_channel_code('Resources/channelcodes.csv', 'test')
    test_channel = bot.get_channel(int(test_channel_code))  # channel for the bot test
    await test_channel.send('theme bot online')


# test that bot is reading messages
@bot.event
async def on_message(message):
    if message.content == "chris":
        await message.channel.send("cheats at battleship")
    if message.content == "tristan":
        await message.channel.send("has small shoulders")
    if message.content == "hayden":
        await message.channel.send("is a manlet")
    if message.content == "amanda":
        await message.channel.send("pegs chris")
    await bot.process_commands(message)


# Input themes to list, also gets information from discord message
# info to grab: Theme, Creator, Used (will always be false), Date added, Date Used (should always be NaN)
@bot.command(name='add_theme')
async def input_theme(ctx, *theme_idea):
    theme_idea = format_input(*theme_idea)
    date_time = ctx.message.created_at
    date_time = date_time.strftime('%m/%d/%Y')
    creator = ctx.message.author
    if not contains_theme(theme_idea, 'Themes.csv'):
        add_theme(theme_idea, creator, False, date_time, 'NaN')
        await ctx.message.channel.send("added theme")
    else:
        await ctx.message.channel.send("Theme already exists in themes database")


@bot.command(name='print_themes')
async def print_unused_themes(ctx):
    await ctx.channel.send('Printing all unused themes in list: ')
    unused_list = get_unused_themes('Themes.csv')
    await ctx.channel.send(unused_list)


@bot.command(name='print_used')
async def print_used_themes(ctx):
    await ctx.channel.send("Printing all of the used themes in list: ")
    used_list = get_used_themes('Themes.csv')
    await ctx.channel.send(used_list)


@bot.command(name='select_theme')
async def select_theme_bot(ctx):
    theme = select_theme()
    await ctx.channel.send(f'Your next theme is: {theme}')


# gets token for the discord server, keep the token in a different file that doesn't get pushed to GitHub for security.
with open('Resources/token.txt') as f:
    token = f.readline()


@bot.command(name='man')
async def man(ctx, *manpage):
    if len(manpage) == 0:
        manpage = ''
    output = manual(manpage)
    await ctx.channel.send(output)


bot.run(token)
