# import pdb
import math

class BHeap:
	'Binary Min-Heap class implemented using an array'

	def __init__(self):
		self.heap = [0]

	def insert(self,val):
		self.heap.append(val)
		self.heapify()

	def heapify(self):
		# pdb.set_trace()
		start = int(math.floor(len(self.heap) / 2)) -1
		for i in range(len(self.heap)-1,1,-1):
			if self.heap[i] < self.heap[i/2]:
				temp = self.heap[i/2]
				self.heap[i/2] = self.heap[i]
				self.heap[i] = temp


	def pop(self):
		min_val = self.heap[1]
		self.heap[1] = self.heap[len(self.heap)-1]
		self.heap.pop()
		self.heapify()
		return min_val

	def display(self):
		# self.heapify()
		print self.heap

if __name__ == '__main__':
	q = BHeap()

	q.insert(7)
	q.insert(12)
	q.insert(1)
	q.insert(-2)
	q.insert(0)
	q.insert(15)
	q.insert(4)
	q.insert(11)
	q.insert(9)
	q.display()

	first = q.pop()
	q.display()

	q.insert(-10)
	q.display()



