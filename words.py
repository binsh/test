#!pathtopython\python
# -*- coding: cp1251 -*- 

# 2. ����� ���������� ��������� ���� �������� ����� ����� ��������� �� ���� ����� �����������? �������: ���, ������, ����. ����������� ����� ������� �������� �����.
baseword="����������"
n=0
with	open('dict_win.txt', 'r') as f:
    for line in f:
        newword = list(line.rstrip())
        x=len(newword)
        if x>1:
            tempword = list(baseword) #����� ����� �� �� ����� ���� �������� ������������� �������.
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
