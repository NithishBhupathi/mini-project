from datetime import datetime

name=input("Enter Your Name:")
#Lists of Items
lists='''
Rice Rs 65/kg
Wheatflour Rs 55/kg
Spinach Rs 30/kg
Chicken Rs 200/kg
Oil Rs 160/liter 
Sweetcorn Rs 50/dozen
Sugar Rs 45/kg
Eggs Rs 72/dozen
Apple Rs 120/kg
Milk Rs 35/liter
'''

#declaration
price=0
pricelist=[]
Totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]

#rates for items
items={'Rice':65,'Wheatflour':55,'Spinach':30,'Chicken':200,'Oil':160,
       'Sweetcorn':50,'Sugar':45,'Eggs':72,'Apple':120,'Milk':35}

option=int(input("for list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            Totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(Totalprice*5)/100
            finalamount=gst+Totalprice
        else:
            print("Sorry your entered item is not available.") 
    else:
        print("you entered wrong number")   
    inp=input("have you completed your purchase yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","Jai Bheem Supermarket",25*"=")
            print(28*" ","Warangal")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'Quantity',3*" ",'price')
            for i in range(len(pricelist)):
                print(i,8*' ',5*' ',ilist[i],3*' ',qlist[i],8*"  ",plist[i])
            print(75*"-")
            print(50*" ",'TotalAmount:','Rs',Totalprice)
            print("gst amount",40*" ",'Rs',gst)
            print(75*"-")   
            print(50*" ",'finalAmount:','Rs',finalamount)
            print(75*"-")
            print(20*" ","THANKS FOR VISITING")
            print(75*"-")










