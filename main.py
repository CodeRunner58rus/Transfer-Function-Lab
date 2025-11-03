#!/usr/bin/env python3
#
#  main.py
#  
#  Copyright 2025 Unknown <ZaharovNS@ZaharovComp>
#  
#  


import sys
import main_menu
import data

def main():
	subProgramNum = -1;
	while subProgramNum != 0x0:
		subProgramNum = -1;
		subProgramNum = main_menu.retMenusPoint();
		if subProgramNum == 0x1:
			data.inputPolinomA();
			print(data.a)
			data.inputPolinomB1();
			print(data.b1)
			data.inputPolinomB2();
			print(data.b2)
			data.inputPolinomB3();
			print(data.b3)
			data.inputPolinomB4();
			print(data.b4)
		elif subProgramNum == 0x2:
			data.solveK();
			print(f"Коэффициенты К {data.K}");
			data.solveTa();
			print(f"Постоянные времени а {data.Ta}");
			data.solveTb1();
			print(f"Постоянные времени b1 {data.Tb1}");
			data.solveTb2();
			print(f"Постоянные времени b2 {data.Tb2}");
			data.solveTb3();
			print(f"Постоянные времени b3 {data.Tb3}");
			data.solveTb4();
			print(f"Постоянные времени b4 {data.Tb4}");
			input();
		elif subProgramNum == 0x3:
			data.solveRootPolinomA();
			print(f"Корни полинома а {data.rootsA}");
			data.solveRootPolinomB1();
			print(f"Корни полинома b1 {data.rootsB1}");
			data.solveRootPolinomB2();
			print(f"Корни полинома b2 {data.rootsB2}");
			data.solveRootPolinomB3();
			print(f"Корни полинома b3 {data.rootsB3}");
			data.solveRootPolinomB4();
			print(f"Корни полинома b4 {data.rootsB4}");
			input();
		elif subProgramNum == 0x4:
			pass;
		elif subProgramNum == 0x5:
			pass;  

if __name__ == '__main__':
	main()
