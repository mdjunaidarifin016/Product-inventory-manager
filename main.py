import json

def load_sales():
    try:
        with open("sales_history.json","r")as f:
           content=f.read()
           if not content.strip():
                return []
           else:
                data= json.loads(content)
                if isinstance(data,list):
                    return data
                else:
                    raise ValueError("File contains unsupported data")
    except FileNotFoundError:
            return []
    except json.JSONDecodeError:
        raise
def load_products():
    try:
        with open("inventory.json","r")as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError("Products file not found,please check before trying again")
    except json.JSONDecodeError:
        raise
    
def save_history(sale):
    with open("sales_history.json","w")as f:
        return json.dump(sale,f)
def save_product(prod):
    with open("inventory.json","w")as f:
        return json.dump(prod,f)
def get_qty():
    while True:
        try:
            qty=int(input("Enter quantity:"))
        except ValueError:
            print("Enter a valid Quantity!,try again")
            continue
        else:
            break
    return qty
class LowStock(Exception):
    pass

def process_sale(product,quantity):
    if quantity<=0:
        raise ValueError ("Quantity must be greater than zero")
    elif product["stock"]<quantity:
        raise LowStock ("Stock is low")
    product["stock"]-=quantity
    profit=(product['selling_price']-product['purchase_cost'])*quantity
    print(f"avalailable stock :{product['stock']},\nprofit:{profit}")
    product_sale={}
    product_sale["product_id"]=product["id"]
    product_sale["quantity_sold"]=quantity
    product_sale["revenue"]=product["selling_price"]*quantity
    product_sale["profit"]=profit
    product_sale["remaining_stock"]=product["stock"]
    return product_sale

def handle_sale():
    id_found=False
    try:
        products=load_products()
    except FileNotFoundError as f:
        print(f)
    except json.JSONDecodeError as j:
        print(j)
    else:
        prod_id=input("Enter product id:")
        for prod_no,prod_det in products.items():
            if prod_id==prod_det["id"]:
                stock_before=prod_det["stock"]
                id_found=True
                while True:
                    try:
                        sales_history=load_sales()
                    except json.JSONDecodeError as j:
                        print (j)
                        break
                    except ValueError as v:
                        print(v)
                        break
                    else:
                        qty=get_qty()
                        try:
                            s=process_sale(prod_det,qty)
                            sales_history.append(s)
                        except ValueError as v:
                            print(v)
                            continue
                        except LowStock as l:
                            print(l)
                            continue
                        else:
                            try:
                                save_product(products)
                                save_history(sales_history)
                            except Exception as e:
                                print(f"Sale could not be saved: {e}")
                                prod_det["stock"]=stock_before
                                try:
                                    save_product(products)
                                except Exception as ex:
                                    print(f"WARNING: Could not restore inventory: {ex}")
                            else:       
                                print("Sale completed successfully!")
                                break
        if not id_found:
            print ("id not found")
    

def total_revenue(product_id):
    sales=load_sales()
    total_rvnue=0
    for sale in sales:
        if sale["product_id"]==product_id:
            total_rvnue+=sale["revenue"]
    return total_rvnue
def total_profit(prod_id):
    sales=load_sales()
    total_prof=0
    for sale in sales:
        if sale["product_id"]==prod_id:
            total_prof+=sale["profit"]
    return total_prof
def count_sales(product_id):
    sales=load_sales()
    count=0
    for sale in sales:
        if sale["product_id"]==product_id:
            count+=1
    return count
def sale_summery():
    try:
        products=load_products()
    except FileNotFoundError as f:
        print(f)
    except json.JSONDecodeError as j:
        print(j)
    else:
        product_id=input("Enter product ID:")
        id_found=False
        for prod_no,prod_det in products.items():
            if prod_det["id"]==product_id:
                id_found=True
                stock=prod_det["stock"]
        if id_found:
            try:
                totalrevenue=total_revenue(product_id)
                totalprofit=total_profit(product_id)
                countsales=count_sales(product_id)
            except json.JSONDecodeError as j:
                print(j)
                return
            except ValueError as v:
                print(v)
                return
            else:
                if isinstance(totalrevenue,(int ,float)) and isinstance(totalprofit,(int ,float)) and isinstance(countsales,int):
                    print("========== SALES SUMMARY ==========")
                    print(f"Total Revenue:  ₹{totalrevenue}")
                    print(f"Total Profit:  ₹{totalprofit}")
                    print(f"Successfull sales:  {countsales}")
                    print(f"Avalailable stock:  {stock}")
                    return
                else:
                    print("Something went wrong check sales_history file and try again!")
                    return
        print("ID not found")
def menu():
    while True:
        print("=======Product Management Menu========")
        print("1.Process sale")
        print("2.Sale Summery")
        print("3.Sales History")
        print("4.Inventory")
        print("5.Exit")

        try:
            choice=int(input("enter your choice:"))
        except ValueError:
            print("Enter a valid choice!")
            continue
        if choice==1:
            handle_sale()
        elif choice==2:
            sale_summery()
        elif choice==3:
            try:
                sales=load_sales()
            except ValueError as v:
                print (v)
            except json.JSONDecodeError as j:
                print(j)
            else:
                if sales ==[]:
                    print("There is no saved history")
                else:
                    print (sales)
        elif choice==4:
            try:
                products=load_products()
            except FileNotFoundError as f:
                print (f)
            except json.JSONDecodeError as j:
                print(j)
            else:
                print(products)
        elif choice==5:
            print("Thank You!")
            break
        else:
            print("Enter a valid choice")
menu()