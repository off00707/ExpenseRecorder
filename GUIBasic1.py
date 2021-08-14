import tkinter as tk
from tkinter import ttk,messagebox
from tkinter import *
import csv
from datetime import datetime
# root window
GUI = tk.Tk()
GUI.geometry('500x600')
GUI.title('โปรเเกรมบันทึกค่าใช้จ่าย v.1.0 by off')


#-----------manu---------------
menubar=Menu(GUI)
GUI.config(menu=menubar)

#-----------file menu ---------
filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='Import CSV')
filemenu.add_command(label='Export to googlesheet')


#----------------help-----------------
def About():
    print('about menu')
    messagebox.showinfo('About','สวัสดีครับนี่คือโปรเเกรมบันทึกข้อมูล\nสนใจบริจากเราใหม? ขอ 1 BTC ก็พอเเล้ว\nBTC Addess: abc')

helpmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='help')
helpmenu.add_command(label='about',command=About)


def Donate():
    messagebox.showinfo('Donate','ขอ 1 BTC ก็พอเเล้ว\nBTC Addess: abc')

donatemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Donate',menu=donatemenu)
donatemenu.add_command(label='บริจาค',command=Donate)
donatemenu.add_command(label='ผู้จัดทำ')


#-------------------------------
# create a notebook
Tab = ttk.Notebook(GUI)  


# create frames
T1 = Frame(Tab)#ใส่ ,width=400 ,height=400
T2 = Frame(Tab)
Tab.pack(fill=BOTH, expand=1) #fill=x คือขยายเเนวเเกน x

icon_t1=PhotoImage(file='t1_expense.png')
icon_t2=PhotoImage(file='t2_expenselist.png')
B1_save=PhotoImage(file='Save.png')

# add frames to notebook
Tab.add(T1, text=f'{"เพิ่มค่าใช้จ่าย":^{30}}',image=icon_t1,compound='top') #ใส่ f string
Tab.add(T2, text=f'{"ค่าใช้จ่ายทั้งหมด":^{30}}',image=icon_t2,compound='top') #.subsample(2) =ย่อรูป


F1=Frame(T1)
#F1.place(x=100,y=50)
F1.pack() #คือไม่ฟิกหน้าจอเมื่อขยายจอจะอยุู่ตรงกลาง

#days = {'Mon':'จันทร์',
 #       'Tue':'อังคาร',
 #       'Wed':'พุธ',
 #       'Thu':'พฤหัสบดี',
 #      'Fri':'ศุกร์',
 #     'Sat':'เสาร์',
 #     'Sun':'อาทิตย์'}

def Save(event=None):
    expense = v_expense.get()
    price =v_price.get()
    num = v_num.get()
   # if expense=='' or price=='' or num=='' :
        #print('nodata')
        #messagebox.showerror('ERROR','กรุณากรอกข้อมูลใหม่ คุณกรอกข้อมูลไม่ครบ')
        #return
    if expense=='':
        print('nodata')
        messagebox.showerror('ERROR','กรุณากรอกรายการ')
        return
    elif price=='':
        print('nodata')
        messagebox.showerror('ERROR','กรุณากรอกราคา')
        return
    elif num=='':
        num=1

    try:        
        now = datetime.now()
        total=int(price)*int(num)
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        # .get() คือดึงค่ามาจาก v_expense=StringVar()
        print(' เวลาที่บันทึก {} รายการ : {} ราคา {} บาท จำนวน {} ชิ้น รวม {} บาท'.format(date_time,expense,price,num,total))
        text = 'รายการ : {} ราคา {} บาท\n '.format(expense,price)
        text = text+'จำนวน {} ชิ้น รวม {} บาท '.format(num,total)
        v_result.set(text)

        #Clear ข้อมูลเก่า
        v_expense.set('')
        v_price.set('')
        v_num.set('')

        #บันทึกข้อมูลลง csv อย่าลืม import csv
        with open('savedata.csv','a',encoding='utf-8',newline='') as f:
            #with คือ คำสั่งเปิดไฟล์เเล้วปิอัติโนมัติ
            # 'a' คือ การบันทึกข้อมูลเรื่อยๆๆเพิ่มข้อมูลต่อจากข้อมูลเก่า
            # newline='' คือการทำให้ข้อมูลไม่มีบรรทัดว่าง
            fw=csv.writer(f) #เพื่อสร้างฟังชั่นสำหรับเขียนข้อมูล
            data=[date_time,expense,price,num,total]
            fw.writerow(data)
        #ทำให้เคอเซอร์กลับไปตำแหน่งช่องกรอก E1
        E1.focus()
        update_table()
    except Exception as e:
        print('ERROR',e)
        messagebox.showerror('ERROR','กรุณากรอกข้อมูลใหม่ คุณกรอกข้อมูลไม่ถูกต้อง')
       # messagebox.showwarning('ERROR','กรุณากรอกข้อมูลใหม่ คุณกรอกข้อมูลไม่ถูกต้อง')
       # messagebox.showinfo('ERROR','กรุณากรอกข้อมูลใหม่ คุณกรอกข้อมูลไม่ถูกต้อง')
         #Clear ข้อมูลเก่า
        v_expense.set('')
        v_price.set('')
        v_num.set('')
        print(e)
   
