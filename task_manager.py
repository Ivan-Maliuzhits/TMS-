


from datetime import datetime
def delete_task(dele2):
    dt.append(dele2)
    manager["deleted_tasks"] = dt
    manager["tasks"].pop(dele2)
    l = 1
    for item in dt:
        print(l,". DELETE",item)
        print("-"*100)
        l += 1
        print(dt)




def create_task(t):    
    while True:
        task = str(input('Enter task '))        
        if task != "exit":              
            task = task + (' '*5) +'|'+ now_time +'|'  
            t.append(task)
            manager["tasks"] = t        
            l = 1
            for item in t:    
                print(l,".",item)
                print("-"*100)
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
    \n1.Create\n2.Delete\n3.Open tasks\
    \n4.Open deleted tasks\n5.Open complited tasks\nEnter:"))
    if q == 1:        
        create_task(t)        
    elif q== 2:
        dele = int(input("Enter serial task"))
        dele -= 1 
        dele2 = manager["tasks"][dele]
        print(dele2)
        delete_task(dele2)
        
        
        
    elif q == 3:        
        l = 1
        for item in t:    
            print(l,".",item)
            print("-"*100)
            l += 1

    
    
   


    
