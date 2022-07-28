# ton-bot-example
Example of Telegram bot that can recieve payments in TON

All sources are in `src/` directory

# Setup
You need to complete 4 simple steps to set up and run the bot
### 1. Clone repository:
    git clone https://github.com/Gusarich/ton-bot-example.git
    cd ton-bot-example
### 2. Install PyPi packages
    pip install -r requirements.txt
### 3. Configure config
Open file `src/config.py` and enter your Bot token, Deposit address and Toncenter API key.

You can also switch between Mainnet and Testnet there by changing `RUN_IN_MAINNET` to `True` or `False`
### 4. Run the bot
    python src/bot.py
