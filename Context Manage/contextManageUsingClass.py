class tempClass:
    def __init__(self, text):
        self.text = text
        print("-------[__init__]-------")

    def __enter__(self):
        print(self.text)
        print("-------[__enter__]-------")
        yield self.text + " yield"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("-------[__exit__]-------")


tempObj = tempClass("abc")
"""
Output:- 
-------[__init__]-------
"""

with tempClass("xyz") as _:
    print(str(_))
    print("Done")
"""
Output:- 
-------[__init__]-------
xyz
-------[__enter__]-------
Done
-------[__exit__]-------
"""
