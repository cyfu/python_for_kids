# coding: utf-8
import time
import _thread as thread
import threading

"""
进程（英语：process），是计算机中已运行程序的实体。进程为曾经是分时系统的基本运作单位。
在面向进程设计的系统（如早期的UNIX，Linux 2.4及更早的版本）中，进程是程序的基本执行实体；
在面向线程设计的系统（如当代多数操作系统、Linux 2.6及更新的版本）中，进程本身不是基本运行单位，而是线程的容器。
程序本身只是指令、数据及其组织形式的描述，进程才是程序（那些指令和数据）的真正运行实例。–维基百科

线程（英语：thread）是操作系统能够进行运算调度的最小单位。它被包含在进程之中，是进程中的实际运作单位。
一条线程指的是进程中一个单一顺序的控制流，一个进程中可以并发多个线程，每条线程并行执行不同的任务。–维基百科
"""

"""
5月1号这一天，麦当劳生意比较火爆，人很多，前台有6个窗口，有4个窗口在工作，随着要吃饭的人变多，麦当劳不得不开放了剩余的两个窗口。
在这里，每一个窗口就是一个进程，处理卖垃圾食品这样一个任务，让系统需要处理更多请求时候，开放窗口就是增加进程来处理需求。
由于是假期，发现即使是6个窗口全开了，排队的客户还是很多，那么，这里是不是没有其它的办法了呢？
效率都是逼出来的，经理发现，客户买完东西，在旁边等，当客户的汉堡（或者其它垃圾食品）准备好了，是由单独的一个人把食品递给客户，
由于这个人需要把准备好的食物分别送给6个不同窗口的客户，所以效率很低。
这时候经理发话了，食品准备好了，直接由窗口的售卖人员把食品给正在等在的客户，这样比较节省时间。
在这里，前台售卖人员的工作就有原来的一项专门售卖商品的工作，变成了两项，就是两个线程。
"""


def ordering(interval):
    cnt = 0
    while cnt < 100:
        print('好了，你订餐成功，订餐号码是:%d号 订餐时间是:%s 请在旁边耐心等待\n\n' % (cnt, time.ctime()))
        time.sleep(interval)
        cnt += 1
    thread.exit_thread()


def notice(interval):
    cnt = 0
    while cnt < 100:
        print('谁的号码是%d,您的餐好了，过来取一下\n' % cnt)
        time.sleep(interval)
        cnt += 1
    thread.exit_thread()


def work():  # Use thread.start_new_thread() to create 2 new threads
    thread.start_new_thread(ordering, (1,))
    thread.start_new_thread(notice, (5,))


def worker(num):
    """
    thread worker function
    :return:
    """
    time.sleep(1)
    print("The num is %d" % num)
    return


def add_thread():
    for i in range(20):
        t = threading.Thread(target=worker, args=(i,), name="t.%d" % i)
        t.start()


if __name__ == '__main__':
    # work()
    add_thread()
