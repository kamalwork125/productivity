import pandas as pd 
import numpy as np
from colorama import Fore,Style
print(Fore.YELLOW+"---- PRODUCTIVITY TRACKER-----"+Style.BRIGHT)
task=[]
while True:
    name=input("Enter task name:")
    type=input("Enter task type:")
    time=int(input("Enter type spend:"))
    productive_tasks = ['study', 'exercise', 'reading', 'project']
    unproductive_tasks = ['netflix', 'scrolling', 'youtube', 'nap']

    if type in productive_tasks:
        category = "Productive"
    elif type in unproductive_tasks:
        category = "Unproductive"
    else:
        category = "Neutral"
    task.append([name,type,time,category])
    df=pd.DataFrame(task,columns=["name","type","time","category"])
    print(df)
    total=df['time'].sum()
    print("total productivity:",total)
    average=df['time'].mean()
    print("average productivity is:",average)
    df.to_csv("productivity_tracker.csv", sep='|', index=False)
    print("\n✅ Data saved successfully to file")

