#!pathtopython\python
# -*- coding: cp1251 -*- 

# 2. Какое количество различных слов русского языка можно составить из букв слова «Ростелеком»? Примеры: кот, стекло, лето. Используйте любой словарь русского языка.
baseword="ростелеком"
n=0
with	open('dict_win.txt', 'r') as f:
    for line in f:
        newword = list(line.rstrip())
        x=len(newword)
        if x>1:
            tempword = list(baseword) #копия чтобы из неё можно было выкинуть повторяющиеся символы.
            i=0
            for letter in newword:
                if letter in tempword:
                    tempword.remove(letter)
                    i+=1
                    if i>=x:
                        print("word: {}".format(line))
                        n+=1
			#print ("{} #{}".format(newword,x))
    print(n)
