"""
Multiprocessing using python
"""
from multiprocessing import Process


def print_func(value='default_value'):
    print(f"This function print {value}")


if __name__ == '__main__':
    names = ['chetan', 'vinay', 'parth']
    procs = []
    proc = Process(target=print_func)  # instantiating without any argument
    procs.append(proc)
    proc.start()

    # instantiating process with arguments
    for name in names:
        # print(name)
        proc = Process(target=print_func, args=(name,))
        procs.append(proc)
        proc.start()

    # complete the processes
    for proc in procs:
        proc.join()


"""
Output:
This function print default_value
This function print chetan
This function print vinay
This function print parth
"""