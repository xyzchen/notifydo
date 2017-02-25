# notifydo
对需要长时间的命令在命令执行完成后发送通知给自己

# 安装

git clone https://github.com/xyzchen/notifydo.git

cd notifydo

sudo ./install.sh telegram_bot_token chat_id

安装脚本将2个文件拷贝到 ／usr／local/bin／， 并在 ~ 下生成配置文件，配置文件如下：

{
	"bot_token": "your telegram bot token",
	"chat_id"  : "your chat id"
}

#用法
notifydo cmd params ...
