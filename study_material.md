Brittany’s Repo
https://github.com/brittanyrjones/cs-practice
25-Sep-2020
*Skip Week 4
Algorithms I, Week 5 - Hash Tables 
*skip Symbol Table Applications
Homework Array Problems
LeetCode Array Problems 11, 15, 16, 18, 26, 27, 31
Mock interview practice
http://pramp.com/
Coding Mock Interview
https://leetcode.com/problems/pascals-triangle/
Notes
Started at 2:20pm

numRows = 1, return row1 [1]
numRows = 2, return row1 + [1, 1]
“ = 3,return row1, row2, [1, row2[0]+row2[1], 1]
“ = 4,return row1, row2, row3, [1, row3[0]+row3[1], row3[1]+row3[2], 1]
“ = 5,return row1, row2, row3, row4, [1, row4[0]+row4[1], row4[1]+row4[2], row4[2]+row4[3], 1]

Function generate(numRows) -> List(List())
# firstRow = [1]
# if (numRows == 0) return nothing
# if (numRows == 1) return firstRow
# result = list[numRows];
# result[0] = firstRow

# for(int i = 1; i < numRows; i++)
#	each new row’s size is the same as the index of the row
#	newRow = list[i];
#	for (int j = 0; j <= i; j++)
#		first and last element of row is always 1
# 		if (j == 0 || j == i-1) newRow[j] = 1
#		newRow[j] = result[i-1][j] + result[i-1][j-1]
#	result[i] = newRow
# return result 


8-Aug-2020
Algorithms I, Week 4 - Binary Search Trees (2nd part of Elementary Symbol Tables)
Memorize the following:
https://github.com/jguamie/algorithms/blob/master/notes/binary-trees.md
After BST Coding Problems, Re-review Algorithms I, Week 4 - Priority Queue
Coding Problems
Stanford Binary Tree Problems
https://leetcode.com/problems/binary-tree-inorder-traversal/ 
Do both recursive and iterative approaches.
https://leetcode.com/problems/validate-binary-search-tree/
https://leetcode.com/problems/unique-binary-search-trees/
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
https://leetcode.com/problems/delete-nodes-and-return-forest/
https://leetcode.com/problems/flip-equivalent-binary-trees/
31-Jul-2020
Algorithms I, Week 1 - Analysis of Algorithms
* Binary Search
* Big O Performance
Algorithms I, Week 3 - Merge and Quick Sort
Algorithms I, Week 4 - Priority Queue
Memorize the following algos:
https://github.com/jguamie/algorithms/blob/master/notes/sorts.md
Coding Problems
https://leetcode.com/problems/two-sum/
https://leetcode.com/problems/3sum/
https://leetcode.com/problems/3sum-closest/
https://leetcode.com/problems/4sum/
Watch the following
Solve '2Sum' Coding/Engineering Interview - How to: Work at Google (YouTube)
Priority Queue Coding Problems
Kth Largest Element in an Array
class Solution {
    public int findKthLargest(int[] nums, int k) {
        // init heap 'the smallest element first'
        PriorityQueue<Integer> heap =
            new PriorityQueue<Integer>((n1, n2) -> n1 - n2);

        // keep k largest elements in the heap
        for (int n: nums) {
          heap.add(n);
          if (heap.size() > k)
            heap.poll();
        }

        // output
        return heap.poll();        
  }
}



Merge k Sorted Lists

LeetCode Solution
from Queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next


Priority Queue Notes
K lists N length of the lists
[1, 2, 4, 10]
[2, 2, 7, 11]
[2, 2, 5, 12]
->PQ<MinHeap>(1, 12, 2, 2, 4, 11, 2, 10)
while(!PQ.isEmpty())
{ 
minVal = PQ.pop()
LL.add(minVal)
}

Return LL

O(k*log m)

For binary trees:
Class Node {
	int Value;
	Node left;
	Node right;
}

Node root; // sometimes called head.

// Find if the number 12 is in the tree
If (root.value != 12) {
Check root.left and root.right;
For priority queues aka binary heap:
[root, root.left, root.right, root.left.left, root.left.right, root.right.left, root.right.right...]
[1, 2, 3, 4, 5...]
 2, 3
// children of node at k are 2k and 2k+1

24-Jul-2020
Algorithms I, Week 2 - Stacks and Queues only
Notes
Linked List problems are important because they are fundamental to comfortably working with Binary Trees. After that, Binary Trees are fundamental to doing Graphs.
Coding Problems
Stanford Linked List Problems
Implement Stack Using Queues
from queue import Queue
 class Stack:
    
   def __init__(self):
        
       self.q1 = Queue()
       self.q2 = Queue() 
             
       self.curr_size = 0
    def push(self, x):
       self.curr_size += 1
        # Push x first in empty q2 
       self.q2.put(x) 
        # Push all the remaining 
       # elements in q1 to q2. 
       while (not self.q1.empty()):
           self.q2.put(self.q1.queue[0]) 
           self.q1.get()
        self.q = self.q1 
       self.q1 = self.q2 
       self.q2 = self.q
    def pop(self):
        # if no elements are there in q1 
       if (self.q1.empty()): 
           return
       self.q1.get() 
       self.curr_size -= 1
    def top(self):
       if (self.q1.empty()):
           return -1
       return self.q1.queue[0]
    def size(self):
       return self.curr_size
 if __name__ == '__main__':
   s = Stack()
   s.push(1) 
   s.push(2) 
   s.push(3) 
    print(s.size())
   print(s.top())
 
 
   s.pop() 
   print(s.top())
   print("top round 2")
   s.pop() 
   print(s.top()) 
    print(s.size())

Implement Queue Using Stacks
class Queue: 
   def __init__(self):
       self.stack_1 = []
       self.stack_2 = []
   def enQueue(self, x):
        
       while len(self.stack_1) != 0: 
           self.stack_2.append(self.stack_1[-1]) 
           self.stack_1.pop()
        # Push item into self.stack_1 
       self.stack_1.append(x) 
        # Push everything back to stack_1 
       while len(self.stack_2) != 0: 
           self.stack_1.append(self.stack_2[-1]) 
           self.stack_2.pop()
    # Dequeue an item from the queue 
   def deQueue(self):
        
           # if first stack is empty 
       if len(self.stack_1) == 0: 
           print("Queue is Empty")
    
       # Return top of self.stack_1 
       x = self.stack_1[-1] 
       self.stack_1.pop() 
       return x
 # Driver code 
if __name__ == '__main__':
   q = Queue()
   q.enQueue(1) 
   q.enQueue(2) 
   q.enQueue(3) 
    print(q.deQueue())
   print(q.deQueue())
   print(q.deQueue())


