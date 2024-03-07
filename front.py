from tkinter import *
import tkcalendar
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException
from EisBerezkaParser import Parser
from EBParser import eb_parser
from ExportToOneXML import run
from Cleaner import clean
import tkinter.messagebox as mb
#7709895509
#7702151927
window = Tk()

window.title("ЕИС-Березка-ЭБ Сверка")
window.iconbitmap('lupa.ico')
window.geometry("500x300")

calendar1 = tkcalendar.DateEntry(window, date_pattern='dd.mm.yyyy')
#calendar1 = Text(window, height=1, width=15)
calendar1.pack()

calendar2 = tkcalendar.DateEntry(window, date_pattern='dd.mm.yyyy')
#calendar2 = Text(window, height=1, width=15)
calendar2.pack()

innput = Text(window, height=1, width=15)
innput.pack()

def pars():
    try:
        Parser(calendar1.get_date().strftime("%d.%m.%Y"), calendar2.get_date().strftime("%d.%m.%Y"), innput.get(1.0, "end-1c"))
        eb_parser(calendar1.get_date().strftime("%d.%m.%Y"), calendar2.get_date().strftime("%d.%m.%Y"), innput.get(1.0, "end-1c"))
        #Parser(calendar1.get("1.0",'end-1c'), calendar2.get("1.0",'end-1c'), innput.get(1.0, "end-1c"))
        #eb_parser(calendar1.get("1.0",'end-1c'), calendar2.get("1.0",'end-1c'), innput.get(1.0, "end-1c"))
        run(innput.get(1.0, "end-1c"))
        clean()
    except TimeoutException and NoSuchElementException and ElementNotVisibleException and ElementClickInterceptedException as ex:
        mb.showerror('Ошибка!', f'Проблема со скоростью загрузки веб-страниц. Попробуйте запустить программу еще раз.\n\n{EX}')
        print('Что-т тут не так')
        print(EX)
    
    except Exception as EX:
        mb.showerror('Ошибка!', f'Работа программы была прервана. Попробуйте запустить программу еще раз.\n\n{EX}')
        print('Что-т тут не так')
        print(EX)

start = Button(window, text='Начать', command=pars)
start.pack()

window.mainloop()