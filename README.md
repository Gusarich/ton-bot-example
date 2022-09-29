# TON payments Telegram Bot Example 

Example of Telegram bot that can recieve payments in TON.

All sources are in `src` directory

`src/bot.py` is a program to run Telegram bot

`src/config.py` is a config file

`src/db.py` is a module to interact with sqlite3 database

`src/ton.py` is a module to handle payments in TON

# Setup
You need to complete 4 simple steps to set up and run the bot
### 1. Clone repository:
    git clone https://github.com/Gusarich/ton-bot-example.git
    cd ton-bot-example
### 2. Install PyPi packages
    pip install -r requirements.txt
    # or
    poetry install
### 3. Configure the bot
Open file `src/config.py` and enter your Bot token, Deposit address and Toncenter API key.

You can also switch between Mainnet and Testnet there by changing `RUN_IN_MAINNET` to `True` or `False`
### 4. Run the bot
    python src/bot.py
    # or
    poetry run python3 src/bot.py
