# Requests for API, Asyncio to call sleep() in async func
import requests
import asyncio

# Aiogram
from aiogram import Bot
from aiogram.types import ParseMode

# We also need config and database here
import config
import db


async def start():
    # Function that is checking our wallet for new deposits and process them

    try:
        # Try to load last_lt from file
        with open('last_lt.txt', 'r') as f:
            last_lt = int(f.read())
    except FileNotFoundError:
        # If file not found, set last_lt to 0
        last_lt = 0

    # We need the Bot instance here to send deposit notifications to users
    bot = Bot(token=config.BOT_TOKEN)

    while True:
        # 2 Seconds delay between checks
        await asyncio.sleep(2)

        # API call to Toncenter that returns last 100 transactions of our wallet
        resp = requests.get(f'{config.API_BASE_URL}/api/v2/getTransactions?'
                            f'address={config.DEPOSIT_ADDRESS}&limit=100&'
                            f'archival=true&api_key={config.API_KEY}').json()

        # If call was not successful, try again
        if not resp['ok']:
            continue

        # Iterating over transactions
        for tx in resp['result']:
            # LT is Logical Time and Hash is hash of our transaction
            lt, hash = int(tx['transaction_id']['lt']), tx['transaction_id']['hash']

            # If this transaction's logical time is lower than our last_lt,
            # we already processed it, so skip it

            if lt <= last_lt:
                continue

            # Get value of transaction (how much NanoTONs have we received)
            value = int(tx['in_msg']['value'])
            if value > 0:
                # If value is greater than 0, it is probably a new deposit and
                # we must process it by increasing someone's balance in database
                uid = tx['in_msg']['message']

                # If transaction comment isn't a number, skip it
                if not uid.isdigit():
                    continue

                uid = int(uid)
                
                if not db.check_user(uid):
                    continue

                # Here 'message' is a existing user's ID
                # and 'value' is deposit amount

                # Increase user's balance in database
                db.add_balance(uid, value)

                # Send a message to user
                await bot.send_message(uid, 'Deposit confirmed!\n'
                                      f'*+{value / 1e9:.2f} TON*',
                                      parse_mode=ParseMode.MARKDOWN)

            # After we processed new transaction, last_lt must be updated
            last_lt = lt
            with open('last_lt.txt', 'w') as f:
                f.write(str(last_lt))
