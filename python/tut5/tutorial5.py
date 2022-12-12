import json
f = open("orders.json",'r')
data = json.load(f)
print(data)
f.close()
list=data['orders']
dict ={"size": "large",
"price": 7.24,
"toppings": ["pepperoni", "basil"],
"extra_cheese": False,
"delivery": False,"client": {"name": "Mark James","phone": "623-312-528","email": "markjames@gmail.com"}}
list.append(dict)
data['orders']=list

#appending data into json file 
with open ("orders.json",'w') as f:
    json.dump(data,f)
#adding pincode to orders 
data ['orders']= list
for i in list:
    cdict=i['client']
    cdict['pincode']='603203'
with open("order.json",'r' )as t:
    data = json.load(t)
    print(data)

#writting data into a json file
with open ("orders.json",'r') as f:
    temp=json.load(f)
    print("After appending")
    print(temp) 
    with open("new_orders.json",'w') as t:
        json.dump(temp,t)
        print("written data in new file")

# Extracting client name and phone number 
with open("orders.json",'r') as f:
    data = json.load(f)
    data['orders']=list
    for i in list:
        cdict=i['client']
        name=cdict['name']
        ph=cdict['phone']
        print("Customer name:--",name)
        print("Customer Phone_Number:--",ph)

# Extracting client name 
with open("orders.json",'r') as f:
    data = json.load(f)
    data['orders']=list
    for i in list:
        cdict=i['client']
        name=cdict['name']
        ph=cdict['phone']
        print("Customer name:--",name)
        cstring=name[0:2]+name[len(name)-2:]
        cst=name[len(name)-2:]*4
        print("Output")
        print("First 2 and last 2 characters-->",cstring)
        print("4 copies of the last 2 characters-->",cst)

# changing separator in json file
jstring = json.dumps(dict,separators =(": ", " = "))
jstring = json.dumps(dict,separators =(", ", " ; "))
print("After changes:--\n",jstring)

# printing data after ensuring user readability
string = json.dumps(data,sort_keys= True,skipkeys = True,allow_nan = True,indent = 6,)
print("READERE:--\n",string)

