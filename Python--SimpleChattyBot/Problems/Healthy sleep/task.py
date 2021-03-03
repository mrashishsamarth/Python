A, B, H = int(input()), int(input()), int(input())
if H < A:
    print('Deficiency')
elif A <= H <= B:
    print('Normal')
else:
    print('Excess')