import msvcrt
import time
from colorama import init
from termcolor import colored
def end():
	print(colored('\nYOU ARE PATHETIC\nSUCKS TO BE YOU!', 'red'))
	exit()
def toprow():
	finish=10
	count=0
	while(1):
		key=ord(msvcrt.getch())
		if key== 224:
			key=ord(msvcrt.getch())
			if key== 77:
				count=count+1
				print "-->",
			if key!=77:
				end()
			if count==finish:
				break
def midrow():
	finish=10
	count=0
	while(1):
		key=ord(msvcrt.getch())
		if key== 224:
			key=ord(msvcrt.getch())
			if key== 80:
				count=count+1
				print "\n                                       |",
			if key!=80:
				end()
			if count==finish:
				break
	if count==finish+1:
		end()
init()
print "Arrow keys control direction\n"
print "OBJECTIVE:\nGO TEN STEPS RIGHT, TEN STEPS DOWN AND TEN STEPS RIGHT AGAIN\n"
s_time=time.time()
toprow()
print "go down",
midrow()
print "go right\n                                      ",
toprow()
time_elapsed=time.time()-s_time
print "\ncongrats you have finished the game"
print "time taken is "+str(time_elapsed)