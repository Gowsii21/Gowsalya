print("Welcome to Simple To-Do List App")
tasks=[]
print("\n1.Add Tasks\n 2.Complete Task \n 3.Show To-Do List\n 4.Save and Quit")
while(1):
    c=int(input("\nEnter your choice: "))
    if(c==1):
       a=input("Enter the task: ")
       tasks.append(a)
       print("Task Added Successfully!!")
    elif(c==2):
        com=input("Enter the task number to mark as complete: ")
        tasks.remove(com)
        print("Task Marked as Complete!!!!")
    elif(c==3):
        print("To-Do List: ")
        with open("task.txt","r")as f:
            t1=f.read().splitlines()
            for item in t1:
                if item in tasks:
                    print("Alreadly Exists")
                else:
                    tasks.append(item)
        print("pending",tasks)
    elif(c==4):
        file=open('task.txt','w')
        for item in tasks:
            file.write(item+"\n")
        print("To-Do List Saved Successfully!!")
    else:
        print("INVALID INPUT")
        break;
   