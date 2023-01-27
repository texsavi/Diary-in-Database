from replit import db
import datetime, time, os

db["pass"]="K1ng"
key=db["pass"]

while True:
  passWd=input("Password>> ").capitalize()
  time.sleep(.2)
  os.system("clear")
  if passWd!="K1ng":
    exit()
  else:
    print("\033[34m⚡⭐Don't Blink, Do it!⭐✨\033[0m")
    print("\033[33mWelcome...✅\n1. Add entry\n2. View entries")
    print()
    entry=input(">> ")
    if entry=="1":
      ctime=datetime.datetime.now()
      entered=input("Type entry> ")
      time.sleep(0.3)
      os.system("clear")
      timEnt=f"entry: {ctime}"
      db[timEnt]=entered
      print("\033[32mDiary updated\033[0m")
      time.sleep(.5)
      os.system("clear")
    else:
      try:
        entries=db.prefix("entry")
        entries=entries[:0:-1]
        counter=0
        for i in entries:
          print(db[i])
          print()
          time.sleep(.5)
          os.system("clear")
          counter+=1
          if counter%1==0:
            go=input("\033[34mView next entry? \ny/n>>\033[0m ").lower()
            if go=="n":
              break
              continue
      except:
        print("\033[31mEntry not found😢\033[0m")
        time.sleep("0.5")
        os.system("clear")
          
    
    
  
  
  