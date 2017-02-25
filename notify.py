#!/usr/bin/env python
# -*- coding:utf-8 -*-
##############################################
#   使用telegram发送通知，去除第三方依赖
#      陈逸少（jmchxy@gmail.com）
#           2016.02.24
##############################################
#from __future__ import unicode_literals
from __future__ import print_function

import sys
import urllib2
import json
import argparse

# 使用telegram发送通知
def Telegram_SendMessage(bot_token, chat_id, message, paser_mode=None):
	apiurl = "https://api.telegram.org/bot{}/sendMessage".format(bot_token)
	data = {}
	data['chat_id'] = chat_id
	data['text'] = message
	if paser_mode is not None:
		data['paser_mode'] = paser_mode
	#发送请求
	try:
		req = urllib2.Request(apiurl)
		req.add_header('Content-Type', 'application/json')
		response = urllib2.urlopen(req, json.dumps(data))
		result = json.loads(response.read())
		#print(result)
		if result["ok"] != True:
			print("\033[31m服务器应答错误")
			return -1
	except ValueError:
		print("\033[31m数据错误: 服务器返回的数据解析错误(非正常json数据)\033[0m")
		return -1
	except urllib2.URLError, err:
		print("\033[31m网络错误: {}\033[0m".format(str(err)))
		return -1
	except BaseException, err:
		print("\033[31m一般性错误: {}\033[0m".format(str(err)))
		return -1
	return 0

##########################################
#  主程序测试入口, 集成通知发布
##########################################
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="使用预定义配置发送通知")
	parser.add_argument('-c', '--config', default="config.json", help="Telegram配置文件路径")
	parser.add_argument('message', nargs='?', help="邮件正文，可选，如果没有则从标准输入读取")
	args = parser.parse_args()

	#从配置文件读取参数，telegram bot token 和 chat_id
	try:
		params = json.load(open(args.config, 'rb'))
	except:
		print("\033[31m**读取配置文件“{}”错误！**\033[0m".format(args.config))
		exit(-1)

	#命令行未指定通知正文，则从标准输入读取
	if args.message == None:
		message = sys.stdin.read()
	else:
		message = args.message

	#发送消息
	result = Telegram_SendMessage(params["bot_token"], params['chat_id'], message)
	exit(result)
