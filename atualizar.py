import os
import schedule
import time

def atualizar_e_push():
    os.system("python lista.py")
    os.system("git add livros.js")
    os.system('git commit -m "Atualização automática"')
    os.system("git push origin master")

schedule.every().day.at("10:00").do(atualizar_e_push)
schedule.every().day.at("13:00").do(atualizar_e_push)
schedule.every().day.at("19:00").do(atualizar_e_push)
schedule.every().day.at("23:00").do(atualizar_e_push)

while True:
    schedule.run_pending()
    time.sleep(1)
