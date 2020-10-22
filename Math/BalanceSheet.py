__author__ = "Gordan"
print("Welcome \n This is a balance sheet calculator.")
print("input '000' in the statements below to move on")
asarr = []
liarr = []
while True:
    ASSETS = int(input("Enter cost of asset: "))
    asarr.append(ASSETS)
    if ASSETS == 000:
        break
print("input '000' in the statements below to move on")
while True:
    LIABILITIES = int(input("Enter cost of Liabilitiy: "))
    liarr.append(LIABILITIES)
    if LIABILITIES == 000:
        break

print(asarr)
print(liarr)

totalAssets = sum(asarr)
totalLiabilities = sum(liarr)
ownerEquity = totalAssets - totalLiabilities

print(f"Total assets = {totalAssets}")
print(f"Total Liabilities = {totalLiabilities}")
print(f"Owners Equity = {ownerEquity}")