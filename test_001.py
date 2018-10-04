from tkinter import *
root = Tk()
root.title('Calculator')
root.geometry('400x500')
bac = Button(root,text='AC',font='黑体',bg='orange',relief=RAISED,fg='blue',command=lambda:getdata('AC')).place(x=0,y=250,width=100,height=50)
bbk = Button(root,text='<--',font='黑体',command=lambda:getdata('<--')).place(x=100,y=250,width=100,height=50)
bmu = Button(root,text='×',font='黑体',command=lambda:getdata('*')).place(x=200,y=250,width=100,height=50)
bmi = Button(root,text='÷',font='黑体',command=lambda:getdata('/')).place(x=300,y=250,width=100,height=50)
bco = Button(root,text='%',font='黑体',command=lambda:getdata('%')).place(x=0,y=450,width=100,height=50)
sub = Button(root,text='-',font='黑体',command=lambda:getdata('-')).place(x=300,y=300,width=100,height=50)
pus = Button(root,text='+',font='黑体',command=lambda:getdata('+')).place(x=300,y=350,width=100,height=50)
poi = Button(root,text='.',font=('黑体',20),command=lambda:getdata('.')).place(x=200,y=450,width=100,height=50)
equ = Button(root,text='=',font=('黑体',30),bg='orange',relief=RAISED,command=lambda:calculate()).place(x=300,y=400,width=100,height=100)
b1  = Button(root,text='1',font='黑体',relief=RAISED,activebackground='red',command=lambda:getdata('1')).place(x=0,y=400,width=100,height=50)
b2  = Button(root,text='2',font='黑体',relief=RAISED,activebackground='orange',command=lambda:getdata('2')).place(x=100,y=400,width=100,height=50)
b3  = Button(root,text='3',font='黑体',relief=RAISED,activebackground='yellow',command=lambda:getdata('3')).place(x=200,y=400,width=100,height=50)
b4  = Button(root,text='4',font='黑体',relief=RAISED,activebackground='green',command=lambda:getdata('4')).place(x=0,y=350,width=100,height=50)
b5  = Button(root,text='5',font='黑体',relief=RAISED,activebackground='lightseagreen',command=lambda:getdata('5')).place(x=100,y=350,width=100,height=50)
b6  = Button(root,text='6',font='黑体',relief=RAISED,activebackground='blue',command=lambda:getdata('6')).place(x=200,y=350,width=100,height=50)
b7  = Button(root,text='7',font='黑体',relief=RAISED,activebackground='purple',command=lambda:getdata('7')).place(x=0,y=300,width=100,height=50)
b8  = Button(root,text='8',font='黑体',relief=RAISED,activebackground='black',command=lambda:getdata('8')).place(x=100,y=300,width=100,height=50)
b9  = Button(root,text='9',font='黑体',relief=RAISED,activebackground='white',command=lambda:getdata('9')).place(x=200,y=300,width=100,height=50)
b0  = Button(root,text='0',font='黑体',relief=RAISED,activebackground='pink',command=lambda:getdata('0')).place(x=100,y=450,width=100,height=50)
result = StringVar()
result1 = StringVar()
result2 =list()
result1.set('冬冬牌洗衣机')
result.set('胖冬没有洗衣机')
label = Label(root,font=('繁体',20),textvariable=result,fg='lime',bg='black').place(y=150,width=400,height=100)
label1 = Label(root,font=('繁体',20),textvariable=result1,fg='skyblue',bg='lemonchiffon').place(y=50,width=400,height=100)
formu = list()
def getdata(data):
    global formu,result2
    if data!='AC' and data!='<--':
        formu.append(data)
    if data:
        if len(formu) == 0:
            result1.set(data)
        else:
            if len(result2)==0:
                message = ''.join(formu)
            else:
                message = str(result2[-1])+''.join(formu)
            result1.set(message)
    if data == 'AC':
        result.set('你买得起洗衣机吗')
        result1.set('一辉也没有洗衣机')
        formu.clear()
        result2.clear()
    if data == '<--':
        try:
            result.set(result2[-2])
            result2.pop(-1)
        except:
            result.set('但你可以让他手洗')
            result1.set('剑剑只有洗衣液')
            formu.clear()
            result2.clear()
    if data.isdigit():
        result.set(data)
def calculate():
    global formu,result2
    if len(result2) !=0:
        try:
            if formu[0].isdigit():
                pass
            else:
                formula =''.join(formu)
                result1.set(str(result2[-1])+formula)
                result2.append(eval(str(result2[-1])+formula))
                result.set(result2[-1])
                formu.clear()
        except:
            pass
    if len(formu) == 0 and len(result2)==0:
        result.set('前提是你有洗衣机')
        result1.set('我有个洗衣球')
    else:
        if len(formu)!=0:
            if formu[0] == '.':
                try:
                    formula = '0'+''.join(formu)
                    result2.append(eval(formula))
                    result.set(eval(formula))
                    result1.set(formula)
                    formu.clear()
                except:
                    result.set('请输入正确算式')
                    result1.set('ERROR!')
            else:
                try:
                    formula =''.join(formu)
                    result2.append(eval(formula))
                    result1.set(formula)
                    result.set(eval(formula))
                    formu.clear()
                except:
                    result.set('能不能好好写算式')
                    result1.set('ERROR!')
root.mainloop()