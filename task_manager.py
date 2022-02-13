


from datetime import datetime

def complited(x):
    x -= 1
    y = manager["tasks"][x]
    result = "|COMPLITED| {0}".format(y)
    manager["tasks"][x] = result
    print(manager["tasks"][x])

def delete_task(dele2):
    dt.append(dele2)
    manager["deleted_tasks"] = dt    
    t.pop(dele) 
    manager["tasks"] = t    
    l = 1
    for item in dt:        
        print(l,". DELETED {0}".format(item))
        print("-"*90)
        l += 1
    return manager,t

def create_task(t):    
    while True:
        task = str(input('Enter task\nor enter "exit" = : '))        
        if task != "exit":              
            task = task + (' '*5) +'|'+ now_time +'|'  
            t.append(task)
            manager["tasks"] = t        
            l = 1
            for item in t:    
                print(l,".",item)
                print("-"*90)
                l += 1
            continue                    
        else:
            break  

now_time = str(datetime.today())[:-7]
ct, dt, t, = [], [], [], 
manager =  {"deleted_tasks" : dt,
            "tasks" : t,
            "completed_tasks" : ct,}

while True: 
    q = int(input("Выберите действие!\
    \n|1.Create |2.Delete |3.Open tasks\
    \n|4.Open deleted tasks |5.Open complited tasks |6.Search\nEnter:"))
    
    if q == 1:        
        create_task(t)        
    elif q== 2:
        dele = int(input("Enter serial task: "))
        dele -= 1 
        dele2 = manager["tasks"][dele]     
        delete_task(dele2)  

    elif q == 3:
        n = None        
        while True:            
            if n != "exit":        
                l = 1
                for item in t:    
                    print(l,".",item)
                    print("-"*90)
                    l += 1
                n = str(input("Enter 'exit' or 'done' tasks: "))
                if n == "done":
                    x = int(input("Enter serial: "))
                    complited(x)
            else:
                break
    elif q == 4:
        l = 1
        for item in dt:
            print(l,". DELETED",item)
            print("-"*90)
            l += 1
    elif q == 6:
        element = str(input("Enter a request: "))   
        for key in manager:          
            for word in manager[key]:
                if key == "deleted_tasks":
                    print("DELETED", word if element in word[:len(element)] else '')
                elif key == "tasks":
                    print(word if element in word[:len(element)] else '')
                elif key == "completed_tasks":
                    print("COMPLITED", word if element in word[:len(element)] else '')


        
            

    
    
   


    
