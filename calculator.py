import math
from tkinter import *

root = Tk()
root.title("Calculator")
w = root.winfo_screenwidth() # ширина экрана
h = root.winfo_screenheight() # высота экрана
w = w - w//4 - 200
h = h - h//4 - 200
root.geometry('400x260+{}+{}'.format(w, h))

# Widget
f_top1 = Frame()
f_top2 = Frame()
f_mid1 = Frame()
f_mid2 = Frame()
f_bot1 = Frame()
f_bot2 = Frame()

info = Label(f_top1, bg='black', fg='white', width=16)
mem = Label(f_top1, bg='black', fg='white', width=32)

empty2 = Label(f_top2)
ent = Entry(f_top2, width=48)
lab = Label(f_top2, bg='grey', fg='white', width=48, text='0')
empty3 = Label(f_top2)

b_add = Button(f_mid1, activebackground='Crimson', width=9, text="+")
b_sub = Button(f_mid1, activebackground='Tomato', width=9, text="-")
b_mul = Button(f_mid1, activebackground='Orange', width=9, text="*")
b_div = Button(f_mid1, activebackground='Gold', width=9, text="/")

b_pow = Button(f_mid2, activebackground='SeaGreen', width=9, text="POW")
b_srt = Button(f_mid2, activebackground='MediumAquamarine', width=9, text="SQRT")
b_log = Button(f_mid2, activebackground='SpringGreen', width=9, text="LOG")
b_one = Button(f_mid2, activebackground='LawnGreen', width=9, text="1/X")

n_pin = Button(f_bot1, activebackground='DodgerBlue', width=9, text="PI")
n_exp = Button(f_bot1, activebackground='DeepSkyBlue', width=9, text="E")
n_sin = Button(f_bot1, activebackground='Turquoise', width=9, text="SIN")
n_cos = Button(f_bot1, activebackground='Cyan', width=9, text="COS")

f_sav = Button(f_bot2, activebackground='Indigo', width=9, text="SAVE")
f_get = Button(f_bot2, activebackground='BlueViolet', width=9, text="GET")
f_del = Button(f_bot2, activebackground='MediumOrchid', width=9, text="DELETE")
f_cle = Button(f_bot2, activebackground='Fuchsia', width=9, text="CLEAR")

f_top1.pack()
info.pack(side=LEFT)
mem.pack(side=LEFT)

empty2.pack()
f_top2.pack()
lab.pack()
ent.pack()
empty3.pack()

f_mid1.pack()
b_add.pack(side=LEFT)
b_sub.pack(side=LEFT)
b_mul.pack(side=LEFT)
b_div.pack(side=LEFT)

f_mid2.pack()
b_pow.pack(side=LEFT)
b_srt.pack(side=LEFT)
b_log.pack(side=LEFT)
b_one.pack(side=LEFT)

f_bot1.pack()
n_pin.pack(side=LEFT)
n_exp.pack(side=LEFT)
n_sin.pack(side=LEFT)
n_cos.pack(side=LEFT)

f_bot2.pack()
f_sav.pack(side=LEFT)
f_get.pack(side=LEFT)
f_del.pack(side=LEFT)
f_cle.pack(side=LEFT)


# Function
def inputer(binar):
    if len(binar) > 25:
        result = "Info: Overly Digits"
        ent.delete(0, END)
    elif binar == '':
        result = "Info: No Value"
    elif binar.isdigit():
        result = int(binar)
    elif binar.replace('.', '', 1).isdigit():
        result = float(binar)
    elif len(binar) > 5 and binar[:-4].replace('.', '', 1).isdigit():
        if binar[-3] == 'e':
            if binar[-4] == '-':
                result = float(binar[:-4]) * (10 ** -(int(binar[-2:])))
            elif binar[-4] == '+':
                result = float(binar[:-4]) * (10 ** -(int(binar[-2:])))
            else:
                result = "Info: Input Error"
                ent.delete(0, END)
        elif binar[-2] == 'e':
            if binar[-3] == '-':
                result = float(binar[:-3]) * (10 ** -(int(binar[-2:])))
            elif binar[-3] == '+':
                result = float(binar[:-3]) * (10 ** -(int(binar[-2:])))
            else:
                result = "Info: Input Error"
                ent.delete(0, END)
        else:
            result = "Info: Input Error"
            ent.delete(0, END)
    elif binar[0] == '-':
        if binar[1:].isdigit():
            result = -int(binar[1:])
        elif binar[1:].replace('.', '', 1).isdigit():
            result = -float(binar[1:])
        elif len(binar) > 6 and binar[1:-4].replace('.', '', 1).isdigit():
            if binar[-3] == 'e':
                if binar[-4] == '-':
                    result = -float(binar[1:-4]) * (10 ** -(int(binar[-2:])))
                elif binar[-4] == '+':
                    result = -float(binar[1:-4]) * (10 ** -(int(binar[-2:])))
                else:
                    result = "Info: Input Error"
                    ent.delete(0, END)
            elif binar[-2] == 'e':
                if binar[-3] == '-':
                    result = -float(binar[1:-3]) * (10 ** -(int(binar[-2:])))
                elif binar[-3] == '+':
                    result = -float(binar[1:-3]) * (10 ** -(int(binar[-2:])))
                else:
                    result = "Info: Input Error"
                    ent.delete(0, END)
            else:
                result = "Info: Input Error"
                ent.delete(0, END)
        else:
            result = "Info: Input Error"
            ent.delete(0, END)
    else:
        result = "Info: Input Error"
        ent.delete(0, END)
    return result


