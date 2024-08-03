import requests
import pandas as pd
import time
import sys
from datetime import datetime

flip = 0
modifyy = 0
amount1 = 0.0
execution_price1 = 0.0
amount2 = 0.0
execution_price2 = 0.0
#new
amount3 = 0.0
execution_price3 = 0.0
amount4= 0.0
execution_price4 = 0.0
amount5 = 0.0
execution_price5 = 0.0


# not entirely sure how these two work yet
def write_to_file(file_path, data):
    with open(file_path, 'a') as file:
        for key, value in data.items():
            file.write(f"{key} = {value}\n")

def read_from_file(file_path):
    variables = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith("#"):
                key, value = line.split('=')
                variables[key.strip()] = float(value.strip())
    return variables

file_path = 'invest.txt'
investment_details = read_from_file(file_path)

##
hell = 0

leaveit = 0
while leaveit == 0:
    flip = input("Modify Investments or test y/n/t ")
    if flip == "y":
        leaveit = 1
        # ask which invest ment to modify
        while hell == 0:
           
           modifyy = int(input("Which investment to modify 1-5 only pick 6 1-5 does not work or all (6): "))
           
           if modifyy == 1:
                data_to_write = {
                'amount1': float(input("Enter amount1: ")),
                'execution_price1' : float(input("Enter execution_price1: "))
                }
                hell = 1

           if modifyy == 2:
                data_to_write = {
                'amount2': float(input("Enter amount2: ")),
                'execution_price2' : float(input("Enter execution_price2: "))
                }
                hell = 1
           if modifyy == 3:
                data_to_write = {
                'amount3': float(input("Enter amount3: ")),
                'execution_price3' : float(input("Enter execution_price3: "))
                }
                hell = 1
           if modifyy == 4:
                data_to_write = {
                'amount4': float(input("Enter amount4: ")),
                'execution_price4' : float(input("Enter execution_price4: "))
                }
                hell = 1
           if modifyy == 5:
                data_to_write = {
                'amount5': float(input("Enter amount5: ")),
                'execution_price5' : float(input("Enter execution_price5: "))
                }
                hell = 1
           if modifyy == 6:
                data_to_write = {
                    'amount1': float(input("Enter amount1: ")),
                    'execution_price1': float(input("Enter execution_price1: ")),
                    'amount2': float(input("Enter amount2: ")),
                    'execution_price2': float(input("Enter execution_price2: ")),
                    'amount3': float(input("Enter amount3: ")),
                    'execution_price3': float(input("Enter execution_price3: ")),
                    'amount4': float(input("Enter amount4: ")),
                    'execution_price4': float(input("Enter execution_price4: ")),
                    'amount5': float(input("Enter amount5: ")),
                    'execution_price5': float(input("Enter execution_price5: ")),
                }
                hell = 1
        #sperate
        write_to_file(file_path, data_to_write)
        print("Data Written!")
        #update and read the data
        read_data = read_from_file(file_path)
        amount1 = read_data.get('amount1')
        execution_price1 = read_data.get('execution_price1')
        amount2 = read_data.get('amount2')
        execution_price1 = read_data.get('execution_price2')
        amount3 = read_data.get('amount3')
        execution_price1 = read_data.get('execution_price3')
        amount4 = read_data.get('amount4')
        execution_price1 = read_data.get('execution_price4')
        amount5 = read_data.get('amount5')
        execution_price1 = read_data.get('execution_price5')
        
    if flip == "n":
        leaveit = 1
        #read from file
        read_data = read_from_file(file_path)
        amount1 = read_data.get('amount1')
        execution_price1 = read_data.get('execution_price1')
        amount2 = read_data.get('amount2')
        execution_price1 = read_data.get('execution_price2')
        amount3 = read_data.get('amount3')
        execution_price1 = read_data.get('execution_price3')
        amount4 = read_data.get('amount4')
        execution_price1 = read_data.get('execution_price4')
        amount5 = read_data.get('amount5')
        execution_price1 = read_data.get('execution_price5')

    if flip == "t":
     leaveit = 1
     amount1 = 0.0047334
     execution_price1 = 62907.59
     amount2 = 0.0097164
     execution_price2 = 61347.79
     #new
     amount3 = 0
     execution_price3 = 0
     amount4= 0
     execution_price4 = 0
     amount5 = 0
     execution_price5 = 0
    

    



