import numpy as np
#Количество элементов полинома
count = 4;
#Полином а (знаменатель)
a = None;
rootsA = None;
#Полиномы b (числители)
b1 = None;
rootsB1 = None;
b2 = None;
rootsB2 = None;
b3 = None;
rootsB3 = None;
b4 = None;
rootsB3 = None;

#дельта для Гурвица
delta1 = None
delta2 = None
delta3 = None
Y1 = None
Y2 = None
Y3 = None
#Статические коэффиценты передачи
K = None;

#Постоянные времени
Ta = None;
Tb1 = None;
Tb2 = None;
Tb3 = None;
Tb4 = None;

def clearData():
	global a, b1, b2, b3, b4, K, Ta, Tb1, Tb2, Tb3, Tb4
	global rootsA, rootsB1, rootsB2, rootsB3, rootsB4
	global delta1, delta2, delta3, Y1, Y2, Y3 
	a = None
	b1 = None;
	b2 = None;
	b3 = None;
	b4 = None;
	K = None
	Ta = None;
	Tb1 = None;
	Tb2 = None;
	Tb3 = None;
	Tb4 = None;
	rootsA = None
	rootsB1 = None;
	rootsB2 = None;
	rootsB3 = None;
	rootsB4 = None;
	delta1 = None;
	delta2 = None;
	delta3 = None;
	Y1 = None;
	Y2 = None;
	Y2 = None;

def inputPolinomA():
	global a
	a = [];
	print("Введите элементы полинома a");
	for i in range(count):
		a.append(float(input(f"Введите a{i}:")));

def inputPolinomB1():
	global b1
	b1 = [];
	print("Введите элементы полинома b1");
	for i in range(count):
		b1.append(float(input(f"Введите b1{i}:")));
def inputPolinomB2():
	global b2
	b2 = [];
	print("Введите элементы полинома b2");
	for i in range(count):
		b2.append(float(input(f"Введите b2{i}:")));
def inputPolinomB3():
	global b3
	b3 = [];
	print("Введите элементы полинома b3");
	for i in range(count):
		b3.append(float(input(f"Введите b3{i}:")));
def inputPolinomB4():
	global b4
	b4 = [];
	print("Введите элементы полинома b4");
	for i in range(count):
		b4.append(float(input(f"Введите b4{i}:")));

def solveK():
	global K
	K = []
	K.append(b1[0]/a[0]);
	K.append(b2[0]/a[0]);
	K.append(b3[0]/a[0]);
	K.append(b4[0]/a[0]);

def solveTa():
	global Ta
	Ta = []
	for i in range(count-1):
		Ta.append(a[i+1]/a[0])
	
def solveTb1():
	global Tb1
	Tb1 = []
	for i in range(count-1):
		Tb1.append(b1[i+1]/b1[0])	
	
def solveTb2():
	global Tb2
	Tb2 = []
	for i in range(count-1):
		Tb2.append(b2[i+1]/b2[0])	
	
def solveTb3():
	global Tb3
	Tb3 = []
	for i in range(count-1):
		Tb3.append(b3[i+1]/b3[0])	
	
def solveTb4():
	global Tb4
	Tb4 = []
	for i in range(count-1):
		Tb4.append(b4[i+1]/b4[0])	

def solveRootPolinomA():
	global rootsA
	rootsA = []
	rootsA = np.roots(a[::-1]).tolist()

def solveRootPolinomB1():
	global rootsB1
	rootsB1 = []
	rootsB1 = np.roots(b1[::-1]).tolist()

def solveRootPolinomB2():
	global rootsB2
	rootsB2 = []
	rootsB2 = np.roots(b2[::-1]).tolist()

def solveRootPolinomB3():
	global rootsB3
	rootsB3 = []
	rootsB3 = np.roots(b3[::-1]).tolist()

def solveRootPolinomB4():
	global rootsB4
	rootsB4 = []
	rootsB4 = np.roots(b4[::-1]).tolist()

def stabilityHurwitz():
	global delta1, delta2, delta3
	global Y1, Y2, Y3 
	#TODO ДОДЕЛАТЬ
	pass
