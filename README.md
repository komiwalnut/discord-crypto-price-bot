# discord-crypto-price-bot

A Discord bot that displays the current price of the **Ronin (RON)** (or your preferred cryptocurrency) token in USD and PHP, along with the 24-hour price change percentage, as its activity status.

## Features
- Fetches live cryptocurrency prices from the [CoinGecko API](https://www.coingecko.com/).
- Updates the bot's activity status with:
  - Current price in USD and PHP.
  - 24-hour price change percentage.

## Usage Instructions
### Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/komiwalnut/discord-crypto-price-bot.git
    cd discord-crypto-price-bot
    ```

2. Create a `keys` directory outside of `discord-crypto-price-bot` (refer to [Directory Structure](#directory-structure)):
   
4. Create a `pricebot.env` file in that directory with the following content:
    ```
    RONTOKEN=your_discord_bot_token_here
    ```

5. Install the required dependencies:
    ```bash
    pip install -U discord aiohttp python-dotenv
    ```

6. Run the bot:
    ```bash
    nohup python3 -u RONBot.py > /dev/null 2>&1 &
    ```
    This command runs the bot in the background on Linux. Ensure you're on a Linux-based system to use this setup.

### How to Create a Discord Bot
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click **New Application**, give it a name (e.g., `$RON`), and click **Create**.
3. In the application settings:
   - Customize your bot’s name and upload an app icon (e.g., an image of the **RON** token).
   - Go to the **Bot** tab and click **Add Bot**.
   - Under **Token**, click **Reset Token**, confirm the action, and copy the token.
   - Paste the token into the `pricebot.env` file like this:
     ```plaintext
     RONTOKEN=your_discord_bot_token_here
     ```

### Installation
1. Navigate to the **Installation** tab in the Developer Portal.
2. Ensure the following:
   - **User Install** is unchecked.
   - **Install Link** is set to `Discord Provider Link` by default.
   - **Default Install Settings** should have `bot` included.
3. Use the provided install link to add the bot to your Discord server.

### How to Monitor Other Tokens
By default, the bot monitors **Ronin (RON)**. To monitor a different cryptocurrency:
1. Visit [CoinGecko](https://www.coingecko.com/).
2. Search for the desired cryptocurrency and note its **id** from the URL. For example, the id for Ethereum is `ethereum`:  
   URL: `https://www.coingecko.com/en/coins/ethereum`  
   **id**: `ethereum`
3. Replace `"ronin"` in the following URLs with the desired token id:
    ```plaintext
    https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=ronin
    https://api.coingecko.com/api/v3/coins/markets?vs_currency=php&ids=ronin
    ```

## Directory Structure
```plaintext
discord-crypto-price-bot
└── RONBot.py
keys
└── pricebot.env (to be created by the user)
```
This directory structure supports having multiple tokens in the `pricebot.env` file. You can safely store token details for different cryptocurrencies in this file. Since the `keys` directory is located outside of the repository, the `pricebot.env` file will not be included in any commits, ensuring that sensitive information like bot tokens remains secure.

## Directory Structure (.env within project directory)
**IMPORTANT**: Make sure to include `pricebot.env` in your `.gitignore` file to prevent it from being committed to the repository
```plaintext
discord-crypto-price-bot
└── RONBot.py
└── pricebot.env (to be created by the user)
```
If you prefer to store the `pricebot.env` file within the project script directory instead of the `keys` folder, modify the following line in `RONBot.py`:
```plaintext
script_dir = os.path.dirname(os.path.abspath(__file__))
keys_folder = "keys"
load_dotenv(os.path.join(script_dir, "..", keys_folder, "pricebot.env"))
```
To something like this:
```plaintext
script_dir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(script_dir, "pricebot.env"))
```
This will load the `pricebot.env` file directly from the project script directory.

## Notes
- Ensure your bot token is kept secure. Never share it publicly.
- The bot updates its activity status approximately every 20 seconds.
- Check the ron.log file for error logs or troubleshooting.
