from tkinter import *

root = Tk()
root.title(' Calculadora de resistencia de 4 bandas Ω ')
root.geometry('400x200')

def show1():
    global resistencia
    if color1.get() == 'Negro[0]':
        resistencia = 0
    if color1.get() == 'Cafe[1]':
        resistencia = 1
    if color1.get() == 'Rojo[2]':
        resistencia = 2
    if color1.get() == 'Naranja[3]':
        resistencia = 3
    if color1.get() == 'Amarillo[4]':
        resistencia = 4
    if color1.get() == 'Verde[5]':
        resistencia = 5
    if color1.get() == 'Azul[6]':
        resistencia = 6
    if color1.get() == 'Violeta[7]':
        resistencia = 7
    if color1.get() == 'Gris[8]':
        resistencia = 8
    if color1.get() == 'Blanco[9]':
        resistencia = 9


def show2():
    global resistencia2
    if color2.get() == 'Negro[0]':
        resistencia2 = 0
    if color2.get() == 'Cafe[1]':
        resistencia2 = 1
    if color2.get() == 'Rojo[2]':
        resistencia2 = 2
    if color2.get() == 'Naranja[3]':
        resistencia2 = 3
    if color2.get() == 'Amarillo[4]':
        resistencia2 = 4
    if color2.get() == 'Verde[5]':
        resistencia2 = 5
    if color2.get() == 'Azul[6]':
        resistencia2 = 6
    if color2.get() == 'Violeta[7]':
        resistencia2 = 7
    if color2.get() == 'Gris[8]':
        resistencia2 = 8
    if color2.get() == 'Blanco[9]':
        resistencia2 = 9


def show3():
    global resistencia3
    if color3.get() == 'Negro[x1Ω]':
        resistencia3 = 1
    if color3.get() == 'Cafe[x10Ω]':
        resistencia3 = 10
    if color3.get() == 'Rojo[x100Ω]':
        resistencia3 = 100
    if color3.get() == 'Naranja[x1KΩ]':
        resistencia3 = 1000
    if color3.get() == 'Amarillo[x10KΩ]':
        resistencia3 = 10000
    if color3.get() == 'Verde[x100KΩ]':
        resistencia3 = 100000
    if color3.get() == 'Azul[x1MΩ]':
        resistencia3 = 1000000
    if color3.get() == 'Violeta[x10MΩ]':
        resistencia3 = 10000000
    if color3.get() == 'Gris[x100MΩ]':
        resistencia3 = 1000000
    if color3.get() == 'Blanco[x1GΩ]':
        resistencia3 = 1000000000

def show4():
    global resistencia4
    if color4.get() == 'Cafe[±1%]':
        resistencia4 = '±1%'
    if color4.get() == 'Rojo[±2%]':
        resistencia4 = '±2%'
    if color4.get() == 'Verde[±0.5%]':
        resistencia4 = '±0.5%'
    if color4.get() == 'Azul[±0.25%]':
        resistencia4 = '±0.25%'
    if color4.get() == 'Violeta[±0.1%]':
        resistencia4 = '±0.1%'
    if color4.get() == 'Gris[±0.05%]':
        resistencia4 = '±0.05%'
    if color4.get() == 'Oro[±5%]':
        resistencia4 = '±5%'
    if color4.get() == 'Plata[±10%]':
        resistencia4 = '±10%'

def calcular():
    show1()
    show2()
    show3()
    show4()
    number = [resistencia,resistencia2]
    strings = [str(integer) for integer in number]
    a_string = ''.join(strings)
    an_integer = int(a_string)
    multiplicador = resistencia3
    final = an_integer*multiplicador

    print(an_integer)
    print(final)
    mostrar = Label(root,text = 'Valor de la resistencia:')
    mostrar.grid(row=6,column=1)
    mostrar2 = Label(root,text =final)
    mostrar2.grid(row=7,column=1)
    mostrar3 = Label(root,text='Ω')
    mostrar3.grid(row=7,column=2)
    mostrar4 = Label(root,text=resistencia4)
    mostrar4.grid(row=7,column=3)
    return

options = [
    "Negro[0]",
    "Cafe[1]",
    "Rojo[2]",
    "Naranja[3]",
    "Amarillo[4]",
    "Verde[5]",
    "Azul[6]",
    "Violeta[7]",
    "Gris[8]",
    "Blanco[9]",
]
options2 = [
    "Negro[x1Ω]",
    "Cafe[x10Ω]",
    "Rojo[x100Ω]",
    "Naranja[x1KΩ]",
    "Amarillo[x10KΩ]",
    "Verde[x100KΩ]",
    "Azul[x1MΩ]",
    "Violeta[x10MΩ]",
    "Gris[x100MΩ]",
    "Blanco[x1GΩ]",
]
options3 = [
    "Cafe[±1%]",
    "Rojo[±2%]",
    "Verde[±0.5%]",
    "Azul[±0.25%]",
    "Violeta[±0.1%]",
    "Gris[±0.05%]",
    "Oro[±5%]",
    "Plata[±10%]"
]


color1 = StringVar()
color1.set(options[0])
color2 = StringVar()
color2.set(options[0])
color3 = StringVar()
color3.set(options2[0])
color4 = StringVar()
color4.set(options3[0])


bd1 = OptionMenu(root, color1, *options)
bd1.grid(row=0, column=2)

bd2 = OptionMenu(root, color2, *options)
bd2.grid(row=1, column=2)

bd3 = OptionMenu(root, color3, *options2)
bd3.grid(row=2, column=2)

bd4 = OptionMenu(root, color4, *options3)
bd4.grid(row=3, column=2)

boton = Button(root,text='Calcular',command = calcular)
boton.grid(row = 5, column = 0)

banda1 = Label(root, text='1.° banda de color').grid(row=0, column=0)
banda2 = Label(root, text='2.° banda de color').grid(row=1, column=0)
banda3 = Label(root, text='Multiplicador').grid(row=2, column=0)
banda4 = Label(root, text='Tolerancia').grid(row=3, column=0)


root.mainloop()
