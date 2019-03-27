# Author: Peter

# queue队列
# queue is especially useful in threaded programming when information must be exchanged safely between multiple threads.
# class queue.Queue(maxsize=0) #先入先出
# class queue.LifoQueue(maxsize=0) #last in fisrt out
# class queue.PriorityQueue(maxsize=0) #存储数据时可设置优先级的队列
# Constructor for a priority queue. maxsize is an integer that sets the upperbound limit on the number of items that can be placed in the queue.
# Insertion will block once this size has been reached, until queue items are consumed. If maxsize is less than or equal to zero, the queue size is infinite

# Queue.qsize()
# Queue.empty() #return True if empty
# Queue.full() # return True if full
# Queue.put(item, block=True, timeout=None)

# q = queue.Queue(maxsize=3)
# q.put("d1") 当size数量超过3的时候,此时往里面put的就会出现等待，不能继续往里面添加
# q.get() 没有数据取，去不了，会等待，卡死,可以在之前通过 q.qsize() 做一个判断
# q.get_nowait()  # 没有数据取，可以取数据，但是会报错
# p.get(block=False)  # 使用block=False,没有数据取的时候不会卡死，但是会报错
# p.get(timeout=1)   # 设置超时时间，没有数据取，超时之后才会取，但是会报错
import queue

q = queue.PriorityQueue()

# 值越小，优先级越高
q.put((-1, "chenronghua"))
q.put((3, "hanyang"))
q.put((10, "alex"))
q.put((6, "wangsen"))

print(q.get())
print(q.get())
print(q.get())
print(q.get())

# # LifoQueue   先入后出，也就是后入先出
# q = queue.LifoQueue()
#
# q.put(1)
# q.put(2)
# q.put(3)
# print(q.get())
# print(q.get())
# print(q.get())
