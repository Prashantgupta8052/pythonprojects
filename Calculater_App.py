import operator
from pydoc import text
from tkinter import *
import math

first_number=second_number=operator=None

def scientific_operation(op):
    try:
        number = float(result_label['text'])

        if op == 'x^2':
            result = number ** 2

        elif op == 'x^3':
            result = number ** 3

        elif op == 'x^1/2':
            result = math.sqrt(number)

        elif op == 'x^1/3':
            result = number ** (1/3)

        elif op == '10^x':
            result = 10 ** number

        elif op == 'x!':
            result = math.factorial(int(number))

        elif op == 'sin':
            result = math.sin(math.radians(number))

        elif op == 'cos':
            result = math.cos(math.radians(number))

        elif op == 'tan':
            result = math.tan(math.radians(number))

        elif op == 'log':
            result = math.log10(number)

        elif op == 'ln':
            result = math.log(number)

        result_label.config(text=str(result))

    except:
        result_label.config(text='Error')
        
def decimal():
    current = result_label['text']
    if current == '':
        result_label.config(text='0.')
    elif '.' not in current:
        result_label.config(text=current + '.')

def precentage():
   def percentage():
    current = result_label['text']

    if current == '':
        return

    current = float(current)
    result_label.config(text=str(current / 100))

def get_result():
    global first_number,second_number,operator
    second_number=int(result_label['text'])
    if operator=='+':
        result_label.config(text=str(first_number+second_number))
    elif operator=='-':
        result_label.config(text=str(first_number-second_number))
    elif operator=='x':
        result_label.config(text=str(first_number*second_number))
    elif operator=='/':
        if second_number==0:
            result_label.config(text='undefind')
        else:
            result_label.config(text=str(round(first_number/second_number)))

def get_operator(op):
    global first_number,operator
    first_number=int(result_label['text'])
    operator=op
    result_label.config(text='')

def del_one_by_one():
    current=result_label['text']
    if current:
        new=current[:-1]
        result_label.config(text=new)

def all_clear():
    result_label.config(text='')
 
def get_digit(digit):
    current=result_label['text']
    new=current+str(digit)
    result_label.config(text=new)

root=Tk()

root.title('Calculater')

root.configure(background='gray')
root.iconbitmap('caluculator_image2.ico')
root.geometry('280x380')
root.resizable(0,0)

result_label=Label(root,text='',bg='gray', fg='black')
result_label.grid(row=0, column=0,columnspan=20, pady=(70,25),sticky='w')
result_label.config(font=('verdana',30,'bold'))

btn7=Button(root,text='7',bg='#00a65a', fg='#505050', width=4, height=1,command=lambda:get_digit(7))
btn7.grid(row=1, column=0)
btn7.config(font=('verdana',14))

btn8=Button(root,text='8',bg='#00a65a', fg="#505050", width=4, height=1,command=lambda:get_digit(8))
btn8.grid(row=1, column=1)
btn8.config(font=('verdana',14))

btn9=Button(root,text='9',bg='#00a65a', fg='#505050', width=4, height=1,command=lambda:get_digit(9) )
btn9.grid(row=1, column=2)
btn9.config(font=('verdana',14))

btn_add=Button(root,text='+',bg='#00a65a', fg="#3A3A3A", width=4, height=1,command=lambda:get_operator('+'))
btn_add.grid(row=1, column=3)
btn_add.config(font=('verdana',14))

btn_sub=Button(root,text='-',bg='#00a65a', fg="#3A3A3A", width=4, height=1,command=lambda:get_operator('-') )
btn_sub.grid(row=1, column=4)
btn_sub.config(font=('verdana',14))

btn4=Button(root,text='4',bg='#00a65a', fg='#505050', width=4, height=1,command=lambda:get_digit(4))
btn4.grid(row=2, column=0)
btn4.config(font=('verdana',14))

btn5=Button(root,text='5',bg='#00a65a', fg="#505050", width=4, height=1,command=lambda:get_digit(5))
btn5.grid(row=2, column=1)
btn5.config(font=('verdana',14))

btn6=Button(root,text='6',bg='#00a65a', fg='#505050', width=4, height=1,command=lambda:get_digit(6))
btn6.grid(row=2, column=2)
btn6.config(font=('verdana',14))

btn_mul=Button(root,text='x',bg='#00a65a', fg="#3A3A3A", width=4, height=1,command=lambda:get_operator('x'))
btn_mul.grid(row=2, column=3)
btn_mul.config(font=('verdana',14))

btn_div=Button(root,text='/',bg='#00a65a', fg="#3A3A3A", width=4, height=1,command=lambda:get_operator('/') )
btn_div.grid(row=2, column=4)
btn_div.config(font=('verdana',14))

