import requests
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import time
import sys
from datetime import datetime

zerocount = 0
second = 300
second_str = str(second)
#second_str = str(second).rstrip('0') 
if second_str.endswith('0'):
    print("happend")



didgets = len(str(second_str))

print(f"DIdgests: {didgets}")

while second != 0:
    print(f"{second_str}", end='')
    print(f"\b" * didgets, end='')
    sys.stdout.flush()  
    second = second - 1
    time.sleep(1)

    if second_str.endswith('0'):
        zerocount = zerocount + 1
        print(f"zero count: {zerocount}")
    if zerocount == 2:
        print("happend")
        zerocount = 0 
       #second_str = str(second).rstrip('0')
