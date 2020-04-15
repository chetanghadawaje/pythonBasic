from contextlib import contextmanager


@contextmanager
def tempFunction(name):
    try:
        print("init")
        yield
        print("Start")
    finally:
        print("end")


with tempFunction("abc"):
    print("Done")

"""
Output:-
init
Done
Start
end
"""