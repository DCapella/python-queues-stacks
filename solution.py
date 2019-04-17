#########################
# !!! SOLUTION CODE !!! #
#########################






import sys

class Solution:
    """Stacks and queues"""
    stack = []
    queue = []

    def pushCharacter(self, c):
      """Adds a chracter to the stack list"""
      self.stack.append(c)

    def enqueueCharacter(self, c):
      """Adds a character to the queue list"""
      self.queue.append(c)

    def popCharacter(self):
      """Removes and returns a character from top of stack list"""
      return self.stack.pop()

    def dequeueCharacter(self):
      """Removes and returns the first character of queued list"""
      return self.queue.pop(0)

# read the string s
