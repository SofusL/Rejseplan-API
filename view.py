from tkinter import *
from datetime import datetime, timedelta

class UserView:
  def __init__(self):
    self.root = Tk()
    self.root.geometry("1080x1920") 
    
  def refresh(self):
    pass

  def setController(self, controller):
    self.controller = controller

  def run(self):
    self.departure = self.controller.fetchDatas()
    self.refresh_Button = Button(self.root, text="✝️", bd = '5', command=self.refresh()).grid(row=3, column=5, padx=5, pady=5)
    Label(self.root, text="Bus", width=10, anchor="w").grid(row=1, column=0, padx=5, pady=2)
    Label(self.root, text="Destination", width=20, anchor="w").grid(row=1, column=1, padx=5, pady=2)
    Label(self.root, text="Planmæssig afgang", width=15, anchor="w").grid(row=1, column=2, padx=5, pady=2)
    Label(self.root, text="forventet afgang", width=14, anchor="w").grid(row=1, column=3, padx=5, pady=2)
    Label(self.root, text="Ankommer om", width=11, anchor="w").grid(row=1, column=4, padx=5, pady=2)
    j=2
    for i in self.departure :
      now = datetime.now().replace(microsecond=0)
      rtTime = i.get("rtTime")
      rtDate = i.get("rtDate")
      depTime = datetime.strptime(rtTime, "%H:%M:%S").time()
      depDate = datetime.strptime(rtDate,"%Y-%m-%d").date()
      rtDep = datetime.combine(depDate, depTime)
      timeDelta = rtDep-now
      timeDelta = max(timeDelta, timedelta())
      print(i.get("name"))
      Label(self.root, text=i.get("name"), width=10, anchor="w").grid(row=j, column=0, padx=5, pady=2)
      Label(self.root, text=i.get("direction"), width=20, anchor="w").grid(row=j, column=1, padx=5, pady=2)
      Label(self.root, text=i.get("time"), width=10, anchor="w").grid(row=j, column=2, padx=5, pady=2)
      Label(self.root, text=i.get("rtTime"), width=10, anchor="w").grid(row=j, column=3, padx=5, pady=2)
      Label(self.root, text=timeDelta, width=10, anchor="w").grid(row=j, column=4, padx=5, pady=2)
      j+=1
    self.root.mainloop()