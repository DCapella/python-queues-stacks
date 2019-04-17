# Python Queues and Stacks

### [HackerRank](www.hackerrank.com)

> Write the following declarations and implementations:
> Two instance variables: one for your stack, and one for your queue.
> A void pushCharacter(char ch) method that pushes a character onto a stack.
> A void enqueueCharacter(char ch) method that enqueues a character in the queue instance variable.
> A char popCharacter() method that pops and returns the character at the top of the stack instance variable.
> A char dequeueCharacter() method that dequeues and returns the first character in the queue instance variable.

## Code

<br/><br/>

### Two instance variables

<br/><br/>

```python
class Solution:
    """Stacks and queues"""
    stack = []
    queue = []
```

<br/><br/>

### pushCharacter method that adds to stack

<br/><br/>

```python
def pushCharacter(self, c):
      """Adds a chracter to the stack list"""
      self.stack.append(c)
```

<br/><br/>

### enqueueCharacter method that adds to queue

<br/><br/>

```python
def enqueueCharacter(self, c):
      """Adds a character to the queue list"""
      self.queue.append(c)
```

<br/><br/>

### popCharacter that returns pop from stack

<br/><br/>

```python
def popCharacter(self):
      """Removes and returns a character from top of stack list"""
      return self.stack.pop()
```

<br/><br/>

### dequeueCharacter method that pops first from queue

<br/><br/>

```python
def dequeueCharacter(self):
      """Removes and returns the first character of queued list"""
      return self.queue.pop(0)
```

<br/><br/>

## Final Code

<br/><br/>

```python
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
```

<br/><br/>

## Conclusion

<br/><br/>

Quick, simple, and fun.
