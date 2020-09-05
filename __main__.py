#!/usr/bin/env python3
import os
import py.helloer

path = os.path.realpath(__file__)
print("hello from main "+path)
py.helloer.hello()