# ทำให้สามารถกด Enter ได้
GUI.bind('<Return>',Save) #ต้องเพิ่มใน def Save(event=None) ด้วย
    
FONT1 = (None,20) #None เปลี่ยนเป็น 'Angsana New' 20 คือขนาด font 

#-------------------image-----------------

main_icon=PhotoImage(file='iconmoney.png')
Mainicon=Label(F1,image=main_icon)
Mainicon.pack()


#-----------------------------------------



#-------------------text1-----------------
L = ttk.Label(F1,text='รายการใช้จ่าย',font=FONT1).pack() #L คือ Label
v_expense = StringVar() #ตัวเเปรเก็บค่าช่อง Textbox 
# StringVar() คือ ตัวเเปรพิเศษสำหรับเก็บข้อมูลใน GUT
E1 = ttk.Entry(F1,textvariable=v_expense,font=FONT1) #Textbox
E1.pack()
#-----------------------------------------

#-------------------text2-----------------
L = ttk.Label(F1,text='ราคา (บาท)',font=FONT1).pack() #L คือ Label
v_price = StringVar() #ตัวเเปรเก็บค่าช่อง Textbox 
# StringVar() คือ ตัวเเปรพิเศษสำหรับเก็บข้อมูลใน GUT
E2 = ttk.Entry(F1,textvariable=v_price,font=FONT1) #Textbox
E2.pack()
#-----------------------------------------

#-------------------text3-----------------
L = ttk.Label(F1,text='จำนวน (ชิ้น)',font=FONT1).pack() #L คือ Label
v_num = StringVar() #ตัวเเปรเก็บค่าช่อง Textbox 
# StringVar() คือ ตัวเเปรพิเศษสำหรับเก็บข้อมูลใน GUT
E3 = ttk.Entry(F1,textvariable=v_num,font=FONT1) #Textbox
E3.pack()
#-----------------------------------------



B2=ttk.Button(F1,text=f'{"Save": >{8}}',image=B1_save,compound='left',command=Save)
B2.pack(ipadx=50,ipady=10,pady=20)


v_result=StringVar()
v_result.set('----------ผลลัพธ์--------')
result=ttk.Label(F1,textvariable=v_result,font=FONT1)
result.pack(pady=20)

#-----------------------Tap2---------------------------------
def read_csv():
    with open('savedata.csv',newline='',encoding='utf-8') as f:
        fr = csv.reader(f)
        #print(fr)
        data=list(fr)
    return data
        # print(data)
        # print(data[0][0])
        # for a,b,c,d,e in data:
        #     print(d[0])

# rs=read_csv()
# print(rs[0])

#-----------Table------------
L = ttk.Label(T2,text='ตารางแสดงผลลัพท์ทั้งหมด',font=FONT1).pack(pady=20) #L คือ Label

header=['วัน-เวลา','รายการ','ค่าใช้จ่าย','จำนวน','รวม']
resulttable = ttk.Treeview(T2,columns=header,show='headings',height=10)
resulttable.pack()
# for i in range(len(header)):
#     resulttable.heading(header[i],text=header[i])
for h in header:
    resulttable.heading(h,text=h)

headerwidth=[150,170,80,80,80]
for h,w in zip(header,headerwidth):
    resulttable.column(h,width=w)

# resulttable.insert('',0,value=['จันทร์','น้ำดื่ม',30,5,150])
# resulttable.insert('','end',value=['จันทร์','น้ำดื่ม',30,5,150])

def update_table():
    resulttable.delete(*resulttable.get_children())
    data=read_csv() 
    for d in data:
        resulttable.insert('',0,value=d)
   

update_table()
print('GET CHILD:',resulttable.get_children())






GUI.bind('<Tab>',lambda x: E2.focus())
GUI.mainloop()
