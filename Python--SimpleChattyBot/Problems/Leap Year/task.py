a = int(input())  # put your python code here
if ((a % 4 == 0) and (a % 100 != 0)) or (a % 400 == 0):
    print("Leap")
else:
    print("Ordinary")
