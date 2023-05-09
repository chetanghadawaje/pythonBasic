"""
__getattr__ gets called if there is no attribute in the instance.

It’s invoked “last”, if Python can’t find that attribute.(lowest priority)
"""


class A:
    def __getattr__(self, name):
        return 'hahaha-' + name


a = A()
a.ace = 'ace value'
print(a.ace)
print(a.ace2)
print(a.__dict__)
# O/P: ace value
# hahaha-ace2
# {'ace': 'ace value'}

"""
__getattribute__ gets called all the times, whether there is the attribute or not.

It’s invoked “first”(highest priority) — it actually “intercepts” every lookup.

So, even if there is the attribute in the instance, Python calls __getattribute__ first, with the attribute as an argument.
"""


class B:
    def __getattr__(self, name):
        return 'hahaha-'+name

    def __getattribute__(self,name):
        return 'jajaja-'+ name


b = B()
b.ace = 'ace value'
print(b.ace)
print(b.ace2)
print(b.__dict__)
# O/P:jajaja-ace
# jajaja-ace2
# jajaja-__dict__
