from collections import deque
import threading


def main():
    n = 10  # max bound
    q = deque([], maxlen=n)
    s_pop = threading.Semaphore(0)
    s_push = threading.Semaphore(n)


def producer(q: deque, s_pop: threading.Semaphore, s_push: threading.Semaphore):
    while True:
    # produce item

    # check queue is not full
        # if acquire is ok push : append the item in queue

        # append the item to queue(acquire)

    # append the item value in to queue(Q.push(I))

    # release the pop semaphore for consumer


def consumer():
    while True:
    # check the queue is not empty
        #if successful acquire in pop semaphore

        # pop the item from queue(pop)

    #pop the item value from queue(q.pop())

    #release the push semaphore for producer

    #consume the value which is popped from queue

if __name__ == '__main__':
    main()
