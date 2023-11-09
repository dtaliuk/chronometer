from tkinter import *
from datetime import datetime

temp_time = 0
after_id = ''


# Добавим функцию, которая будет отвечать за таймер
# Рекурсивная функция
def tick():
    global temp_time, after_id
    after_id = root.after(1000, tick)  # 1000 миллисекунд - это 1 секунда
    f_temp = datetime.fromtimestamp(temp_time).strftime('%M:%S')
    label1.configure(text=str(f_temp))
    temp_time += 1


def start_tick():
    btnStart.pack_forget()
    btnStop.pack()
    tick()


def stop_tick():
    btnStop.pack_forget()
    btnContinue.pack()
    btnReset.pack()
    root.after_cancel(after_id)


def continue_tick():
    btnContinue.pack_forget()
    btnReset.pack_forget()
    btnStop.pack()
    tick()


def reset_tick():
    global temp_time
    temp_time = 0
    label1.configure(text='00:00')
    btnContinue.pack_forget()
    btnReset.pack_forget()
    btnStart.pack()


root = Tk()
root.title("Секундомер")
# чтобы пропорции окна не менялись
root.resizable(width=False, height=False)
# укажем разрешение
root.geometry('300x200')


# Создаем лэйбл
label1 = Label(root, width=10, font=('Comic Sans MS', 30), text='00:00:00')
label1.pack()


# Создаем кнопки
btnStart = Button(root, text='Старт', font=('Comic Sans MS', 20), width=12, command=start_tick)
btnStop = Button(root, text='Стоп', font=('Comic Sans MS', 20), width=12, command=stop_tick)
btnContinue = Button(root, text='Продолжить', font=('Comic Sans MS', 15), width=12, command=continue_tick)
btnReset = Button(root, text='Сброс', font=('Comic Sans MS', 15), width=12, command=reset_tick)

btnStart.pack()

root.mainloop()
