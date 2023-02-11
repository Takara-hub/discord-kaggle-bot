# ローカル環境変数を読み込む
from dotenv import load_dotenv
load_dotenv()

import os
from discordwebhook import Discord
from kaggle import KaggleApi
from datetime import datetime, timedelta

# kaggle認証
api = KaggleApi()
api.authenticate()

def new_competition():
  # discordの設定
  DISCORD_WEBHOOK_URL_COMPETITION_LIST = os.environ['DISCORD_WEBHOOK_URL_COMPETITION_LIST']
  discord = Discord(url=DISCORD_WEBHOOK_URL_COMPETITION_LIST)
  competitions_list = api.competitions_list()
  previous_date = datetime.now() - timedelta(days=1)
  current_date = datetime.now()
  # 本日開催のもののみを送信
  for competition in competitions_list:
    if not (previous_date < competition.enabledDate and competition.enabledDate <= current_date):
     continue
    send_message = f'\nタイトル：{competition.title if competition.hasTitle else "なし"}'
    send_message += f'\nURL：{competition.ref}'
    send_message += f'\n賞金：{competition.reward if competition.hasReward else "なし"}'
    send_message += f'\n〆切：{competition.deadline}'
    discord.post(content=send_message)
