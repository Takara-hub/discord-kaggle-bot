# ローカル環境変数を読み込む
from dotenv import load_dotenv
load_dotenv()

import os
import sys
import json
from discordwebhook import Discord
from kaggle import KaggleApi

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
  competition_list = api.competitions_list()
  print(competition_list)
  # discord.post(content="Hello, world.")
else:
  raise Exception(f'そのようなコマンドは存在しません。\n{command_example}')
