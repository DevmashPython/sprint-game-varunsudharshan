import msvcrt
import time
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
			if count==finish:
				break
print "press enter key to get started!"
raw_input()
s_time=time.time()
toprow()
print "go down",
midrow()
print "go right\n                                      ",
toprow()
time_elapsed=time.time()-s_time
print "\ncongrats you have finished the game"
print "time taken is "+str(time_elapsed)