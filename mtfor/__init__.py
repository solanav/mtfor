#!/usr/bin/python3

from threading import Thread
from queue import Queue


def parts_per_thread(list_len, num_threads):
    _parts_per_thread = []

    for i in range(num_threads):
        _parts_per_thread.append(list_len // num_threads)

    remainder = list_len % num_threads

    for i in range(num_threads):
        if remainder == 0:
            break

        _parts_per_thread[i] += 1
        remainder -= 1

    return _parts_per_thread


def divide_list(_list, _parts_per_thread):
    _list_list = []
    for i in range(len(_parts_per_thread)):
        ini = 0 if i == 0 else end
        end = ini + _parts_per_thread[i]
        _list_list.append(_list[ini:end])

    return _list_list


def apply_function(_id, _list, function):
    result = list(map(function, _list))
    return (_id, result)


def mtfor(_list, function, num_threads):
    if (num_threads <= 0):
        raise Exception("Error, number of threads cannot be <= 0")

    list_len = len(_list)

    if (len(_list) <= 0):
        raise Exception("Error, list cannot have length <= 0")

    queue = Queue()

    # Divide the _list
    _parts_per_thread = parts_per_thread(list_len, num_threads)
    _list_list = divide_list(_list, _parts_per_thread)

    # Create threads
    thread_list = []
    _id = 0
    for l in _list_list:
        t = Thread(target=lambda q, l, function: q.put(apply_function(
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