# Operation
def add(event):
    val = inputer(ent.get())
    basic = basic_var()
    if not isinstance(val, str):
        result = basic + val
        info['text'] = ''
        lab['text'] = str(result)
        ent.delete(0, END)
    else:
        info['text'] = val


def sub(event):
    val = inputer(ent.get())
    basic = basic_var()
    if not isinstance(val, str):
        result = basic - val
        info['text'] = ''
        lab['text'] = str(result)
        ent.delete(0, END)
    else:
        info['text'] = val


def mul(event):
    val = inputer(ent.get())
    basic = basic_var()
    if not isinstance(val, str):
        result = basic * val
        info['text'] = ''
        lab['text'] = str(result)
        ent.delete(0, END)
    else:
        info['text'] = val


def div(event):
    val = inputer(ent.get())
    basic = basic_var()
    if not isinstance(val, str):
        if val == 0:
            info['text'] = "Info: Zero Error"
            ent.delete(0, END)
        else:
            result = basic / val
            info['text'] = ''
            lab['text'] = str(result)
            ent.delete(0, END)
    else:
        info['text'] = val


def powder(event):
    val = inputer(ent.get())
    basic = basic_var()
    if not isinstance(val, str):
        result = pow(basic, val)
        info['text'] = ''
        lab['text'] = str(result)
        ent.delete(0, END)
    else:
        info['text'] = val


def srt(event):
    val = inputer(ent.get())
    basic = basic_var()
    if not isinstance(val, str):
        if val == 0:
            result = 0
            info['text'] = ''
            lab['text'] = str(result)
            ent.delete(0, END)
        elif val > 0:
            if basic > 0:
                result = pow(basic, (1 / val))
                info['text'] = ''
                lab['text'] = str(result)
                ent.delete(0, END)
            elif basic < 0:
                if val % 2 == 1:
                    result = -pow(basic, (1 / val[1:]))
                    info['text'] = ''
                    lab['text'] = str(result)
                    ent.delete(0, END)
                else:
                    info['text'] = "Info: Complex number"
                    ent.delete(0, END)
            else:
                result = 0
                info['text'] = ''
                lab['text'] = str(result)
                ent.delete(0, END)
        else:
            info['text'] = "Info: Error Value"
            ent.delete(0, END)



def logaf(event):
    val = inputer(ent.get())
    basic = basic_var()
    if not isinstance(val, str):
        if basic <= 0 or val <= 0:
            info['text'] = "Info: Error Value"
            ent.delete(0, END)
        else:
            result = math.log(basic, val)
            info['text'] = ''
            lab['text'] = str(result)
            ent.delete(0, END)
    else:
        info['text'] = val


def one(event):
    val = inputer(ent.get())
    if not isinstance(val, str):
        result = 1 / val
        ent.delete(0, END)
        ent.insert(0, result)
    else:
        info['text'] = val


# Func
def sav(event):
    mem['text'] = "Memory: {}".format(lab['text'])


def get_func(event):
    if mem['text'] != '':
        value = mem['text'][8:]
        ent.delete(0, END)
        ent.insert(0, value)


def delete(event):
    lab['text'] = '0'
    ent.delete(0, END)


def clear(event):
    mem['text'] = ''
    info['text'] = ''


def pin(event):
    ent.delete(0, END)
    ent.insert(0, math.pi)


def exp(event):
    ent.delete(0, END)
    ent.insert(0, math.e)


def sin(event):
    val = inputer(ent.get())
    if not isinstance(val, str):
        rad = math.radians(val)
        result = math.sin(rad)
        ent.delete(0, END)
        ent.insert(0, result)
    else:
        info['text'] = val


def cos(event):
    val = inputer(ent.get())
    if not isinstance(val, str):
        rad = math.radians(val)
        result = math.cos(rad)
        ent.delete(0, END)
        ent.insert(0, result)
    else:
        info['text'] = val


# Variable
def basic_var():
    if lab['text'].isdigit():
        basic = int(lab['text'])
    else:
        basic = float(lab['text'])
    return basic


b_add.bind('<Button-1>', add)
b_sub.bind('<Button-1>', sub)
b_mul.bind('<Button-1>', mul)
b_div.bind('<Button-1>', div)

b_pow.bind('<Button-1>', powder)
b_srt.bind('<Button-1>', srt)
b_log.bind('<Button-1>', logaf)
b_one.bind('<Button-1>', one)

n_pin.bind('<Button-1>', pin)
n_exp.bind('<Button-1>', exp)
n_sin.bind('<Button-1>', sin)
n_cos.bind('<Button-1>', cos)

f_sav.bind('<Button-1>', sav)
f_get.bind('<Button-1>', get_func)
f_del.bind('<Button-1>', delete)
f_cle.bind('<Button-1>', clear)

if __name__ == "__main__":
    root.mainloop()
