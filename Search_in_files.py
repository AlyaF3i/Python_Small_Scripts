import os
from types import GeneratorType

for fileName in os.listdir():
    if not fileName.__contains__('.'):
        continue
    with open(fileName,'r',errors='ignore') as f:
        grep = f.read()
        if grep.__contains__('html'):
            print(fileName)
    

