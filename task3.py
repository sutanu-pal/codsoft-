tasks=[]
def add_task():
    task=input("enter a new task:")
    tasks.append(task)
    print("task added successfully")
def view():
    if len(tasks)==0:
        print("no task")
    else:
        print("list of tasks:")
        for i, task in enumerate(tasks):
            print(f' {i+1}.{task}')
def delete_task():
    if len(tasks)==0:
        print("no task to delete")
    else:
        print("tasks")
        for i, task in enumerate(tasks):
            print(f'{i+1}.{task}')
        choice= int(input("enter the task number to delete:"))
        if 0<choice<= len(tasks):
            del tasks[choice-1]
            print("task deleted!")
        else:
            print("invalid task number")
def update():
    index= int(input("enter index of task to update:"))
    a= input("enter new task:")
    if 0<=index< len(tasks) :
       tasks[index] = a
       print("task updated!")
       
    

def main():
    while True:
        print("\n Menue:")
        print("1.add Task")
        print("2.view")
        print("3.delete")
        print("4.update")
        print("5.exit")
        ch=int(input("enter your choice:"))
               
        if ch==1:
         add_task()
        elif ch==2:
           view()
        elif ch==3:
           delete_task()
        elif ch==4:
           update()
        elif ch==5:
          print("thank you! exiting...")
          break
        else:
           print("invalid choice!!!")
        
if __name__ =="__main__":
  main()
            