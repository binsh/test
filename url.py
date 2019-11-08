#!pathtopython\python
# -*- coding: cp1251 -*- 

#1. Посчитайте распределение тематик новостей в файле URL.txt (то есть какое количество раз встречается страница с каждой темой). Тематикой можно считать первое слово между знаками '/' в URL новости.
import re #регулярные выраж.
try:
	res={}
	pattern="/(.+)/[0-9]{8}.+/"
	preg= re.compile(pattern) #компиляция шаблона
	f = open('urls.txt')
	for line in f:
		key=(preg.findall(line))
		if key :
			res.setdefault(key[0],0)
			res[key[0]]+=1
	print (res)

except Exception as e:
    print("Error: '{}', Args: ".format(e))
