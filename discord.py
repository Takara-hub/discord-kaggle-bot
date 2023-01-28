import os
from discordwebhook import Discord
# import kaggle

# ローカル環境変数を読み込む
import setting

DISCORD_WEBHOOK_URL = os.environ['DISCORD_WEBHOOK_URL']
discord = Discord(url=DISCORD_WEBHOOK_URL)
discord.post(content="Hello, world.")
