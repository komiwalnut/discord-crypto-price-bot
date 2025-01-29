# discord-crypto-price-bot

<image src=./images/price-bot.png/> <image src=./images/price-bot2.png/>

A Discord bot that displays the current price of your preferred cryptocurrency token in USD and PHP, along with the 24-hour price change percentage, as its activity status.

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
    CRYPTO=your_crypto_token_to_monitor_here
    FIAT1=your_desired_fiat_currency
    FIAT2=your_other_desired_fiat_currency
    TOKEN=your_discord_bot_token_here
    ```

3. Install Python 3 and venv (if not already installed):
   ```bash
    sudo apt install python3 python3-venv
    ```

4. Create and activate a virtual environment:
   ```bash
    python3 -m venv price-bot-venv
    source price-bot-venv/bin/activate
    ```

5. Install the required dependencies inside the virtual environment:
    ```bash
    pip install -r requirements.txt
    ```

6. Run the bot:
    ```bash
    nohup python3 -u Bot.py > /dev/null 2>&1 &
    ```
    This command runs the bot in the background on Linux. Ensure you're on a Linux-based system to use this setup.

7. It should give you a similar message with the PID of the script (ex. 43945):
    ```bash
    [1] 43945
    ```
    Note: To stop the bot, just type `kill [PID]`. If you don't know the PID then do `ps auf | grep .py` and it should give you a similar list where 43934 is the PID:
    ```bash
    ubuntu     43945  0.3  4.1 269948 40408 pts/0    Sl   22:13   0:00 python3 -u Bot.py
    ```

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
To monitor a different cryptocurrency and fiat currency:
1. Visit [CoinGecko](https://www.coingecko.com/).
2. Search for the desired cryptocurrency and note its **id** from the URL. For example, the id for Ethereum is `ethereum`:  
   URL: `https://www.coingecko.com/en/coins/ethereum`  
   **id**: `ethereum`
3. Replace `CRYPTO` in the `.env` file:
    ```plaintext
    CRYPTO=ethereum
    ```
    Note: If it's fetching the wrong crypto token or wrong price then message me on Discord because this is an old version of fetching prices via CoinGecko.
    - ID: 904940122468909138
    - Username: komiwalnut

4. Replace `FIAT1` and `FIAT2` in the `.env` file with your [desired fiat currency](https://support.coingecko.com/hc/en-us/articles/4538839949081-Which-currencies-are-supported):
    ```plaintext
    FIAT1=usd
    FIAT2=php
    ```

## Notes
- Ensure your bot token is kept secure. Never share it publicly.
- The bot updates its activity status approximately every 20 seconds.
- Check the token.log file for error logs or troubleshooting.
