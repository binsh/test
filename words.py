#!pathtopython\python
# -*- coding: cp1251 -*- 

# 2. ����� ���������� ��������� ���� �������� ����� ����� ��������� �� ���� ����� �����������? �������: ���, ������, ����. ����������� ����� ������� �������� �����.
import copy
baseword= list("����������")
try:
	n=0
	f = open('dict_win.txt')
	for line in f:
		newword= list(line.rstrip())
		x=len(newword)
		if x>1:
			tempword=copy.copy(baseword) #����� ����� �� �� ����� ���� �������� ������������� �������.
			i=0
			www=""
			for letter in newword:
				if letter in tempword:
					tempword.remove(letter) # ���������� ������������� �������
					i+=1
					#print ("{} of {} #{} in {}".format(letter, newword,i,x))
			if i>=x:
				print("word: {}".format(line))
				n+=1
			#print ("{} #{}".format(newword,x))
	print(n)
except Exception as e:
    print("Error: '{}', Args: ".format(e))
