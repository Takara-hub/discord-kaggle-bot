# ローカル環境変数を読み込む
from dotenv import load_dotenv
load_dotenv()

import os
import sys
import json
from discordwebhook import Discord
from kaggle import KaggleApi
from datetime import datetime, timedelta

# コマンドエラー時に表示するコマンド例を作成
command_json = json.load(open('command.json', 'r'))
command_example = f"{command_json['example']}\ncommand list:"
for command in command_json['command_list']:
  command_example += f'\n{command}'

# コマンドライン引数を取得
if len(sys.argv) < 2:
  raise Exception(f'コマンドを記述してください。\n{command_example}')

command = sys.argv[1]

# kaggle認証
api = KaggleApi()
api.authenticate()

if command == 'competitions_list':
  # discordの設定
  DISCORD_WEBHOOK_URL_COMPETITION_LIST = os.environ['DISCORD_WEBHOOK_URL_COMPETITION_LIST']
  discord = Discord(url=DISCORD_WEBHOOK_URL_COMPETITION_LIST)
  competitions_list = api.competitions_list()
  discord.post(content='開催中のコンペ')
  for competition in competitions_list:
    # 常設コンペは除外
    if competition.hasCategory and competition.category == 'Getting Started':
     continue
    send_message = f'\nタイトル：{competition.title if competition.hasTitle else "なし"}'
    send_message += f'\nURL：{competition.ref}'
    send_message += f'\n賞金：{competition.reward if competition.hasReward else "なし"}'
    send_message += f'\n〆切：{competition.deadline}'
    discord.post(content=send_message)
elif command == 'new_competition':
  # discordの設定
  DISCORD_WEBHOOK_URL_COMPETITION_LIST = os.environ['DISCORD_WEBHOOK_URL_COMPETITION_LIST']
  discord = Discord(url=DISCORD_WEBHOOK_URL_COMPETITION_LIST)
  competitions_list = api.competitions_list()
  previous_date = datetime.now() - timedelta(days=5)
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
else:
  raise Exception(f'そのようなコマンドは存在しません。\n{command_example}')
