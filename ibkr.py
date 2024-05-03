import discord
from discord.ext import commands
import asyncio
import ib_insync

# Initialize IBKR API client
ib = ib_insync.IB()

# Discord bot configuration
bot = commands.Bot(command_prefix='!')

# IBKR API connection details
host = 'your_ibkr_host'
port = 4001  # Port number for IBKR API (adjust if needed)
client_id = 1  # Client ID for API connection

# Connect to IBKR API
ib.connect(host, port, client_id)

# Function to execute a trade
async def execute_trade(contract, action, quantity):
    order = ib_insync.MarketOrder(action, quantity)
    trade = ib.placeOrder(contract, order)
    await asyncio.sleep(1)  # Delay to allow order to process
    return trade

# Event listener for incoming Discord messages
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # Ignore messages sent by the bot itself

    # Example: Check if message contains trade alert
    if 'buy' in message.content.lower() or 'sell' in message.content.lower():
        # Extract trade details from message (replace with your parsing logic)
        contract = ib_insync.Stock('AAPL', 'SMART', 'USD')  # Example contract
        action = 'BUY' if 'buy' in message.content.lower() else 'SELL'
        quantity = 100  # Example quantity (adjust as needed)

        # Execute the trade
        trade = await execute_trade(contract, action, quantity)
        await message.channel.send(f'Trade executed: {action} {quantity} {contract.symbol}')

    await bot.process_commands(message)

# Bot startup event
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Run the Discord bot
bot.run('YOUR_DISCORD_BOT_TOKEN')  # Replace with your Discord bot token
