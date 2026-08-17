# Discord IBKR Bot

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![Discord](https://img.shields.io/badge/Discord-Bot-5865F2?style=flat&logo=discord&logoColor=white)](https://discord.com)
[![ib_insync](https://img.shields.io/badge/ib__insync-0.9.86+-brightgreen?style=flat)](https://github.com/erdewit/ib_insync)
[![License](https://img.shields.io/github/license/NadirAliOfficial/Discord-IBKR-)](LICENSE)

A Discord bot that bridges trading alerts from Discord channels directly to Interactive Brokers. Monitors specified channels for buy/sell signals, parses structured alert messages, and executes orders via `ib_insync` — with trade journaling, position tracking, and Discord reply confirmations.

---

## How It Works

```
Discord Channel Alert
  "BUY AAPL 100 shares TP: 195 SL: 185"
          │
          ▼
    Message Parser
    (regex + NLP)
          │
          ▼
    Signal Validator
    (symbol check, size limits, duplicate filter)
          │
          ▼
    IBKR Order Engine (ib_insync)
    ├── Market order (entry)
    ├── Limit order (take profit)
    └── Stop order (stop loss)
          │
          ▼
    Discord Reply  +  Local Trade Journal
    "✅ BUY AAPL 100 @ $190.32 | TP: $195 | SL: $185"
```

---

## Features

- **Channel monitoring** — watches one or more Discord channels for structured trade alerts
- **Alert parsing** — extracts symbol, direction, quantity, TP, and SL from natural-language messages
- **IBKR execution** — places market entry + limit TP + stop SL orders via `ib_insync`
- **Duplicate filter** — ignores repeat signals for an already-open position in the same direction
- **Discord reply confirmation** — bot replies to the alert message with order fill details
- **Trade journal** — all trades logged with entry price, TP/SL levels, fill times, and exit reason
- **Position tracker** — `/positions` command shows all open IBKR positions with unrealized P&L
- **Manual override** — `/close SYMBOL` command to close any position directly from Discord

---

## Setup

### 1. Install dependencies

```bash
pip install discord.py ib_insync python-dotenv
```

### 2. Configure `.env`

```env
DISCORD_TOKEN=your_discord_bot_token
CHANNEL_IDS=123456789,987654321
IB_HOST=127.0.0.1
IB_PORT=7497
IB_CLIENT_ID=2
```

### 3. Start TWS or IB Gateway

Enable API access in TWS: **File → Global Configuration → API → Settings → Enable ActiveX and Socket Clients**

### 4. Run

```bash
python bot.py
```

---

## Alert Format

The bot parses alerts in this format (flexible, not strict):

```
BUY AAPL 50 TP 195.50 SL 185.00
SELL EURUSD 10000 TP 1.0850 SL 1.0950
CLOSE TSLA
```

Supported keywords: `BUY`, `SELL`, `LONG`, `SHORT`, `CLOSE`, `EXIT`

---

## Discord Commands

| Command | Description |
|---|---|
| `/positions` | List all open IBKR positions with unrealized P&L |
| `/close SYMBOL` | Immediately close the position for a symbol |
| `/journal` | Show today's completed trades with entry/exit prices |
| `/status` | Show IBKR connection status and account balance |

---

## Project Structure

```
Discord-IBKR-/
├── bot.py          # Main Discord bot — event listeners, command handlers
├── parser.py       # Alert message parsing logic
├── ibkr.py         # IBKR order execution via ib_insync
├── journal.py      # Trade logging and retrieval
├── .env            # Bot token and config (not committed)
└── README.md
```

---

## Notes

- Run in paper trading mode first (`IB_PORT=7497`) to validate parsing and execution
- For Forex symbols, use standard format: `EURUSD`, `GBPUSD` (no slash)
- The bot must have **Read Messages** and **Send Messages** permissions in the monitored channels

---

## Developer

Built by **Nadir Ali Khan** — [TEAM NAK](https://github.com/NadirAliOfficial) | [Telegram](https://t.me/NAKBlockDev)
