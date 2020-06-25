#coding:UTF-8
import discord
from discord.ext import tasks
from datetime import datetime

TOKEN = "NzI1ODE3OTAxNTQ1OTQ3MTYw.XvUQ-w.20Ka3P-BGJDrBwaY7BP2mwDwbe4" #トークン
CHANNEL_ID = 723804560950296596 #チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '20:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/poll "今日の夜は？" "いつでも良いよ" "やる事終れば" "今日は無理だ"')

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
