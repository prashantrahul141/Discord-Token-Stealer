<h1 align="center">Discord Token Stealer</h1>
<p align="center">
A discord bot which can steal discord tokens. For educational purposes only.
</p>

<h2>Usage</h2>

1. Clone the repository / or download the source code.
```sh
git clone https://github.com/prashantrahul141/Discord-Token-Stealer
```

2. Install python dependencies from the `requirements.txt` file.
```sh
pip install -r requirements.txt
```

3. Create a `.env` file with the following env vars.
```sh
DISCORD_BOT_TOKEN="Your Discord Bot Token"
```

4. Install firefox<br>
The script uses firefox browser to handle interactions with discord.

5. Run the script
```sh
python main.py
```

Whenever someone types `:verify` in the chat. The bot will create a browser instance (firefox) and take the qr code from discord's login page. The bot will then send the victim a message to verify their account by scanning the qr code using discord mobile. Once scanned, the bot will retrive the token from session storage, check the token against discord, if the token is real, it will save the token in a `tokens.json` file.


<h2>Warning</h2>
This project is for educational purposes only, I do not take any responsibilty if you break discord's TOS without their and someone's consent.