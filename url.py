#!pathtopython\python
# -*- coding: cp1251 -*- 

#1. ���������� ������������� ������� �������� � ����� URL.txt (�� ���� ����� ���������� ��� ����������� �������� � ������ �����). ��������� ����� ������� ������ ����� ����� ������� '/' � URL �������.
import re #���������� �����.
try:
	res={}
	pattern="/(.+)/[0-9]{8}.+/"
	preg= re.compile(pattern) #���������� �������
	f = open('urls.txt')
	for line in f:
		key=(preg.findall(line))
		if key :
			res.setdefault(key[0],0)
			res[key[0]]+=1
	print (res)

except Exception as e:
    print("Error: '{}', Args: ".format(e))
