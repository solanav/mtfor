#!/usr/bin/python3

from threading import Thread
from queue import Queue


def __parts_per_thread(list_len, num_threads):
    ppt = []

    for i in range(num_threads):
        ppt.append(list_len // num_threads)

    remainder = list_len % num_threads

    for i in range(num_threads):
        if remainder == 0:
            break

        ppt[i] += 1
        remainder -= 1

    return ppt


def __divide_list(user_list, ppt):
    _list_list = []
    for i in range(len(ppt)):
        ini = 0 if i == 0 else end
        end = ini + ppt[i]
        _list_list.append(user_list[ini:end])

    return _list_list


def __apply_function(_id, user_list, function):
    result = list(map(function, user_list))
    return (_id, result)


def mtfor(user_list, function, num_threads):
    if (num_threads <= 0):
        raise Exception("Error, number of threads cannot be <= 0")

    list_len = len(user_list)

    if (len(user_list) <= 0):
        raise Exception("Error, list cannot have length <= 0")

    queue = Queue()

    # Divide the user_list
    ppt = __parts_per_thread(list_len, num_threads)
    _list_list = __divide_list(user_list, ppt)

    # Create threads
    thread_list = []
    _id = 0
    for l in _list_list:
        t = Thread(target=lambda q, l, function: q.put(__apply_function(
            _id, l, function)), args=(queue, l, function,), daemon=True)
        t.start()
        thread_list.append(t)
        _id += 1

    # Wait for threads to end
    for t in thread_list:
        t.join()

    # Get results
    meta_result = []
    while not queue.empty():
        meta_result.append(queue.get())

    # Sort the list with meta info
    meta_result.sort(key=lambda x: x[0])

    # Remove meta and flatten the list
    complex_result = list(map(lambda x: x[1], meta_result))
    result = []
    for l in complex_result:
        result = result + l

    return result