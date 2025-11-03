#создание меню

def textMenu():
	print("Нажмите 1 для ввода исходных данных");
	print("Нажмите 2 для вывода статических коеффициентов передачи");
	print("                     и постоянных времени");
	print("Нажмите 3 для вывода корней полиномов");
	print("Нажмите 4 для анализа устойчивости по Гурвицу");
	print("Нажмите 5 для построения графиков переходных характеристик");
	print("Нажмите 0 для выхода");

def retMenusPoint(): 
	textMenu();
	menusPoint = input();
	if menusPoint == '1':
		return 0x1;
	elif menusPoint == '2':
		return 0x2;
	elif menusPoint == '3':
		return 0x3;
	elif menusPoint == '4':
		return 0x4;
	elif menusPoint == '5':
		return 0x5;
	elif menusPoint == '0':
		return 0x0;
	else: return 0xff;

