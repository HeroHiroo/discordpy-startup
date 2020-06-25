#coding:UTF-8
import discord
from discord.ext import tasks
from datetime import datetime

TOKEN = "NzI1NDQxNTg5NTY4MDc3ODQ1.XvOy4A.HCk43ngzou71U8rtpD6BoGcGsMI" #トークン
CHANNEL_ID = 723804560950296596 #チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '19:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('/poll "今日の夜は？" "いつでも良いよ" "やる事終れば" "今日は無理だ"')

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
