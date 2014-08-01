#!/usr/bin/python
#coding=utf-8

import os
import shutil

def CopytoEachFile():
	DirName = os.listdir(os.getcwd())
	for x in DirName:
		if os.path.isdir(x):
			shutil.copy("PullReader.html", x)
			EditHtml(x)
			pass
		pass
	pass
def EditHtml(DirNameStr):
	FileName = os.listdir(DirNameStr)
	HtmlPath = DirNameStr + "\\PullReader.html"
	fp=open(HtmlPath, 'r')
	TextBuf = fp.read()
	fp.close()
	FlagText = '<!this place go for mark flag!!!>'
	for x in FileName:
		if "jpg" in x or "png" in x:
			# jpgPath = os.getcwd() + "\\" + DirNameStr + "\\" + x;
			# print jpgPath
			jpgPath = x
			ReplaceText = '<img src="'+ jpgPath +'">\n<!this place go for mark flag!!!>'
			TextBuf = TextBuf.replace(FlagText, ReplaceText)
			pass
		pass
	fp = open(HtmlPath, 'w')
	fp.writelines(TextBuf)
	fp.close()
	print "finish!!!"
	pass
CopytoEachFile()