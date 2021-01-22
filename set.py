#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 
# author  Se0x
#

file_list = [] #创建一个空的列表，用于接收
def quchong_file():
	file_01 = "1.txt"    #需要去重的文件
	with open(file_01, "r" , encoding="utf-8") as f :  #打开文件			
		for file_02 in f.readlines():
			file_list.append(file_02)
		out_file = set(file_list)     #set()函数自动过滤重复函数
		last_out_file = list(out_file)
		for out in last_out_file:
			with open("result.txt", "a+", encoding="utf-8") as f:
				f.write(out)
				print(out)
if __name__ == '__main__':
	quchong_file()
