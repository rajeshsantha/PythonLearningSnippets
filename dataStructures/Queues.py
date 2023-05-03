# First In First Out
# if you want access 3rd item , you need to accee 1st and 2nd items first

# if we have large lists , then reaching for 100000th element will require 99999 elements to be moved in memory
# For those kind of cases, we can use dequeu object

from collections import deque
queue = deque([])
queue.append(1)  # first person came in queue
queue.append(2)  # second one followed first person
queue.append(3)  # one more added in queue

queue.popleft()  # first person got his request served and moved away
print(queue)  # deque([2, 3])

queue.popleft()  # second person got his request served and moved away
print(queue)  # deque([3])


queue.popleft()  # third person got his request served and moved away
print(queue)  # deque([])

# check if queue is empty before you popleft()
if queue:
    queue.popleft()
else:
    print("queue is empty")
