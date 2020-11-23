#!/usr/bin/env python3
# -*- coding: UTF-8 -*-



'''

Thread 101

import threading

function th1 als thread th anlegen
	th = threading.Thread(target=th1)

thread th starten
	th.start())


	th.is_alive()
	threading.active_count()

Auf Beendigung eines Threads warten bevor es weiter geht
	th.join()


'''



##############################################################################################
#
# 				import modules
#
##############################################################################################

import time
from random import randint
import threading



##############################################################################################
#
# 				functions
#
##############################################################################################

def th1():
	print('th1: thread started, waiting 5 secs')
	time.sleep(5)
	print('th1: thread finished, time over')
	return()

def example_01():
	print('example_01 : Threads running: ', threading.active_count())
	th = threading.Thread(target=th1)
	print('example_01 : th1 Thread status:', th.is_alive())
	print('example_01 : Thread wird gestartet')
	th.start()
	print('example_01 : th1 Thread status:', th.is_alive())
	
	print('example_01 : gruss aus der function example_01')
	return()




##############################################################################################
#
# 				Main
#
##############################################################################################

if __name__== "__main__":
	example_01()



