import os
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def intro():
    clear_console()
    ZeLoopVar=0
    while ZeLoopVar!=29:
        print("This program was made by idiot .inc and drunkcord .inc")
        time.sleep(0.1)
        ZeLoopVar+=1
    print("This program was made by idiot .inc and drunkcord .inc")
    time.sleep(2)
    



Items=[]
ItemPrices=[]

def main():
    while True:    
        clear_console()
        GoToCart=0
        ItemName=""
        while GoToCart==0:
            while ItemName=="":
                ItemName=input("Give me the name of the item that you would like to purchase or enter `done` to finish the order: ")
                if ItemName=="":
                    print("Please enter the name of an item!")
            
            if ItemName=="done" or ItemName=="Done":
                GoToCart=1
                #print("GoToCart is:",GoToCart)
            
            if GoToCart!=1:
                Items.append(ItemName)
                ItemPrice=""
                PriceEntryDone=0
                while PriceEntryDone==0:
                    try:
                        ItemPrice=float(input("Please Enter the Item's price in USD: "))
                    except ValueError:
                        print("Please enter a number!")
                    else:
                        if ItemPrice % 1 == 0:
                            ItemPrices.append(int(ItemPrice))
                        else:
                            ItemPrices.append(float(ItemPrice))
                        ItemName=""
                        PriceEntryDone=1
                
                clear_console()
                print("The Item Was Added To Your Cart!")
                print()
        
        clear_console()
        if Items==[]:
            clear_console()
            print("You Are A Fucking Idiot!")
            exit(0)
        
        ItemAmount=len(Items)
        CurrentItem=0
        print("Your Cart:")
        while ItemAmount!=CurrentItem:
            time.sleep(0.5)
            print("  "+Items[CurrentItem]+" - "+str(ItemPrices[CurrentItem])+"$")
            CurrentItem+=1
        time.sleep(2)
        print("Your total is: "+str(sum(ItemPrices))+"$")
        
        ConfirmOrder=""
        print()
        ConfirmOrder=input("If you want to confirm the order type Y, If you want to add another product to your cart type N: ")
        
        if ConfirmOrder=="y" or ConfirmOrder=="Y":
            clear_console()
            ItemAmount=len(Items)
            CurrentItem=0
            
            print("Your Cart:")
            while ItemAmount!=CurrentItem:
                print("  "+Items[CurrentItem]+" - "+str(ItemPrices[CurrentItem])+"$")
                CurrentItem+=1
            
            print("Your total is: "+str(sum(ItemPrices))+"$")
            print()
            print("Processing your order")
            time.sleep(1)
            clear_console()
            ItemAmount=len(Items)
            CurrentItem=0
            
            print("Your Cart:")
            while ItemAmount!=CurrentItem:
                print("  "+Items[CurrentItem]+" - "+str(ItemPrices[CurrentItem])+"$")
                CurrentItem+=1
            
            print("Your total is: "+str(sum(ItemPrices))+"$")
            print()
            print("Processing your order.")
            time.sleep(1)
            clear_console()
            ItemAmount=len(Items)
            CurrentItem=0
            
            print("Your Cart:")
            while ItemAmount!=CurrentItem:
                print("  "+Items[CurrentItem]+" - "+str(ItemPrices[CurrentItem])+"$")
                CurrentItem+=1
            
            print("Your total is: "+str(sum(ItemPrices))+"$")
            print()
            print("Processing your order..")
            time.sleep(1)
            clear_console()
            ItemAmount=len(Items)
            CurrentItem=0
            
            print("Your Cart:")
            while ItemAmount!=CurrentItem:
                print("  "+Items[CurrentItem]+" - "+str(ItemPrices[CurrentItem])+"$")
                CurrentItem+=1
            
            print("Your total is: "+str(sum(ItemPrices))+"$")
            print()
            print("Processing your order...")
            time.sleep(1)
            clear_console()
            ItemAmount=len(Items)
            CurrentItem=0
            
            print("Your Cart:")
            while ItemAmount!=CurrentItem:
                print("  "+Items[CurrentItem]+" - "+str(ItemPrices[CurrentItem])+"$")
                CurrentItem+=1
            
            print("Your total is: "+str(sum(ItemPrices))+"$")
            print()
            print("Processing your order....")
            time.sleep(1)
            clear_console()
            ItemAmount=len(Items)
            CurrentItem=0
            
            print("Your Cart:")
            while ItemAmount!=CurrentItem:
                print("  "+Items[CurrentItem]+" - "+str(ItemPrices[CurrentItem])+"$")
                CurrentItem+=1
            
            print("Your total is: "+str(sum(ItemPrices))+"$")
            print()
            print("Done!")
            time.sleep(1)

            clear_console()
            ItemAmount=len(Items)
            CurrentItem=0
            
            print("Your Cart:")
            while ItemAmount!=CurrentItem:
                print("  "+Items[CurrentItem]+" - "+str(ItemPrices[CurrentItem])+"$")
                CurrentItem+=1
            
            print("Your total is: "+str(sum(ItemPrices))+"$")
            print()
            print()
            print("Your Item will be delivered by 100% not spy drones and will arrive tomorrow!")
            exit(0)
            

intro()
main()