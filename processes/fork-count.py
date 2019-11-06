import os,time

def counter(count):
	for i in range(count):
		time.sleep(1)
#		print('[%s] => %s' % (os.getpid(),i))
#	os._exit(0)
	print('%f    Main process  %d===>%d exiting.' % (time.time(),os.getpid(),pid))
for i in range(1):
	pid = os.fork()
	if pid != 0:
		print('%f    Process %d spawned' % (time.time(),pid))
	else:
		counter(5)
#print('%f    Main process  %d===>%d exiting.' % (time.time(),os.getpid(),pid))
