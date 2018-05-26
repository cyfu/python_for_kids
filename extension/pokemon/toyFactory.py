# !/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import threading

"""
线程，有时被称为轻量级进程(Lightweight Process，LWP），是程序执行流的最小单元。
一个标准的线程由线程ID，当前指令指针(PC），寄存器集合和堆栈组成。
另外，线程是进程中的一个实体，是被系统独立调度和分派的基本单位，线程自己不独立拥有系统资源，
但它可与同属一个进程的其它线程共享该进程所拥有的全部资源。
一个线程可以创建和撤消另一个线程，同一进程中的多个线程之间可以并发执行。
由于线程之间的相互制约，致使线程在运行中呈现出间断性。
线程也有就绪、阻塞和运行三种基本状态。
就绪状态是指线程具备运行的所有条件，逻辑上可以运行，在等待处理机；
运行状态是指线程占有处理机正在运行；
阻塞状态是指线程在等待一个事件（如某个信号量），逻辑上不可执行。
每一个应用程序都至少有一个进程和一个线程。
线程是程序中一个单一的顺序控制流程。
在单个程序中同时运行多个线程完成不同的被划分成一块一块的工作，称为多线程。
"""
NUM = 0


def show():
    global NUM
    NUM += 1
    name = t.getName()
    time.sleep(1)  # 注意，这行语句的位置很重要，必须在NUM被修改后，否则观察不到脏数据的现象。
    print(name, "执行完毕后，NUM的值为： ", NUM)

def entrance():
    for i in range(20):
        t = threading.Thread(target=show)
        t.start()
    print('main thread stop')

"""
信号量(Semaphore)
类名：BoundedSemaphore
这种锁允许一定数量的线程同时更改数据，它不是互斥锁。
比如地铁安检，排队人很多，工作人员只允许一定数量的人进入安检区，其它的人继续排队。
"""


def enter_platform(semaphore, n):
    semaphore.acquire()
    print("Go to plat form number : %s" % n)
    time.sleep(5)
    semaphore.release()


def dragon_diary():
    num = 0
    semaphore = threading.BoundedSemaphore(5)  # 最多允许5个线程同时运行
    for i in range(20):
        t = threading.Thread(target=enter_platform, args=(semaphore,i,))
        t.start()


if __name__ == '__main__':
    #entrance()
    dragon_diary()