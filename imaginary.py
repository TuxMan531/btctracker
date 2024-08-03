import requests
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import time
import sys
from datetime import datetime

sleept = 15
pricemount = 100000

# Initial investment details
amount1 = 0.00678153
execution_price1 = 65862.78
amount2 = 0.00601886
execution_price2 = 66457.77

# Calculate initial investment
initial_investment = (amount1 * execution_price1) + (amount2 * execution_price2)

# Function to get live Bitcoin price
def get_live_btc_price():
    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
    data = response.json()
    return data['bitcoin']['usd']

# Live updating profit/loss
while True:
    current_price = pricemount #######
    current_value = (amount1 + amount2) * current_price
    profit_loss = current_value - initial_investment
    

    # Get the current date and time
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M")

    # Print the current profit/loss
    print(f"Current Profit/Loss: ${profit_loss:.2f} at {current_time} BTC {current_price}\n")
    # Append to text file
    ##DO NOT 
    
    # Wait for a minute before updating again
    print(f"Sleeping Countdown: %s " % (sleept), end='')
    sys.stdout.flush() 
    time.sleep(5)
    sleept - sleept - 5

    while sleept != 0:
        print(sleept, end=' ')
        sys.stdout.flush()  
        sleept = sleept - 5
        time.sleep(5)
        
    print("0")
    time.sleep(1)
    
    time.sleep(sleept)
    sleept = 15
    