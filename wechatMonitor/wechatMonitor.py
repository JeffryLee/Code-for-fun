import itchat


class wechatMonitor:
	def __init__(self):
		itchat.auto_login()

	def sendMsg(self, content):
		itchat.send(content, toUserName='filehelper')