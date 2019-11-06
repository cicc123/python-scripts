import _thread,time

def action(i):
	time.sleep(1)
	print(i**32)
class Power:
	def __init__(self,i):
		self.i = i
	def action(self):
		time.sleep(1)
		print(self.i**32)
_thread.start_new_thread(action,(2,))
_thread.start_new_thread((lambda: action(2)),())
obj = Power(2)
_thread.start_new_thread(obj.action,())

time.sleep(1.1)
print('end')
