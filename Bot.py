import os
import logging
import discord
import aiohttp
from discord.ext import tasks
from dotenv import load_dotenv

logging.basicConfig(filename='token.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

script_dir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(script_dir, ".env"))

CRYPTO = os.getenv("CRYPTO")
TOKEN = os.getenv("TOKEN")
FIAT1 = os.getenv("FIAT1")
FIAT2 = os.getenv("FIAT2")
if not TOKEN:
    logging.error("Token not found. Please check your .env file.")
    exit()

client = discord.Client(intents=discord.Intents.default())


async def get_prices():
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(f'https://api.coingecko.com/api/v3/coins/markets?vs_currency={FIAT1}&ids={CRYPTO}') as response:
                data = await response.json()

                if data and data[0].get('current_price') and data[0].get('price_change_percentage_24h'):
                    current_price = data[0].get('current_price', 0)
                    price_change = data[0].get('price_change_percentage_24h', 0)

                    async with session.get(f'https://api.coingecko.com/api/v3/coins/markets?vs_currency={FIAT2}&ids={CRYPTO}') as response2:
                        data2 = await response2.json()

                        if data2 and data2[0].get('current_price') and data2[0].get('price_change_percentage_24h'):
                            current_price2 = data2[0].get('current_price', 0)

                            activity_text = f"${current_price:.2f} ₱{current_price2:.2f} {price_change:.2f}%"
                            await client.change_presence(activity=discord.Game(name=activity_text))
                            logging.info(f'Updated price to $ {current_price:.3f}, Price change {price_change:.2f}%')
                        else:
                            logging.warning(f'Could not load price data for {CRYPTO}')
                else:
                    logging.warning(f'Could not load price data for {CRYPTO}')

        except Exception as e:
            logging.error(f"Error occurred while fetching prices: {e}")


@client.event
async def on_ready():
    logging.info(f'Logged in as {client.user}')
    get_prices_loop.start()


@tasks.loop(seconds=20)
async def get_prices_loop():
    await get_prices()


if __name__ == '__main__':
    client.run(TOKEN)
