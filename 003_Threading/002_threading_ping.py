#!/usr/bin/env python3
# -*- coding: UTF-8 -*-



'''

Thread IP checker  , sending multiple pings on the same time  192.168.1.0-10
   Linux version

import threading

function th1 als thread th anlegen
	th1 = threading.Thread(target=th1)

start  thread 'th1' 
	th.start()

	th1.is_alive()
	threading.active_count()

Wait for ending of the thread 'th1'
	th1.join()


'''



##############################################################################################
#
# 				import modules
#
##############################################################################################

import os
import threading



##############################################################################################
#
# 				functions
#
##############################################################################################

def ip_check(ip):
	global result
	print (f"thread: ping {ip} ")
	ping_out = os.system("ping -q -c1 "+ip+' > /dev/null')    # Linux ping

	if ping_out == 0:
		print (f"...end thread pinging {ip}, result : {ip} is reachable")
	else:
		print (f"...end thread pinging {ip}, result : {ip} is unreachable")
	return(result)

  




##############################################################################################
#
# 				Main
#
##############################################################################################

if __name__== "__main__":
	os.system('clear')

	# threads starten
	result = []
	for suffix in range(2,5):
		ip = "192.168.1."+str(suffix)
		th = threading.Thread(target=ip_check, args=(ip,))
		th.start()
	print('all Threads are running')