sleept = 300

didgets = 3 

# Calculate initial investment
initial_investment = (amount1 * execution_price1) + (amount2 * execution_price2) + (amount3 * execution_price3) + (amount4 * execution_price4)



# Function to get live Bitcoin price
def get_live_btc_price():
    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
    data = response.json()
    return data['bitcoin']['usd']

# Live updating profit/loss
while True:
    current_price = get_live_btc_price()
    current_value = (amount1 + amount2 + amount3 + amount4) * current_price
    profit_loss = current_value - initial_investment
    
    value1 = amount1 * current_price
    value2 = amount2 * current_price
    value3 = amount3 * current_price
    value4 = amount4 * current_price
    value5 = amount5 * current_price
    

    initinvest1 = amount1 * execution_price1
    initinvest2 = amount2 * execution_price2
    initinvest3 = amount3 * execution_price3
    initinvest4 = amount4 * execution_price4
    initinvest5 = amount5 * execution_price5
    

    profit_loss1 = value1 - initinvest1
    profit_loss2 = value2 - initinvest2
    profit_loss3 = value3 - initinvest3
    profit_loss4 = value4 - initinvest4
    profit_loss5 = value5 - initinvest5
    


    # Get the current date and time
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M")

    # Print the current profit/loss
    print(f"\rCurrent Profit/Loss: ${profit_loss:.2f} at {current_time} BTC {current_price}")
    print(f"Investment 1: ${profit_loss1:.2f} at {execution_price1} with {amount1}btc")
    if amount2 != 0:
        print(f"Investment 2: ${profit_loss2:.2f} at {execution_price2} with {amount2}btc")
    if amount3 != 0:
        print(f"Investment 3: ${profit_loss3:.2f} at {execution_price3} with {amount3}btc")
    if amount4 != 0:
        print(f"Investment 4: ${profit_loss4:.2f} at {execution_price4} with {amount4}btc") 
    if amount5 != 0:
        print(f"Investment 5: ${profit_loss5:.2f} at {execution_price5} with {amount5}btc")
    sys.stdout.flush()
       

    # Append to text file
    with open("log.txt", "a") as file:
        file.write(f"Profit/Loss TOTAL: ${profit_loss:.2f} at {current_time} BTC {current_price}\n")
        file.write(f"Profit/Loss: ${profit_loss1:.2f} at {execution_price1} with {amount1}btc\n")
        if amount2 != 0:
            file.write(f"Profit/Loss: ${profit_loss2:.2f} at {execution_price2} with {amount2}btc\n")
        if amount3 != 0:
            file.write(f"Profit/Loss: ${profit_loss3:.2f} at {execution_price3} with {amount3}btc\n")
        if amount4 != 0:
            file.write(f"Profit/Loss: ${profit_loss4:.2f} at {execution_price4} with {amount4}btc\n")
        if amount5 != 0:
           file.write(f"Profit/Loss: ${profit_loss5:.2f} at {execution_price5} with {amount5}btc\n")
        
        
    
    # Wait for a minute before updating again
    
    print(f"Sleeping Countdown: %s " % (sleept), end='')
    sys.stdout.flush() 
    time.sleep(5)
    sleept - sleept - 5

    while sleept != 0:
        didgets = len(str(sleept)) + 1
        print(f"\b" * didgets, end='')
        sys.stdout.flush()  
        print(f"{sleept}", end=' ')
        sys.stdout.flush()  
        sleept = sleept - 5
        time.sleep(5)
        


    print("0")
    time.sleep(1)
    
    time.sleep(sleept)
    sleept = 300
    

### use json file for writing and reading