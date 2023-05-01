import os
import schedule
import time

def atualizar():
    os.system("python lista.py")

def push():
    os.system("git add .")
    os.system("git add livros.js")
    os.system('git commit -m "Atualização automática"')
    os.system("git push")


schedule.every().day.at("10:20").do(atualizar)
schedule.every().day.at("10:25").do(push)
schedule.every().day.at("13:00").do(atualizar)
schedule.every().day.at("13:05").do(push)
schedule.every().day.at("15:00").do(atualizar)
schedule.every().day.at("15:05").do(push)
schedule.every().day.at("17:00").do(atualizar)
schedule.every().day.at("17:05").do(push)
schedule.every().day.at("18:02").do(atualizar)
schedule.every().day.at("18:05").do(push)
schedule.every().day.at("22:02").do(atualizar)
schedule.every().day.at("22:05").do(push)

while True:
    schedule.run_pending()
    time.sleep(1)

#python atualizar.py