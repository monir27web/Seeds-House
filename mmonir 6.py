item_dict = {}
f = open("F:\\monir.txt","r")
while True:
  item=f.readline()
  if item=="\n":
      break
  qutt = f.readline()
  uprice = f.readline() 
  item = item[:len(item)-1]
  qutt = int(qutt[:len(qutt)-1])
  uprice = float(uprice[:len(uprice)-1])
  item_dict[item]=[qutt,uprice]
f.close()  


def present_data() :
    print (30*"=")
    print ("**MONIR's Seeds Shop**".center(30))
    print (30*"=")
    print ("_Aviable Seeds in Store Room_".center(30))
    print (30*"=")
    for x in item_dict:
        print(x,(20-len(x))*" " ,(6-len(str(item_dict[x][0])))*" " ,item_dict[x][0])
    print(28*"-")

    

def dec_quant(item,amount):
    item_dict[item][0] -=amount   


def inc_quant(item,amount):
    item_dict[item][0] +=amount


def import_seeds():
    while True:
        item = input("Item(Type 'x' To Stop): ")
        if item=='x':
            break
        amnt = int(input("amount: "))
        if item not in item_dict:
            print("New Seeds Found")
            uprice = float (input("Enter The Unit Price: "))
            item_dict[item] = [amnt,uprice]
            continue
        inc_quant(item,amnt)
    

def sell_seeds():
    demand_list = []
    while True:
        item = input ("Item (Type 'x' to Stop): ")
        if item=='x':
            break
        if item not in item_dict:
            print("Sorry! item is not available.".title())
            continue
        amnt = int(input("amount: "))
        if amnt>item_dict[item][0]:
            print(f"total {item_dict[item][0]} pcs available!")
            continue
        dec_quant(item,amnt)
        demand_list+=[item,amnt,
                      item_dict[item][1],
                      amnt*item_dict[item][1]],
    print (40*"=")
    print ("** Payment Receipt **".center(40))
    print (40*"=")
    print("item name".title()," "," ", "quantity".title()," ","uprice".title(), "subtotal".title())
    print (40*"-")
    tprice=0
    for x in demand_list:
        tprice+=x[3]
        print (x[0].title(), (13-len(x[0]))*" ",
              (6-len(str(x[1])))*" ",x[1],
              (6-len(str("%.2f"%x[2])))*" ","%.2f"%x[2],
              (8-len(str("%.2f"%x[3])))*" ","%.2f"%x[3])
    print (40*"-")
    tprice="%.2f"%tprice
    print("Total Price:".title(),(26-len(str(tprice)))*" ",tprice)
    print(40*" ")

    
while True:
    present_data()
    print("Choose An Option:")
    print("Type '1' : Import Seeds to Store")
    print("Type '2' : Calculate and Show Seeds")
    print("Type '3' : Close Shop")
    choice = (input("choice: "))
    if choice == '1':
        import_seeds()
    elif choice =='2':
        sell_seeds()
    elif choice =='3':
        break
    else:
        continue

                 
f = open("F:\\monir.txt","w")
for x in item_dict:
    f.write(x+"\n")
    f.write((str(item_dict[x][0]))+"\n")
    f.write((str(item_dict[x][1]))+"\n")
f.write("\n")
f.close()

    
        
