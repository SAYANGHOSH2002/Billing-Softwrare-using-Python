from tkinter import*
import math,random
from tkinter import messagebox
class Bill_App:
    def  __init__(self , root):
        self.root=root
        self.root.geometry=("1400*800+0+0")
        self.root.title=("Billing Software")
        bg_color="#000000"
        #=======BILLING SOFTWARE FRAME==========
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold","underline"),pady=2).pack(fill=X)
        #========VARIABLES===========
        #========BURGERS=========
        self.lun_bur=IntVar()
        self.chicken_burger=IntVar()
        self.King_Burger=IntVar()
        self.Chargrilled_Burger=IntVar()
        self.Cheeseburger=IntVar()
        #========CHOWMEINS========
        self.Chicken_Chowmein=IntVar()
        self.Fried_Noodles=IntVar()
        self.Sichuan_Noodles=IntVar()
        self.Drunken_Noodles=IntVar()
        self.Paneer_Noodles=IntVar()
        #=======ROLLS=============
        self.Mutton_Roll=IntVar()
        self.Paneer_Roll=IntVar()
        self.Cheese_Egg_Roll=IntVar()
        self.Double_Egg_Roll=IntVar()
        self.Egg_Chicken_Roll=IntVar()
        #========CUSTOMER=======
        self.Customer_Name=StringVar()
        self.Phone_No=StringVar()
        self.Bill_No=StringVar()
        x=random.randint(500,9999)
        self.Bill_No.set(int(x))
        self.search_bill=StringVar()
        self.bill_data=StringVar()
        #=========BILLS & TAX=======
        self.Burger_Price=StringVar()
        self.Chowmein_Price=StringVar()
        self.Roll_Price=StringVar()

        self.Burger_Tax=StringVar()
        self.Chowmein_Tax=StringVar()
        self.Roll_Tax=StringVar()

        
        #=======CUSTOMER DETAILS FRAME===========
        F1=LabelFrame(self.root,text="Customer Details",bd=12,relief=GROOVE,bg=bg_color,fg="gold",font=("times new roman",20,"bold"))
        F1.place(x=0,y=80,relwidth=1)

        cname=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0)
        cname_txt=Entry(F1,width=20,textvariable=self.Customer_Name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        cphno=Label(F1,text="Phone No.",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=2)
        cphno_txt=Entry(F1,width=20,textvariable=self.Phone_No,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)
        cbill=Label(F1,text="Bill No.",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=4)
        cbill_txt=Entry(F1,width=20,textvariable=self.Bill_No,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)
        c_button=Button(F1,width=20,text="Search",font="arial 15 bold",bd=7).grid(row=0,column=6,pady=5,padx=10)

        #========BURGER FRAME===========
        F2=LabelFrame(self.root,text="Burgers",bd=12,relief=GROOVE,bg=bg_color,fg="gold",font=("times new roman",20,"bold"))
        F2.place(x=0,y=170,width=325,height=365)

        s1name=Label(F2,text="Luger Burger",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=0,column=0,sticky="W")
        s1name_txt=Entry(F2,width=5,textvariable=self.lun_bur,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10,sticky="E")
        s2name=Label(F2,text="Chicken Burger",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=1,column=0,sticky="W")
        s2name_txt=Entry(F2,width=5,textvariable=self.chicken_burger,font="arial 15",bd=7,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10,sticky="E")
        s3name=Label(F2,text="King Burger",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=2,column=0,sticky="W")
        s3name_txt=Entry(F2,width=5,textvariable=self.King_Burger,font="arial 15",bd=7,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10,sticky="E")
        s4name=Label(F2,text="Chargrilled Burger",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=3,column=0,sticky="W")
        s4name_txt=Entry(F2,width=5,textvariable=self.Chargrilled_Burger,font="arial 15",bd=7,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10,sticky="E")
        s5name=Label(F2,text="Cheeseburger",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=4,column=0,sticky="W")
        s5name_txt=Entry(F2,width=5,textvariable=self.Cheeseburger,font="arial 15",bd=7,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10,sticky="E")

        #========CHOWMEIN FRAME===========
        F2=LabelFrame(self.root,text="Chowmein",bd=12,relief=GROOVE,bg=bg_color,fg="gold",font=("times new roman",20,"bold"))
        F2.place(x=320,y=170,width=325,height=365)

        c1name=Label(F2,text="Chicken Chowmein",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=0,column=0,sticky="W")
        c1name_txt=Entry(F2,width=5,textvariable=self.Chicken_Chowmein,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10,sticky="E")
        c2name=Label(F2,text="Fried Noodles",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=1,column=0,sticky="W")
        c2name_txt=Entry(F2,width=5,textvariable=self.Fried_Noodles,font="arial 15",bd=7,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10,sticky="E")
        c3name=Label(F2,text="Sichuan Noodles",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=2,column=0,sticky="W")
        c3name_txt=Entry(F2,width=5,textvariable=self.Sichuan_Noodles,font="arial 15",bd=7,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10,sticky="E")
        c4name=Label(F2,text="Drunken Noodles",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=3,column=0,sticky="W")
        c4name_txt=Entry(F2,width=5,textvariable=self.Drunken_Noodles,font="arial 15",bd=7,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10,sticky="E")
        c5name=Label(F2,text="Paneer Noodles",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=4,column=0,sticky="W")
        c5name_txt=Entry(F2,width=5,textvariable=self.Paneer_Noodles,font="arial 15",bd=7,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10,sticky="E")

        #========ROLL FRAME===========
        F3=LabelFrame(self.root,text="Roll",bd=12,relief=GROOVE,bg=bg_color,fg="gold",font=("times new roman",20,"bold"))
        F3.place(x=635,y=170,width=325,height=365)

        r1name=Label(F3,text="Mutton Kathi Roll",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=0,column=0,sticky="W")
        r1name_txt=Entry(F3,width=5,textvariable=self.Mutton_Roll,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10,sticky="E")
        r2name=Label(F3,text="Paneer Tikka Roll",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=1,column=0,sticky="W")
        r2name_txt=Entry(F3,width=5,textvariable=self.Paneer_Roll,font="arial 15",bd=7,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10,sticky="E")
        r3name=Label(F3,text="Cheese Egg Roll",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=2,column=0,sticky="W")
        r3name_txt=Entry(F3,width=5,textvariable=self.Cheese_Egg_Roll,font="arial 15",bd=7,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10,sticky="E")
        r4name=Label(F3,text="Double Egg Roll",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=3,column=0,sticky="W")
        r4name_txt=Entry(F3,width=5,textvariable=self.Double_Egg_Roll,font="arial 15",bd=7,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10,sticky="E")
        r5name=Label(F3,text="Egg Chicken Roll",bg=bg_color,fg="lightgreen",font=("times new roman",18,"bold")).grid(row=4,column=0,sticky="W")
        r5name_txt=Entry(F3,width=5,textvariable=self.Egg_Chicken_Roll,font="arial 15",bd=7,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10,sticky="E")

        #===========BILL AREA============
        F4=Frame(self.root ,bd=12,relief=GROOVE)
        F4.place(x=950,y=185,width=420,height=355)
        b_title=Label(F4,text="Bill Area",font=("times new roman",18,"bold"),bd=7,relief=GROOVE,fg="black").pack(fill=X)
        scroll_y=Scrollbar(F4,orient=VERTICAL)
        self.txtarea=Text(F4,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #============Bill Button==============
        F5=LabelFrame(self.root,text="Bill Menu",bd=12,relief=GROOVE,bg=bg_color,fg="gold",font=("times new roman",20,"bold"))
        F5.place(x=0,y=528,relwidth=1,height=180)

        B1_name=Label(F5,text="Total Burger Price",bg=bg_color,fg="lightblue",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=0,pady=1,sticky="W")
        B1_name_txt=Entry(F5,width=8,textvariable=self.Burger_Price,font="arial 10",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=1,padx=10,sticky="E")
        B2_name=Label(F5,text="Total Chowmein Price",bg=bg_color,fg="lightblue",font=("times new roman",15,"bold")).grid(row=1,column=0,padx=0,pady=1,sticky="W")
        B2_name_txt=Entry(F5,width=8,textvariable=self.Chowmein_Price,font="arial 10",bd=7,relief=SUNKEN).grid(row=1,column=1,pady=1,padx=10,sticky="E")
        B3_name=Label(F5,text="Total Roll Price",bg=bg_color,fg="lightblue",font=("times new roman",15,"bold")).grid(row=2,column=0,padx=0,pady=1,sticky="W")
        B3_name_txt=Entry(F5,width=8,textvariable=self.Roll_Price,font="arial 10",bd=7,relief=SUNKEN).grid(row=2,column=1,pady=1,padx=10,sticky="E")

        B1_name=Label(F5,text="Burger Tax",bg=bg_color,fg="lightblue",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=0,pady=1,sticky="W")
        B1_name_txt=Entry(F5,width=8,textvariable=self.Burger_Tax,font="arial 10",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=1,padx=10,sticky="E")
        B2_name=Label(F5,text="Chowmein Tax",bg=bg_color,fg="lightblue",font=("times new roman",15,"bold")).grid(row=1,column=2,padx=0,pady=1,sticky="W")
        B2_name_txt=Entry(F5,width=8,textvariable=self.Chowmein_Tax,font="arial 10",bd=7,relief=SUNKEN).grid(row=1,column=3,pady=1,padx=10,sticky="E")
        B3_name=Label(F5,text="Roll Tax",bg=bg_color,fg="lightblue",font=("times new roman",15,"bold")).grid(row=2,column=2,padx=0,pady=1,sticky="W")
        B3_name_txt=Entry(F5,width=8,textvariable=self.Roll_Tax,font="arial 10",bd=7,relief=SUNKEN).grid(row=2,column=3,pady=1,padx=10,sticky="E")

        btn=Frame(F5,bd=12,relief=GROOVE,bg=bg_color)
        btn.place(x=520,width=800,height=130)
        total_btn=Button(btn,command=self.total,text="Total",bd=7,width=9,height=2,font=("arial 15 bold")).grid(row=0,column=0,padx=10,pady=10)
        total_btn=Button(btn,command=self.bill_area,text="Generate Bill",bd=7,width=10,height=2,font=("arial 15 bold")).grid(row=0,column=1,padx=10,pady=10)
        total_btn=Button(btn,command=self.save_bill,text="Save Bill",bd=7,width=9,height=2,font=("arial 15 bold")).grid(row=0,column=2,padx=10,pady=5)
        total_btn=Button(btn,command=self.clear,text="Clear",bd=7,width=9,height=2,font=("arial 15 bold")).grid(row=0,column=3,padx=10,pady=10)
        total_btn=Button(btn,command=self.bill_exit,text="Exit",bd=7,width=9,height=2,font=("arial 15 bold")).grid(row=0,column=4,padx=10,pady=5)
        self.wel_bill()
        
    def total(self):
        self.lb=float(self.lun_bur.get()*40)
        self.cb=float(self.chicken_burger.get()*40)
        self.kb=float(self.King_Burger.get()*40)
        self.chb=float(self.Chargrilled_Burger.get()*40)
        self.csb=float(self.Cheeseburger.get()*40)
        self.total_burger_price=float(
                                                    (self.lb)+
                                                    (self.cb)+
                                                    (self.kb)+
                                                    (self.chb)+
                                                    (self.csb)
                                                )
        self.Burger_Price.set("Rs."+str(self.total_burger_price))
        self.b_tax=float(self.total_burger_price*0.1)
        self.Burger_Tax.set("Rs."+str(self.b_tax))

        self.cc=float(self.Chicken_Chowmein.get()*60)
        self.fn=float(self.Fried_Noodles.get()*60)
        self.sn=float(self.Sichuan_Noodles.get()*60)
        self.dn=float(self.Drunken_Noodles.get()*60)
        self.pn=float(self.Paneer_Noodles.get()*60)
        self.total_chowmein_price=float(
                                                        (self.cc)+
                                                        (self.fn)+
                                                        (self.sn)+
                                                        (self.dn)+
                                                        (self.pn)
                                                    )
        self.Chowmein_Price.set("Rs."+str(self.total_chowmein_price))
        self.c_tax=float(self.total_chowmein_price*0.1)
        self.Chowmein_Tax.set("Rs."+str(self.c_tax))


        self.mr=float(self.Mutton_Roll.get()*60)
        self.pr=float(self.Paneer_Roll.get()*60)
        self.er=float(self.Cheese_Egg_Roll.get()*60)
        self.der=float(self.Double_Egg_Roll.get()*60)
        self.cr=float(self.Egg_Chicken_Roll.get()*60)
        self.total_roll_price=float(
                                                        (self.mr)+
                                                        (self.pr)+
                                                        (self.er)+
                                                        (self.der)+
                                                        (self.cr)
                                        )
        self.Roll_Price.set("Rs."+str(self.total_roll_price))
        self.r_tax=float(self.total_roll_price*0.05)
        self.Roll_Tax.set("Rs."+str(self.r_tax))

    def wel_bill(self):
        self.txtarea.delete(1.0,END)
        self.txtarea.insert(END,"\t   Welcome To Python Program")
        self.txtarea.insert(END,f"\n Bill No.:  {self.Bill_No.get()}")
        self.txtarea.insert(END,f"\n Customer Name: {self.Customer_Name.get()}")
        self.txtarea.insert(END,f"\n Phone Number: {self.Phone_No.get()}")

        self.txtarea.insert(END,f"\n==============================================")
        self.txtarea.insert(END,f"\n   Product name     Quantity       Price       ")
        self.txtarea.insert(END,f"\n==============================================")
    def bill_area(self):
        if self.Customer_Name.get()=="" or self.Phone_No.get()=="":
            messagebox.showerror("Error","Customer details are must")
        else:
            self.wel_bill()
            if self.lun_bur.get()!=0:
                self.txtarea.insert(END,f"\n Luber Burger\t\t\t{self.lun_bur.get()}\t\t{self.lb}")
            if self.chicken_burger.get()!=0:
                self.txtarea.insert(END,f"\n Chicken Burger\t\t\t{self.chicken_burger.get()}\t\t{self.cb}")
            if self.King_Burger.get()!=0:
                self.txtarea.insert(END,f"\n King Burger\t\t\t{self.King_Burger.get()}\t\t{self.kb}")
            if self.Chargrilled_Burger.get()!=0:
                self.txtarea.insert(END,f"\n Chargrilled Burger\t\t\t{self.Chargrilled_Burger.get()}\t\t{self.chb}")
            if self.Cheeseburger.get()!=0:
                self.txtarea.insert(END,f"\n Cheeseburger\t\t\t{self.Cheeseburger.get()}\t\t{self.csb}")
            
            if self.Chicken_Chowmein.get()!=0:
                self.txtarea.insert(END,f"\n Chicken Chowmein\t\t\t{self.Chicken_Chowmein.get()}\t\t{self.cc}")
            if self.Fried_Noodles.get()!=0:
                self.txtarea.insert(END,f"\n Fried Noodles\t\t\t{self.Fried_Noodles.get()}\t\t{self.fn}")
            if self.Sichuan_Noodles.get()!=0:
                self.txtarea.insert(END,f"\n Sichuan Noodles\t\t\t{self.Sichuan_Noodles.get()}\t\t{self.sn}")
            if self.Drunken_Noodles.get()!=0:
                self.txtarea.insert(END,f"\n Drunken Noodles\t\t\t{self.Drunken_Noodles.get()}\t\t{self.dn}")
            if self.Paneer_Noodles.get()!=0:
                self.txtarea.insert(END,f"\n Paneer Noodles\t\t\t{self.Paneer_Noodles.get()}\t\t{self.pn}")

            if self.Mutton_Roll.get()!=0:
                self.txtarea.insert(END,f"\n Mutton Roll\t\t\t{self.Mutton_Roll.get()}\t\t{self.mr}")
            if self.Paneer_Roll.get()!=0:
                self.txtarea.insert(END,f"\n Paneer Roll\t\t\t{self.Paneer_Roll.get()}\t\t{self.pr}")
            if self.Cheese_Egg_Roll.get()!=0:
                self.txtarea.insert(END,f"\n Cheese Egg Roll\t\t\t{self.Cheese_Egg_Roll.get()}\t\t{self.er}")
            if self.Double_Egg_Roll.get()!=0:
                self.txtarea.insert(END,f"\n Double Egg Roll\t\t\t{self.Double_Egg_Roll.get()}\t\t{self.der}")
            if self.Egg_Chicken_Roll.get()!=0:
                self.txtarea.insert(END,f"\n Egg Chicken Roll\t\t\t{self.Egg_Chicken_Roll.get()}\t\t{self.cr}")
            self.tax=float((self.b_tax)+(self.c_tax)+(self.r_tax))
            self.txtarea.insert(END,f"\n Tax\t\t\t\t\t {self.tax}")
            self.txtarea.insert(END,f"\n==============================================")
            self.total=str((self.total_burger_price)+(self.total_chowmein_price)+(self.total_roll_price)+(self.tax))
            self.txtarea.insert(END,f"\n Total\t\t\t\t\t{(self.total)}")
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            fp=open("Bills/"+str(self.Bill_No.get()),".txt","w+")
            fp.write(self.bill_data)
            
            fp.close()
        else:
            return
    def clear(self):
        op=messagebox.askyesno("Clear","Do you really want to clear?")
        if op>0:
            #========BURGERS=========
            self.lun_bur.set(0)
            self.chicken_burger.set(0)
            self.King_Burger.set(0)
            self.Chargrilled_Burger.set(0)
            self.Cheeseburger.set(0)
            #========CHOWMEINS========
            self.Chicken_Chowmein.set(0)
            self.Fried_Noodles.set(0)
            self.Sichuan_Noodles.set(0)
            self.Drunken_Noodles.set(0)
            self.Paneer_Noodles.set(0)
            #=======ROLLS=============
            self.Mutton_Roll.set(0)
            self.Paneer_Roll.set(0)
            self.Cheese_Egg_Roll.set(0)
            self.Double_Egg_Roll.set(0)
            self.Egg_Chicken_Roll.set(0)
            #========CUSTOMER=======
            self.Customer_Name.set("")
            self.Phone_No.set("")
            self.Bill_No.set("")
            x=random.randint(500,9999)
            self.Bill_No.set(str(x))
            self.search_bill.set("")
            #=========BILLS & TAX=======
            self.Burger_Price.set("")
            self.Chowmein_Price.set("")
            self.Roll_Price.set("")

            self.Burger_Tax.set("")
            self.Chowmein_Tax.set("")
            self.Roll_Tax.set("")

    def bill_exit(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()



    
root=Tk()
obj=Bill_App(root)
root.mainloop()
