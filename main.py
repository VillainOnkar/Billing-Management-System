from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os,random
import tempfile
from time import strftime

class bill_win:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")
        self.root.state("zoomed")
#======================================================variables=================================================
        self.cname=StringVar()
        self.cphone=StringVar()
        self.billno=StringVar()
        self.z=random.randint(1000,9999)
        self.billno.set(self.z)
        self.cemail=StringVar()
        self.searchbill_var=StringVar()
        self.product=StringVar()
        self.price_var=IntVar()
        self.qty=IntVar()
        self.subtotal=StringVar()
        self.tax=StringVar()
        self.total=StringVar()
#=======================================================product categories list==================================
        self.category=["Select Option","Clothing","Lifestyle","Mobiles"]

        #subcategory clothing
        self.subcateclothing=["Pant","Shirt","T-Shirt"]
        self.pant=["Levis","Mufti","Spykar"]
        self.price_levis=5000
        self.price_mufti=7000
        self.price_spykar=8000

        self.shirt=["Peter England","Louis Phillipe","Park Avenue"]
        self.price_PeterEngland=2100
        self.price_LouisPhillipe=2700
        self.price_parkavenue=1740

        self.Tshirt=["Polo","Roadster","Jack&Jones"]
        self.price_polo=1500
        self.price_roadster=1800
        self.price_jackjones=1700
#=================================================================================================
        #subcate lifestyle
        self.subcatelifestyle=["Bath Soap","Face Wash","Hair Oil"]
        
        self.bathsoap=["Santoor","Lux","Lifeboy"]
        self.price_santoor=100
        self.price_lux=150
        self.price_lifeboy=200

        self.facewash=["Garnier","Himalaya","Mastang"]
        self.price_garnier=250
        self.price_himalaya=300
        self.price_mastang=400

        self.Hairoil=["Bajaj","Coconut","Jasmin"]
        self.price_bajaj=500
        self.price_coconut=550
        self.price_jasmin=600
#===============================================================================================================
        #subcatemobiles
        self.subcatemobiles=["Iphone","Samsang","OPPO"]

        self.iphone=["IPhone11","IPhone12","IPhone14"]
        self.price_i11=100000
        self.price_i12=150000
        self.price_i14=200000

        self.samsang=["SamV12","S23","S24"]
        self.price_samv12=120000
        self.price_s23=130000
        self.price_s24=150000

        self.oppo=["Oppof23","Oppov21","Oppo24"]
        self.price_oppo23=25000
        self.price_oppov21=21000
        self.price_oppo24=22000
