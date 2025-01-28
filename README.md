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
   
2. Create a `.env` file in that directory with the following content:
    ```
    TOKEN=your_discord_bot_token_here
    ```

3. Install the required dependencies on your desired machine where this script will be deployed:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the bot:
    ```bash
    nohup python3 -u Bot.py > /dev/null 2>&1 &
    ```
    This command runs the bot in the background on Linux. Ensure you're on a Linux-based system to use this setup.

### Additional Notes

To ensure 24/7 deployment, consider hosting this bot on a cloud server, such as AWS, Google Cloud, or DigitalOcean. These platforms allow you to maintain uptime without relying on local machines.

### How to Create a Discord Bot
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click **New Application**, give it a name (e.g., `$RON`), and click **Create**.
3. In the application settings:
   - Customize your bot’s name and upload an app icon (e.g., an image of the **RON** token).
   - Go to the **Bot** tab and click **Add Bot**.
   - Under **Token**, click **Reset Token**, confirm the action, and copy the token.
   - Paste the token into the `.env` file like this:
     ```plaintext
     TOKEN=your_discord_bot_token_here
     ```
     
### Installation
1. Navigate to the **Installation** tab in the Developer Portal.
2. Ensure the following:
   - **User Install** is unchecked.
   - **Install Link** is set to `Discord Provider Link` by default.
   - **Default Install Settings** should have `bot` included.
3. Use the provided install link to add the bot to your Discord server.

### How to Monitor Other Tokens and fiat currency
By default, the bot monitors **Ronin (RON)** and in $ (USD) and ₱ (PHP). To monitor a different cryptocurrency and fiat currency:
1. Visit [CoinGecko](https://www.coingecko.com/).
2. Search for the desired cryptocurrency and note its **id** from the URL. For example, the id for Ethereum is `ethereum`:  
   URL: `https://www.coingecko.com/en/coins/ethereum`  
   **id**: `ethereum`
3. Replace `ronin` in the following URLs with the desired token id:
    ```plaintext
    https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=ronin
    https://api.coingecko.com/api/v3/coins/markets?vs_currency=php&ids=ronin
    ```
4. Replace `usd` or `php` in the following URLs with the [desired fiat currency](https://support.coingecko.com/hc/en-us/articles/4538839949081-Which-currencies-are-supported):
   ```plaintext
    https://api.coingecko.com/api/v3/coins/markets?vs_currency=eur&ids=ronin
    https://api.coingecko.com/api/v3/coins/markets?vs_currency=jpy&ids=ronin
    ```

## Notes
- Ensure your bot token is kept secure. Never share it publicly.
- The bot updates its activity status approximately every 20 seconds.
- Check the token.log file for error logs or troubleshooting.
