income = int(input())
if income == 0 or income <= 15527:
    percent = 0
    calculated_tax = round((income * (percent / 100))) 
    print(f'The tax for {income} is {percent}%. That is {calculated_tax} dollars!')
elif income == 15528 or income <= 42707:
    percent = 15
    calculated_tax = round((income * (percent / 100))) 
    print(f'The tax for {income} is {percent}%. That is {calculated_tax:} dollars!')
elif income == 42708 or income <= 132406:
    percent = 25
    calculated_tax = round((income * (percent / 100))) 
    print(f'The tax for {income} is {percent}%. That is {calculated_tax} dollars!')
elif income > 132406:
    percent = 28
    calculated_tax = round((income * (percent / 100))) 
    print(f'The tax for {income} is {percent}%. That is {calculated_tax} dollars!')
