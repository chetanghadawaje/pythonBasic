""" f-strings were introduced in Python 3.6"""
import math

style = "formatted"
print(f"This is a {style} string")

r = 3.6
print(f"A circle with radius {r} has area {math.pi * r * r:.2f}")

python = 3.8
print(f"{python=}")