#================================================================================================================
#================================================image=====================================================
        img_1=Image.open(r"E:\BillingSystem\photos\img1.jpg")
        img_1=img_1.resize((500,130),Image.ANTIALIAS)
        self.demo_1=ImageTk.PhotoImage(img_1)
        lbl1=Label(self.root,image=self.demo_1,bd=0,bg="black")
        lbl1.place(x=0,y=0,width=500,height=130)

        img_2=Image.open(r"E:\BillingSystem\photos\img2.jpg")
        img_2=img_2.resize((500,130),Image.ANTIALIAS)
        self.demo_2=ImageTk.PhotoImage(img_2)
        lbl2=Label(self.root,image=self.demo_2,bd=0,bg="black")
        lbl2.place(x=500,y=0,width=500,height=130)

        img_3=Image.open(r"E:\BillingSystem\photos\img3.jpg")
        img_3=img_3.resize((535,130),Image.ANTIALIAS)
        self.demo_3=ImageTk.PhotoImage(img_3)
        lbl3=Label(self.root,image=self.demo_3,bd=0,bg="black")
        lbl3.place(x=1000,y=0,width=535,height=130)

        lbl_main=Label(self.root,text="BILLING MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),fg="red",bg="white")
        lbl_main.place(x=0,y=130,width=1535,height=45)
#==================================================timer ==========================================
        def time():
            string=strftime("%H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(lbl_main,font=("times new roman",16,"bold"),bg="white",fg="red")
        lbl.place(x=0,y=0,width=150,height=60)
        time()
#======================================================================================================
        mainframe=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        mainframe.place(x=0,y=175,width=1535,height=665)
#=======================================================customer label frame========================================
        #customer label frame
        cust_frame=LabelFrame(mainframe,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="red")
        cust_frame.place(x=10,y=5,width=350,height=140)

        #mobile
        self.lbl_mobile=Label(cust_frame,text="Mobile No:",font=("times new roman",12,"bold"),bg="white")
        self.lbl_mobile.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        self.entry_mobile=ttk.Entry(cust_frame,textvariable=self.cphone,font=("times new roman",10,"bold"),width=24)
        self.entry_mobile.grid(row=0,column=1)

        #name
        self.lbl_name=Label(cust_frame,text="Customer Name:",font=("times new roman",12,"bold"),bg="white")
        self.lbl_name.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        self.entry_name=ttk.Entry(cust_frame,textvariable=self.cname,font=("times new roman",10,"bold"),width=24)
        self.entry_name.grid(row=1,column=1)

        #email
        self.lbl_email=Label(cust_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        self.lbl_email.grid(row=3,column=0,sticky=W,padx=5,pady=2)
        self.entry_email=ttk.Entry(cust_frame,textvariable=self.cemail,font=("times new roman",10,"bold"),width=24)
        self.entry_email.grid(row=3,column=1)

        #product label frame
        product_frame=LabelFrame(mainframe,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
        product_frame.place(x=370,y=5,width=640,height=140)

        #categoery
        self.lbl_categoery=Label(product_frame,text="Select Categories:",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lbl_categoery.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        self.combo_categoery=ttk.Combobox(product_frame,values=self.category,font=("times new roman",10,"bold"),width=24,state="readonly")
        self.combo_categoery.current(0)
        self.combo_categoery.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.combo_categoery.bind("<<ComboboxSelected>>",self.categories)

        #subcategoery
        self.lbl_subcategoery=Label(product_frame,text="Select Subcategory:",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lbl_subcategoery.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        self.combo_subcategoery=ttk.Combobox(product_frame,font=("times new roman",10,"bold"),width=24,state="readonly")
        self.combo_subcategoery.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.combo_subcategoery.bind("<<ComboboxSelected>>",self.productadd)
#=======================================================product label frame=================================================
        #product_name
        self.lbl_product_name=Label(product_frame,text="Product Name:",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lbl_product_name.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        self.combo_product_name=ttk.Combobox(product_frame,textvariable=self.product,font=("times new roman",10,"bold"),width=24,state="readonly")
        self.combo_product_name.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.combo_product_name.bind("<<ComboboxSelected>>",self.price)

        #price
        self.lbl_price=Label(product_frame,text="price:",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lbl_price.grid(row=0,column=2,sticky=W,padx=5,pady=2)
        self.combo_price=ttk.Combobox(product_frame,textvariable=self.price_var,font=("times new roman",10,"bold"),width=24,state="readonly")
        self.combo_price.grid(row=0,column=3,sticky=W,padx=5,pady=2)

        #Quantity
        self.lbl_quantity=Label(product_frame,text="Quantity:",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lbl_quantity.grid(row=1,column=2,sticky=W,padx=5,pady=2)
        self.combo_quantity=ttk.Entry(product_frame,textvariable=self.qty,font=("times new roman",10,"bold"),width=24)
        self.combo_quantity.grid(row=1,column=3,sticky=W,padx=5,pady=2)
#=======================================================middle frame==================================================
        middleframe=Frame(mainframe,bd=10,bg="white")
        middleframe.place(x=10,y=150,width=1000,height=340)

        img_4=Image.open(r"E:\BillingSystem\photos\img4.jpg")
        img_4=img_4.resize((490,340),Image.ANTIALIAS)
        self.demo_4=ImageTk.PhotoImage(img_4)
        lbl4=Label(middleframe,image=self.demo_4,bd=0,bg="black")
        lbl4.place(x=0,y=0,width=490,height=340)

        img_5=Image.open(r"E:\BillingSystem\photos\img5.jpg")
        img_5=img_5.resize((500,340),Image.ANTIALIAS)
        self.demo_5=ImageTk.PhotoImage(img_5)
        lbl5=Label(middleframe,image=self.demo_5,bd=0,bg="black")
        lbl5.place(x=490,y=0,width=500,height=340)
#=======================================================search frame===================================================
        searchframe=Frame(mainframe,bd=2,bg="white")
        searchframe.place(x=1025,y=15,width=500,height=40)

        self.lbl_billno=Label(searchframe,text="Bill Number:",font=("times new roman",12,"bold"),bg="red",fg="white")
        self.lbl_billno.grid(row=0,column=0,sticky=W,padx=1)

        self.searchentry=ttk.Entry(searchframe,textvariable=self.searchbill_var,font=("times new roman",10,"bold"),width=24)
        self.searchentry.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.searchbtn=Button(searchframe,text="SEARCH",command=self.searchbill,font=("times new roman",10,"bold"),bg="orangered",fg="white",activebackground="orangered",activeforeground="white",cursor="hand2",width=15)
        self.searchbtn.grid(row=0,column=2,sticky=W,padx=5,pady=2)


#=================================================frame bill area=======================================================
        rightbillframe=LabelFrame(mainframe,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="red")
        rightbillframe.place(x=1030,y=45,width=480,height=440)

        scrolly=Scrollbar(rightbillframe,orient=VERTICAL)
        self.textarea=Text(rightbillframe,yscrollcommand=scrolly.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #bill counter labelframe
        bottomframe=LabelFrame(mainframe,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
        bottomframe.place(x=0,y=485,width=1520,height=125)

        #subtotal
        self.lbl_subtotal=Label(bottomframe,text="Sub Total:",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lbl_subtotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        self.entry_subtotal=ttk.Entry(bottomframe,textvariable=self.subtotal,font=("times new roman",10,"bold"),width=26)
        self.entry_subtotal.grid(row=0,column=1)

        #tax
        self.lbl_tax=Label(bottomframe,text="Tax:",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lbl_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        self.entry_tax=ttk.Entry(bottomframe,textvariable=self.tax,font=("times new roman",10,"bold"),width=26)
        self.entry_tax.grid(row=1,column=1)

        #Total amount
        self.lbl_total=Label(bottomframe,text="Total:",font=("times new roman",12,"bold"),bg="white",bd=4)
        self.lbl_total.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        self.entry_total=ttk.Entry(bottomframe,textvariable=self.total,font=("times new roman",10,"bold"),width=26)
        self.entry_total.grid(row=2,column=1)

#==============================================================btn frame================================================
        btnframe=Frame(bottomframe,bd=2,bg="white")
        btnframe.place(x=320,y=0)

        self.addcartbtn1=Button(btnframe,height=2,text="Add TO Cart",command=self.addcartbtn,font=("times new roman",15,"bold"),bg="orangered",fg="white",activebackground="orangered",activeforeground="white",cursor="hand2",width=15)
        self.addcartbtn1.grid(row=0,column=0,padx=3)

        self.generatebillbtn=Button(btnframe,height=2,text="Generate Bill",command=self.gen_bill,font=("times new roman",15,"bold"),bg="orangered",fg="white",activebackground="orangered",activeforeground="white",cursor="hand2",width=15)
        self.generatebillbtn.grid(row=0,column=1,padx=3)

        self.Savebillbtn=Button(btnframe,height=2,text="Save Bill",command=self.savebill,font=("times new roman",15,"bold"),bg="orangered",fg="white",activebackground="orangered",activeforeground="white",cursor="hand2",width=15)
        self.Savebillbtn.grid(row=0,column=2,padx=3)

        self.printbtn=Button(btnframe,height=2,text="Print Bill",command=self.printbtn1,font=("times new roman",15,"bold"),bg="orangered",fg="white",activebackground="orangered",activeforeground="white",cursor="hand2",width=15)
        self.printbtn.grid(row=0,column=3,padx=3)

        self.clearbtn1=Button(btnframe,height=2,text="Clear",command=self.clearbtn,font=("times new roman",15,"bold"),bg="orangered",fg="white",activebackground="orangered",activeforeground="white",cursor="hand2",width=15)
        self.clearbtn1.grid(row=0,column=4,padx=3)

        self.exitbtn=Button(btnframe,height=2,text="Exit",font=("times new roman",15,"bold"),bg="orangered",fg="white",activebackground="orangered",activeforeground="white",cursor="hand2",width=15)
        self.exitbtn.grid(row=0,column=5,padx=3)

#===================================================================receipt field============================================================================
        self.welcome()
        self.list1=[]
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t WELCOME TO SARTH TAILOR SHOP")
        self.textarea.insert(END,f"\n Bill Number:{self.billno.get()}",)
        self.textarea.insert(END,f"\n Customer Name:{self.cname.get()}")
        self.textarea.insert(END,f"\n Mobile Number:{self.cphone.get()}")
        self.textarea.insert(END,f"\n Email:{self.cemail.get()}")

        self.textarea.insert(END,"\n==================================================")
        self.textarea.insert(END,f"\n PRODUCTS\t\t\tQTY\t\t\tPRICE")
        self.textarea.insert(END,"\n==================================================\n")

    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please Add To Cart Product")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.list1))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n==================================================")
            self.textarea.insert(END,f"\n Sub Total:{self.subtotal.get()}")
            self.textarea.insert(END,f"\n Tax:{self.tax.get()}")
            self.textarea.insert(END,f"\n Total:{self.total.get()}")
            self.textarea.insert(END,"\n==================================================")

    def savebill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill")
        if op>0:
            self.billdata=self.textarea.get(1.0,END)
            f1=open("bills/"+str(self.billno.get())+".txt","w")
            f1.write(self.billdata)
            messagebox.showinfo("Saved",f"Bill No:{self.billno.get()} Saved Successfully..!")
            f1.close()
    
    def printbtn1(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp(".txt")
        open(filename,"w").write(q)
        os.startfile(filename,"print")

    def searchbill(self):
        found="no"
        for i in os.listdir("bills/"):
            if i.split(".")[0]==self.searchbill_var.get():
                f1=open(f"bills/{i}","r")
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found=="no":
            messagebox.showerror("Error","Invalid Bill No.")

    def clearbtn(self):
        self.textarea.delete(1.0,END)
        self.cname.set("")
        self.cphone.set("")
        self.billno.set(str(self.z))
        self.cemail.set("")
        self.searchbill_var.set("")
        self.product.set("")
        self.price_var.set(0)
        self.qty.set(0)
        self.list1=[0]
        self.subtotal.set("")
        self.tax.set("")
        self.total.set("")
        self.welcome()
        

#===========================================================functions============================================
    def categories(self,event=""):
        if self.combo_categoery.get()=="Clothing":
            self.combo_subcategoery.config(values=self.subcateclothing)
            self.combo_subcategoery.current(0)

        if self.combo_categoery.get()=="Lifestyle":
            self.combo_subcategoery.config(values=self.subcatelifestyle)
            self.combo_subcategoery.current(0)

        if self.combo_categoery.get()=="Mobiles":
            self.combo_subcategoery.config(values=self.subcatemobiles)
            self.combo_subcategoery.current(0)
#=====================================================product combo================================
    def productadd(self,event=""):
        #clothing
        if self.combo_subcategoery.get()=="Pant":
            self.combo_product_name.config(values=self.pant)
            self.combo_product_name.current(0)

        if self.combo_subcategoery.get()=="Shirt":
            self.combo_product_name.config(values=self.shirt)
            self.combo_product_name.current(0)

        if self.combo_subcategoery.get()=="T-Shirt":
            self.combo_product_name.config(values=self.Tshirt)
            self.combo_product_name.current(0)

        #lifestyle
        if self.combo_subcategoery.get()=="Bath Soap":
            self.combo_product_name.config(values=self.bathsoap)
            self.combo_product_name.current(0)

        if self.combo_subcategoery.get()=="Face Wash":
            self.combo_product_name.config(values=self.facewash)
            self.combo_product_name.current(0)

        if self.combo_subcategoery.get()=="Hair Oil":
            self.combo_product_name.config(values=self.Hairoil)
            self.combo_product_name.current(0)

        #mobiles
        if self.combo_subcategoery.get()=="Iphone":
            self.combo_product_name.config(values=self.iphone)
            self.combo_product_name.current(0)

        if self.combo_subcategoery.get()=="Samsang":
            self.combo_product_name.config(values=self.samsang)
            self.combo_product_name.current(0)

        if self.combo_subcategoery.get()=="OPPO":
            self.combo_product_name.config(values=self.oppo)
            self.combo_product_name.current(0)
#==========================================================price combo===================================
    def price(self,event=""):
        #clothing
        #pant
        if self.combo_product_name.get()=="Levis":
            self.combo_price.config(values=self.price_levis)
            self.combo_price.current(0)
            self.qty.set(1)
        
        if self.combo_product_name.get()=="Mufti":
            self.combo_price.config(values=self.price_mufti)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product_name.get()=="Spykar":
            self.combo_price.config(values=self.price_spykar)
            self.combo_price.current(0)
            self.qty.set(1)

        #shirty
        if self.combo_product_name.get()=="Peter England":
            self.combo_price.config(values=self.price_PeterEngland)
            self.combo_price.current(0)
            self.qty.set(1)
        
        if self.combo_product_name.get()=="Louis Phillipe":
            self.combo_price.config(values=self.price_LouisPhillipe)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product_name.get()=="Park Avenue":
            self.combo_price.config(values=self.price_parkavenue)
            self.combo_price.current(0)
            self.qty.set(1)
        
        #tshirt
        if self.combo_product_name.get()=="Polo":
            self.combo_price.config(values=self.price_polo)
            self.combo_price.current(0)
            self.qty.set(1)
        
        if self.combo_product_name.get()=="Roadster":
            self.combo_price.config(values=self.price_roadster)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product_name.get()=="Jack&Jones":
            self.combo_price.config(values=self.price_jackjones)
            self.combo_price.current(0)
            self.qty.set(1)

        #lifestyle
        #Bath Soap
        if self.combo_product_name.get()=="Santoor":
            self.combo_price.config(values=self.price_santoor)
            self.combo_price.current(0)
            self.qty.set(1)
        
        if self.combo_product_name.get()=="Lux":
            self.combo_price.config(values=self.price_lux)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product_name.get()=="Lifeboy":
            self.combo_price.config(values=self.price_lifeboy)
            self.combo_price.current(0)
            self.qty.set(1)

        #Face Wash
        if self.combo_product_name.get()=="Garnier":
            self.combo_price.config(values=self.price_garnier)
            self.combo_price.current(0)
            self.qty.set(1)
        
        if self.combo_product_name.get()=="Himalaya":
            self.combo_price.config(values=self.price_himalaya)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product_name.get()=="Mastang":
            self.combo_price.config(values=self.price_mastang)
            self.combo_price.current(0)
            self.qty.set(1)

        #Hair Oil
        if self.combo_product_name.get()=="Bajaj":
            self.combo_price.config(values=self.price_bajaj)
            self.combo_price.current(0)
            self.qty.set(1)
        
        if self.combo_product_name.get()=="Coconut":
            self.combo_price.config(values=self.price_coconut)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product_name.get()=="Jasmin":
            self.combo_price.config(values=self.price_jasmin)
            self.combo_price.current(0)
            self.qty.set(1)

        #Mobile
        #Iphone
        if self.combo_product_name.get()=="IPhone11":
            self.combo_price.config(values=self.price_i11)
            self.combo_price.current(0)
            self.qty.set(1)
        
        if self.combo_product_name.get()=="IPhone12":
            self.combo_price.config(values=self.price_i12)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product_name.get()=="IPhone14":
            self.combo_price.config(values=self.price_i14)
            self.combo_price.current(0)
            self.qty.set(1)

        #Samsang
        if self.combo_product_name.get()=="SamV12":
            self.combo_price.config(values=self.price_samv12)
            self.combo_price.current(0)
            self.qty.set(1)
        
        if self.combo_product_name.get()=="S23":
            self.combo_price.config(values=self.price_s23)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product_name.get()=="S24":
            self.combo_price.config(values=self.price_s24)
            self.combo_price.current(0)
            self.qty.set(1)

        #oppo
        if self.combo_product_name.get()=="Oppof23":
            self.combo_price.config(values=self.price_oppo23)
            self.combo_price.current(0)
            self.qty.set(1)
        
        if self.combo_product_name.get()=="Oppov21":
            self.combo_price.config(values=self.price_oppov21)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product_name.get()=="Oppo24":
            self.combo_price.config(values=self.price_oppo24)
            self.combo_price.current(0)
            self.qty.set(1)
#====================================================================add cart btn===========================================================================
        
    def addcartbtn(self):
        Tax=1
        self.n=self.price_var.get()
        self.m=self.qty.get()*self.n
        self.list1.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error","Pleaae Select the Product Name...!")
        else:
            self.textarea.insert(END,f"\n {self.product.get()}\t\t\t{self.qty.get()}\t\t\t{self.m}")
            self.subtotal.set(str("Rs.%.2f"%(sum(self.list1))))
            self.tax.set(str("Rs.%.2f"%((((sum(self.list1))-(self.price_var.get()))*Tax)/100)))
            self.total.set(str("Rs.%.2f"%(((sum(self.list1))+((((sum(self.list1))-(self.price_var.get()))*Tax)/100)))))
        
















if __name__=="__main__":
    root=Tk()
    app=bill_win(root)
    root.mainloop()