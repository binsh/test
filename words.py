#!pathtopython\python
# -*- coding: cp1251 -*- 

# 2. Какое количество различных слов русского языка можно составить из букв слова «Ростелеком»? Примеры: кот, стекло, лето. Используйте любой словарь русского языка.
import copy
baseword= list("ростелеком")
try:
	n=0
	f = open('dict_win.txt')
	for line in f:
		newword= list(line.rstrip())
		x=len(newword)
		if x>1:
			tempword=copy.copy(baseword) #копия чтобы из неё можно было выкинуть повторяющиеся символы.
			i=0
			www=""
			for letter in newword:
				if letter in tempword:
					tempword.remove(letter) # выкидываем повторяющиеся символы
					i+=1
					#print ("{} of {} #{} in {}".format(letter, newword,i,x))
			if i>=x:
				print("word: {}".format(line))
				n+=1
			#print ("{} #{}".format(newword,x))
	print(n)
except Exception as e:
    print("Error: '{}', Args: ".format(e))