btn1=Button(root,text='1',bg='#00a65a', fg='#505050', width=4, height=1,command=lambda:get_digit(1))
btn1.grid(row=3, column=0)
btn1.config(font=('verdana',14))

btn2=Button(root,text='2',bg='#00a65a', fg="#505050", width=4, height=1,command=lambda:get_digit(2))
btn2.grid(row=3, column=1)
btn2.config(font=('verdana',14))

btn3=Button(root,text='3',bg='#00a65a', fg='#505050', width=4, height=1,command=lambda:get_digit(3))
btn3.grid(row=3, column=2)
btn3.config(font=('verdana',14))

btn_DEL=Button(root,text='DEL',bg='#00a65a', fg="#3A3A3A", width=4, height=1,command=lambda:del_one_by_one() )
btn_DEL.grid(row=3, column=3)
btn_DEL.config(font=('verdana',14))

btn_AC=Button(root,text='AC',bg='#00a65a', fg="#3A3A3A", width=4, height=1, command=lambda:all_clear())
btn_AC.grid(row=3, column=4)
btn_AC.config(font=('verdana',14))

btn0=Button(root,text='0',bg='#00a65a', fg='#505050', width=4, height=1,command=lambda:get_digit(0) )
btn0.grid(row=4, column=0)
btn0.config(font=('verdana',14))

btn_dec=Button(root,text='.',bg='#00a65a', fg="#505050", width=4, height=1,command=decimal)
btn_dec.grid(row=4, column=1)
btn_dec.config(font=('verdana',14))

btn_prece=Button(root,text='%',bg='#00a65a', fg='#505050', width=4, height=1,command=precentage() )
btn_prece.grid(row=4, column=2)
btn_prece.config(font=('verdana',14))

btn_Square=Button(root,text='x^2',bg='#00a65a', fg="#3A3A3A", width=4, height=1,command=lambda: scientific_operation('x^2'))
btn_Square.grid(row=4, column=3)
btn_Square.config(font=('verdana',14))

btn_Equal=Button(root,text='=',bg='#00a65a', fg="#3A3A3A", width=4, height=1,command=get_result)
btn_Equal.grid(row=4, column=4)
btn_Equal.config(font=('verdana',14))

btn_squareroot=Button(root,text='x^1/2',bg='#00a65a', fg='#505050', width=4, height=1,command=lambda:get_operator('x^1/2'))
btn_squareroot.grid(row=5, column=0)
btn_squareroot.config(font=('verdana',14))

btn_cube=Button(root,text='x^3',bg='#00a65a', fg="#505050", width=4, height=1,command=lambda: scientific_operation('x^3'))
btn_cube.grid(row=5, column=1)
btn_cube.config(font=('verdana',14))

btn_10kipower=Button(root,text='10^x',bg='#00a65a', fg='#505050', width=4, height=1,command=lambda: scientific_operation('10^x'))
btn_10kipower.grid(row=5, column=2)
btn_10kipower.config(font=('verdana',14))

btn_factorial=Button(root,text='x!',bg='#00a65a', fg="#3A3A3A", width=4, height=1,command=lambda:scientific_operation('x!') )
btn_factorial.grid(row=5, column=3)
btn_factorial.config(font=('verdana',14))

btn_cubicroot=Button(root,text='',bg='#00a65a', fg="#3A3A3A", width=4, height=1,command=lambda:scientific_operation('x^1/3') )
btn_cubicroot.grid(row=5, column=4)
btn_cubicroot.config(font=('verdana',14))


btn_sin=Button(root,text='sin',bg='#00a65a', fg='#505050', width=4, height=1,command=lambda:scientific_operation('sin') )
btn_sin.grid(row=6, column=0)
btn_sin.config(font=('verdana',14))

btn_cos=Button(root,text='cos',bg='#00a65a', fg="#505050", width=4, height=1,command=lambda:scientific_operation('cos'))
btn_cos.grid(row=6, column=1)
btn_cos.config(font=('verdana',14))

btn_tan=Button(root,text='tan',bg='#00a65a', fg='#505050', width=4, height=1,command=lambda:scientific_operation('tan') )
btn_tan.grid(row=6, column=2)
btn_tan.config(font=('verdana',14))

btn_log=Button(root,text='log',bg='#00a65a', fg="#3A3A3A", width=4, height=1,command=lambda:scientific_operation('log') )
btn_log.grid(row=6, column=3)
btn_log.config(font=('verdana',14))

btn_ln=Button(root,text='ln',bg='#00a65a', fg="#3A3A3A", width=4, height=1,command=lambda:scientific_operation('ln'))
btn_ln.grid(row=6, column=4)
btn_ln.config(font=('verdana',14))

root.mainloop()