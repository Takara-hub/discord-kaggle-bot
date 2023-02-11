# discord-kaggle-bot

# 環境構築
## パッケージのインストール
``` 
pip install -r requirements.txt
```
## 環境変数のサンプル
フォルダ直下に`.env`ファイルを作成後以下のサンプルを参考に編集
```
# discord
DISCORD_WEBHOOK_URL_COMPETITION_LIST=<competition_list用のwebhookのurl>

# kaggle
KAGGLE_USERNAME=<kaggleのユーザー名>
KAGGLE_KEY=<kaggleのAPIキー>
```

# 実行
``` 
python3 discord.py コマンド
```

# 本番環境
[Azure Functions の timerTrigger](TimerTrigger/readme.md) を使用

