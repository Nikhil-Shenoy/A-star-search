# import pdb
import math
from cell import Cell

class BHeap:
	'Binary Min-Heap class implemented using an array. Takes Cell object as parameters'

	def __init__(self,tie_val = 0):
		self.heap = [0]
		self.tie_break = tie_val # 0 = break in favor of larger g, 1 = break in favor of smaller g

	def insert(self,cell):
		self.heap.append(cell)
		self.bubble_up()

	def bubble_up(self):
		# pdb.set_trace()

		start = len(self.heap)-1
		for i in range(start,1,-1):
			parent_index = int(math.floor(i/2))
			parent_f_val = self.heap[parent_index].f_val
			child_f_val = self.heap[i].f_val
			parent_g_val = self.heap[parent_index].g_val
			child_g_val = self.heap[i].g_val

			if child_f_val == parent_f_val:
				if self.tie_break == 1 and child_g_val < parent_g_val:
					# favor smaller g
					# print "Smaller g Tie-break!"
					temp = self.heap[parent_index]
					self.heap[parent_index] = self.heap[i]
					self.heap[i] = temp

				elif self.tie_break == 0 and child_g_val > parent_g_val:
					# favor larger g
					# print "Larger g Tie-break!"
					temp = self.heap[parent_index]
					self.heap[parent_index] = self.heap[i]
					self.heap[i] = temp
			elif child_f_val < parent_f_val:
				temp = self.heap[parent_index]
				self.heap[parent_index] = self.heap[i]
				self.heap[i] = temp

	def bubble_down(self):
		size = len(self.heap)
		end = int(math.floor(size/2))

		for i in range(1,end):
			parent = self.heap[i].f_val
			left = self.heap[2*i].f_val
			right = self.heap[2*i+1].f_val

			if parent > left and parent > right:
				if left <= right:
					temp = self.heap[i]
					self.heap[i] = self.heap[2*i]
					self.heap[2*i] = temp
				else:
					temp = self.heap[i]
					self.heap[i] = self.heap[2*i+1]
					self.heap[2*i+1] = temp
			elif parent < left and parent > right:
				temp = self.heap[i]
				self.heap[i] = self.heap[2*i+1]
				self.heap[2*i+1] = temp
			elif parent > left and parent < right:
				temp = self.heap[i]
				self.heap[i] = self.heap[2*i]
				self.heap[2*i] = temp

	def delete(self):
		min_val = self.heap[1] # Need to think about how to break ties
		self.heap[1] = self.heap[len(self.heap)-1]
		self.heap.pop()
		self.bubble_down()
		return min_val

	def display(self):
		for i in range(1,len(self.heap)):
			print "({0},{1}) -> {2}".format(self.heap[i].x,self.heap[i].y,self.heap[i].f_val)

	def empty(self):
		if len(self.heap) > 1:
			return False
		else:
			return True

	def check_min(self):
		return self.heap[1].f_val

	def contains(self,cell):
		for i in range(1,len(self.heap)):
			if cell.equals(self.heap[i]):
				return True

		return False

if __name__ == '__main__':
	q = BHeap()

	vals = [7,12,1,-2,0,15,4,11,9]
	for val in vals:
		cell = Cell()
		cell.f_val = val

		q.insert(cell)

	# Original 
	q.display()

	# Delete min key
	first = q.delete()
	q.display()

	s = Cell()
	s.f_val = 10
	q.insert(s)
	q.display()



