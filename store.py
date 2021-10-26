quantProducts = {1: 10, 2: 4, 3: 0, 4: 9}
priceProduct = {1: 9.99, 2:19.9, 3: 14.99, 4: 4.99}

cash = 0

def showMenu():
    print("Menu")
    print("1.- Show full store detail")
    print("2.- Sales")
    print("3.- Replace")
    print("4.- Change price of product")
    print("5.- exit")
    option = int(input("Choose an option:"))
    return option

def getPriceProduct(code):
    if not priceProduct:
        return False
    else:
        return priceProduct[code]

def getQuantityProduct(code):
    if not quantProducts:
        return False
    else:
        return quantProducts[code]

def getDetailProduct(code):
    if not quantProducts:
        if not priceProduct:
            return False
    else:
        price = priceProduct[code]
        quant = quantProducts[code]
        detail = "{}, {}".format(quant,price)
        return detail

def getCash():
    global cash

    return float(cash)

def addQuantProduct(code, quant):
    if not quantProducts:
        return False
    else:
        quantProducts[code] = getQuantityProduct(code) + quant
    
def setPriceProduct(code, price):
    if not priceProduct:
        return False
    else:
        priceProduct[code] = price
        msg = "Price of", priceProduct[code], "updated"
        return msg

def saleProduct(code):
    global cash
    if not priceProduct or not quantProducts:
        return False
    else:
        global cash
        cash = cash + (getPriceProduct(code)*getQuantityProduct(code))
        quantProducts[code] = 0
        msg = "SUCCESFULY SALE"
        return msg

def replaceProduct(code, quant):
    global cash
    if not priceProduct or not quantProducts:
        return False
    else:
        cash =  cash - (getPriceProduct(code)*0.2)
        quantProducts[code] = getQuantityProduct(code) + quant
        msg = "SUCCESFULY RESTOCKED"
        return msg

def getFullStock():
    if not priceProduct or not quantProducts:
        return False
    else:
        full_stock = []
        for i in quantProducts.keys():
            full_stock.append((i, quantProducts[i], priceProduct[i]))
        return full_stock

while True:
    option = showMenu()

    if option == 1:

        if getFullStock == False:
            print("ERROR, EMPY DATA")
        else:
            print("Curren store status")
            print("===================")
            print("Product detail: ")
            print("[Code - Unit - Price]")
            for i in getFullStock():
                print(i)
            print("Cash", getCash(),"€")

    elif option == 2:

        code = int(input("Enter product code: "))
        if saleProduct(code) == False:
            print("ERROR, EMPTY DATA")
        else:
            print(saleProduct(code))

    elif option == 3:

        code = int(input("Enter product code: "))
        units = int(input("Enter units: "))
        if replaceProduct(code,units) == False:
            print("ERROR, EMPTY DATA")
        else:
            print(replaceProduct(code,units))

    elif option == 4:

        code = int(input("Enter product code: "))
        price = float(input("Set a new price: "))

        if setPriceProduct == False:
            print("ERROR, EMPTY DATA")
        else:
            print(setPriceProduct(price,code))

    elif option == 5:
        print("Exit")
        break

    



















    




