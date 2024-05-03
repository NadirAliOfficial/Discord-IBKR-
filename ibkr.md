

# Discord Bot for Automated Trading with IBKR API

This Discord bot allows you to automate trading actions on Interactive Brokers (IBKR) based on trade alerts posted in Discord channels. The bot listens for specific keywords in messages (e.g., 'buy', 'sell') and executes corresponding trades using the IBKR API.

## Requirements

- Python 3.6+
- `discord.py` library (`pip install discord.py`)
- `ib_insync` library (`pip install ib_insync`)
- Interactive Brokers account with API access

## Setup

1. **Clone Repository:**
   ```bash
   git clone https://github.com/yourusername/discord-ibkr-bot.git
   cd discord-ibkr-bot
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configuration:**
   - Obtain a Discord bot token from the [Discord Developer Portal](https://discord.com/developers/applications).
   - Replace `'YOUR_DISCORD_BOT_TOKEN'` in `bot.py` with your Discord bot token.
   - Update `host`, `port`, and `client_id` in `bot.py` with your IBKR API connection details.

## Usage

1. **Run the Bot:**
   ```bash
   python bot.py
   ```

2. **Interacting with the Bot:**
   - Invite the bot to your Discord server using the invite link generated from the [Discord Developer Portal](https://discord.com/developers/applications).
   - Post trade alerts in Discord channels containing keywords like 'buy' or 'sell'.
   - The bot will detect these keywords and execute corresponding trades on IBKR using the specified contract and quantity.

## Features

- Listens for trade alerts in Discord channels and executes trades automatically.
- Supports basic trade actions (buying and selling) based on message content.
- Demonstrates integration with the IBKR API for real-time trade execution.

## Customization

- Modify the parsing logic in `bot.py` to extract trade details from Discord messages according to your specific trade alert format.
- Implement additional trade actions (e.g., setting stop-loss orders, handling multiple contracts) based on your trading strategy.

## Disclaimer

- **Use at your own risk:** Automated trading involves financial risks. Ensure proper risk management and testing before deploying the bot for live trading.
- This project is for educational and demonstration purposes only. The author assumes no responsibility for any financial losses incurred through the use of this software.

## Contributing

Contributions are welcome! Feel free to submit issues, feature requests, or pull requests to improve this project.
