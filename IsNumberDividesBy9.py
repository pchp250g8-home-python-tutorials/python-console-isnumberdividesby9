# --condig:utf-8--
import os

os.system("cls")
print("Input an integer number:")
iNum = int(input())
iVal = abs(iNum)
nSumDigits = 0
while (iVal > 0):
    nSumDigits += iVal % 10
    iVal //= 10
print(f"The sum of digits of the number {iNum} is {nSumDigits}")
if nSumDigits % 9 == 0:
    print(f"The number {iNum} divides by 9")
else:
    print(f"The number {iNum} does not divide by 9")
