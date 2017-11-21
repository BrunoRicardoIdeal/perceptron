# -*- coding: utf-8 -*-
from random import choice
from numpy import array, dot, random

step = lambda x: 0 if x < 0 else 1

data = [
    (array([0,0]), 0),
    (array([0,1]), 1),
    (array([1,0]), 1),
    (array([1,1]), 1),
]

w = random.rand(3)
errors = []
learn_rate = 0.2
gen = 100

for i in xrange(gen):
    x, expected = choice(data)
    result = dot(w, x)
    error = expected - step(result)
    errors.append(error)
    w += learn_rate * error * x

for x, _ in data:
    result = dot(x, w)
    print("{}: {} -> {}".format(x[:2], result, step(result)))