from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import ImageTk,Image
from tkcalendar import Calendar, DateEntry
from tkinter import ttk #treeview 
import traceback #les erreurs de la base de données 
import datetime 
from tkinter import filedialog

class maingui:
    def __init__(self, root):

        self.root = root
        self.root.title("Richesse")
        self.root.geometry('1200x800+200+10')
        self.root.resizable(0,0)


        self.img=ImageTk.PhotoImage(file="a2.jpg")
        self.imgICON=ImageTk.PhotoImage(file="d2.png")
        self.root.iconphoto(False,self.imgICON)
        self.bg_img=Label(self.root,image=self.img).place(x=0,y=0,relwidth=1,relheight=1)
        self.pageshow = Login_Page(self, self.root)
        self.pageshow = Login_Page(self, self.root)
    def changepage(self, page):
        self.page = page
        
        if self.page == 0:
            #del self.pageshow
            self.pageshow = Login_Page(self, self.root)

        if self.page == 1:
            #del self.pageshow
            self.pageshow = Sign_Page(self, self.root)
        if self.page == 2:
            #del self.pageshow
            self.pageshow = Home_Page(self, self.root)
        if self.page == 3:
            #del self.pageshow
            self.pageshow = Add_Page(self, self.root)
        if self.page == 4:
            #del self.pageshow
            self.pageshow = DU_Page(self, self.root)
        if self.page == 5:
            #del self.pageshow
            self.pageshow = SEARCH_Page(self, self.root)
        if self.page == 6:
            #del self.pageshow
            self.pageshow = VIEW_Page(self, self.root)
class Login_Page:
    def __init__(self, parent, window):
        
        self.parent = parent
        
        self.frame = Frame(window,width=580,height=800,bg='#EEE1C6')
        self.frame.place(x=0,y=0)
        
        self.username=Label(self.frame,text='Username',bg='#EEE1C6',fg='black',font=('Times New Roman',25))
        self.username.place(x=210,y=250)
        self.username_entry=Entry(self.frame,highlightthickness=0,relief=FLAT,bg='#EEE1C6',fg='black',font=('Times New Roman',20))
        self.username_entry.place(x=100,y=300)
        self.username_line=Canvas(self.frame,width=400,height=2.0,bg='black',highlightthickness=0)
        self.username_line.place(x=80,y=335)

        self.password=Label(self.frame,text='Password',bg='#EEE1C6',fg='black',font=('Times New Roman',25))
        self.password.place(x=210,y=375)
        self.password_entry=Entry(self.frame,highlightthickness=0,relief=FLAT,bg='#EEE1C6',fg='black',font=('Times New Roman',20))
        self.password_entry.place(x=100,y=415)
        self.password_line=Canvas(self.frame,width=400,height=2.0,bg='black',highlightthickness=0)
        self.password_line.place(x=80,y=450)

        self.loginbutton=Button(self.frame,bg="black",width=10,text='Sign in',fg="white",command=self.sign_in)
        self.loginbutton.place(x=240,y=500)
        self.signUp=Label(self.frame,text="Don't have an account :) ? ",font=('Open Sans',9,'bold'),bg='#EEE1C6',fg="black")
        self.signUp.place(x=20,y=600)
        self.signUpButton=Button(self.frame,text="Create it",font=('Open Sans',9,'bold underline'),bd=0,bg='#EEE1C6',fg='blue',cursor='hand2',activebackground='white',activeforeground='blue',command=self.clicked)
        self.signUpButton.place(x=170,y=600)
        self.jewlery=PhotoImage(file="fingerprint-scan.png")
        self.jew=Label(self.frame,image=self.jewlery,bg="#EEE1C6")
        self.jew.place(x=240,y=120)    

       
       

    def clicked(self):
        self.frame.destroy()
        self.parent.changepage(1)
    def clickedHome(self):
        self.frame.destroy()
        self.parent.changepage(2)
    def clear(self):
       self.username_entry.delete(0,END)
       self.password_entry.delete(0,END)
    def sign_in(self):
    
         if self.username_entry.get()=='' or self.password_entry.get=='':
          messagebox.showerror('error','please fill all the fields')
      
         
         else :
           if (len(self.username_entry.get())<=2 or len(self.password_entry.get())<=2):
             messagebox.showerror('error','Password or username must contain at least 3 caracters')
           else:
              try:
                   database=mysql.connector.connect(
                   host="127.0.0.1",
                   database="richessedb",
                   user="root",
                   password="3619"
                    )
                  
                   cursor=database.cursor()
                   sql_research="SELECT * from users where nomUser=%s and passUser=%s"
                   val=(self.username_entry.get(),self.password_entry.get())
                   cursor.execute(sql_research,val)
                   resultat=cursor.fetchall()
                   if(len(resultat)>0):
                       self.parent.changepage(2)
                   else:
                     
                     
                      
                       messagebox.showerror('Error', 'Account is not found')
                       self.clear()
                       
              except:
                  messagebox.showerror('error','connexion to db was not successfull')
                  traceback.print_exc()
    

class Sign_Page():
    def __init__(self, parent, window):

        self.parent = parent
        self.frame= Frame(window,width=580,height=800,bg='#EEE1C6')
        self.frame.place(x=0,y=0)
        
        self.username=Label(self.frame,text='Username',bg='#EEE1C6',fg='black',font=('Times New Roman',25))
        self.username.place(x=210,y=220)
        self.username_entry=Entry(self.frame,highlightthickness=0,relief=FLAT,bg='#EEE1C6',fg='black',font=('Times New Roman',20))
        self.username_entry.place(x=100,y=260)
        self.username_line=Canvas(self.frame,width=400,height=2.0,bg='black',highlightthickness=0)
        self.username_line.place(x=80,y=290)

        self.password=Label(self.frame,text='Password',bg='#EEE1C6',fg='black',font=('Times New Roman',25))
        self.password.place(x=210,y=320)
        self.password_entry=Entry(self.frame,highlightthickness=0,relief=FLAT,bg='#EEE1C6',fg='black',font=('Times New Roman',20))
        self.password_entry.place(x=100,y=360)
        self.password_line=Canvas(self.frame,width=400,height=2.0,bg='black',highlightthickness=0)
        self.password_line.place(x=80,y=390)

        self.passwordConfirm=Label(self.frame,text='Confirm Password',bg='#EEE1C6',fg='black',font=('Times New Roman',25))
        self.passwordConfirm.place(x=150,y=430)
        self.passwordConfirm_entry=Entry(self.frame,highlightthickness=0,relief=FLAT,bg='#EEE1C6',fg='black',font=('Times New Roman',20))
        self.passwordConfirm_entry.place(x=100,y=470)
        self.passwordConfirm_line=Canvas(self.frame,width=400,height=2.0,bg='black',highlightthickness=0)
        self.passwordConfirm_line.place(x=80,y=500)

        self.SignUPButton=Button(self.frame,bg="black",width=10,text='Sign up',fg="white",command=self.sign_up)
        self.SignUPButton.place(x=240,y=550)


        self.lock=PhotoImage(file="add-user2.png")
        self.lockpic=Label(self.frame,image=self.lock,bg="#EEE1C6")
        self.lockpic.place(x=240,y=125)

        self.signIN=Label(self.frame,text="Already have an account :) ? ",font=('Open Sans',9,'bold'),bg='#EEE1C6',fg="black")
        self.signIN.place(x=20,y=600)
        self.signINButton=Button(self.frame,text="Log in",font=('Open Sans',9,'bold underline'),bd=0,bg='#EEE1C6',fg='blue',cursor='hand2',activebackground='white',activeforeground='blue',command=self.clickedLogin)
        self.signINButton.place(x=190,y=600)
    def clickedLogin(self):
        self.frame.destroy()
        self.parent.changepage(0)
  
    def sign_up(self):   
         self.tries=0
         if(self.username_entry.get()=='' or self.password_entry.get()=='' or self.passwordConfirm_entry==''):
             messagebox.showerror('error',"Please fill up all the fields")
         else:
           self.tries+=1
         if(self.password_entry.get()!= self.passwordConfirm_entry.get()):
            messagebox.showerror('error',"Passwords doesn't match")
         else:  
             self.tries+=1
         if (len(self.username_entry.get())<=2 or len(self.password_entry.get())<=2):
           messagebox.showerror('error','Password or username must contain at least 3 caracters')
         else:
             self.tries+=1

         if(self.tries==3):
            try:
                database=mysql.connector.connect(
                host="127.0.0.1",
                database="richessedb",
                user="root",
                password="3619"
                 )
               
                cursor=database.cursor()
                sql_research="SELECT * from users where nomUser=%s and passUser=%s"
                val=(self.username_entry.get(),self.password_entry.get())
                cursor.execute(sql_research,val)
                resultat=cursor.fetchall()
                if(len(resultat)>0):
                     messagebox.showerror('Error','Account Already exists' )
                else: 
                 sql="Insert into users(nomUser,passUser) values (%s,%s)"
                 values=(self.username_entry.get(),self.password_entry.get())
                 cursor.execute(sql,values)
                 messagebox.showinfo('Success',"You are signed up , please sign in :) ")
                 database.commit()
                 database.close()
                 self.clickedLogin()

            except: 
                messagebox.showerror('error','connexion to db was not successfull')


class Home_Page():
    def __init__(self, parent,window):
        self.window=window
        self.parent = parent
        self.frame=Frame(self.window,width=1200,height=800)
        self.info_frame=Frame(self.window,width=1200,height=100,bg='#EEE1C6')
        self.info_frame.place(x=0,y=0)
        self.backg_image=ImageTk.PhotoImage(Image.open('bg2.jpg'))
      
        self.buttons_frame=Label(self.window,width=1200,height=800,image=self.backg_image)
        self.buttons_frame.place(x=0,y=100)
        self.title=Label(self.info_frame,text="Richesse's Inventory Management ",bg='#EEE1C6',fg='black',font=('Times New Roman',25))
        self.title.place(x=390,y=30)

        self.add_button=Button(self.buttons_frame,text="Add",fg='white',width=20,height=3,bg='black',command=self.clickedADD,font="Times 12 bold",borderwidth=8)
        self.add_button.place(x=370,y=90)
        self.delete_button=Button(self.buttons_frame,text="Update",fg='white',width=20,height=3,bg='black',command=self.clickedDU,font="Times 12 bold",borderwidth=8)
        self.delete_button.place(x=670,y=90)
        update_button=Button(self.buttons_frame,text="Delete",fg='white',width=20,height=3,bg='black',command=self.clickedDU,font="Times 12 bold",borderwidth=8)
        update_button.place(x=370,y=240)
        self.search_button=Button(self.buttons_frame,text="Search",fg='white',width=20,height=3,bg='black',command=self.clickedSEARCH,font="Times 12 bold",borderwidth=8)
        self.search_button.place(x=670,y=240)
        self.exit_button=Button(self.buttons_frame,text="Exit",fg='white',width=20,height=3,bg='black',command=self.exit,font="Times 12 bold",borderwidth=8)
        self.exit_button.place(x=370,y=390)
        self.view_button=Button(self.buttons_frame,text="View Products",fg='white',width=20,height=3,bg='black',command=self.clickedVIEW,font="Times 12 bold",borderwidth=8)
        self.view_button.place(x=670,y=390)
    def clickedADD(self):
        self.frame.destroy()
        self.parent.changepage(3)
    def clickedDU(self):
        self.frame.destroy()
        self.parent.changepage(4)
    def clickedSEARCH(self):
        self.frame.destroy()
        self.parent.changepage(5)
    def clickedVIEW(self):
        self.frame.destroy()
        self.parent.changepage(6)
    def exit(self):
       exit= messagebox.askyesno("Info","Are you sure you want to quit ?")
       if exit>0:
          self.parent.root.destroy()
          return
       

class Add_Page():       
 def __init__(self, parent, window):
      self.parent = parent
      self.window=window
      self.frame=Frame(self.window,width=1200,height=800)
      self.info_frame=Frame(self.window,width=1200,height=100,bg='#EEE1C6')
      self.info_frame.place(x=0,y=0)
      self.add_image=ImageTk.PhotoImage(Image.open('ADDIM.png'))
      self.im_label=Label(self.info_frame,image=self.add_image,bg='#EEE1C6')
      self.im_label.place(x=980,y=15)
      self.buttons_frame=Label(self.window,width=1200,height=800)
      self.buttons_frame.place(x=0,y=100)
      self.title=Label(self.info_frame,text="Richesse's Inventory Management ",bg='#EEE1C6',fg='black',font=('Times New Roman',25))
      self.title.place(x=390,y=30)
      self.products_frame=Frame(window,width=1200,height=800)
      self.products_frame.place(x=0,y=100)
           #products frame 
#name
      self.product_name=Label(self.products_frame,text="Name : ")
      self.product_name.place(x=10,y=40)
      self.product_name_entry=Entry(self.products_frame)
      self.product_name_entry.place(x=150,y=40)

#desc
      self.product_desc=Label(self.products_frame,text="Description : ")
      self.product_desc.place(x=10,y=80)
      self.product_desc_entry=Entry(self.products_frame)
      self.product_desc_entry.place(x=150,y=80)
#price
      self.product_price=Label(self.products_frame,text="Price : ")
      self.product_price.place(x=10,y=120)
      self.product_price_entry=Entry(self.products_frame)
      self.product_price_entry.place(x=150,y=120)
#quantity
      self.product_qty=Label(self.products_frame,text="Quantity : ")
      self.product_qty.place(x=10,y=160)
      self.product_qty_entry=Entry(self.products_frame)
      self.product_qty_entry.place(x=150,y=160)
#Seuil alerte idk
      self.product_alertThreshold=Label(self.products_frame,text="Alert Threshold : ")
      self.product_alertThreshold.place(x=10,y=200)
      self.product_alertThreshold_entry=Entry(self.products_frame)
      self.product_alertThreshold_entry.place(x=150,y=200)

#dates 

#Entree
      self.product_lastEntryDate=Label(self.products_frame,text="Date of last Entry : ")
      self.product_lastEntryDate.place(x=440,y=40)
      self.product_lastEntryDate_DP=DateEntry(self.products_frame, width= 16, background= "brown", foreground= "white",bd=2)
      self.product_lastEntryDate_DP.place(x=580,y=40)

#Sortie
      self.product_lastRemovalDate=Label(self.products_frame,text="Date of last Removal : ")
      self.product_lastRemovalDate.place(x=440,y=80)
      self.product_lastRemovalDate_DP=DateEntry(self.products_frame, width= 16, background= "brown", foreground= "white",bd=2)
      self.product_lastRemovalDate_DP.place(x=580,y=80)


#Image :) 

      self.product_image=Label(self.products_frame,text="Image :")
      self.product_image.place(x=900,y=60)
      self.prop=ImageTk.PhotoImage(Image.open('box2.png'))

      self.products_image=Frame(self.products_frame,bg="#EEE1C6",width=100,height=100,borderwidth=1, relief="solid", highlightthickness=1, highlightbackground="black")
      self.products_image.place(x=1000,y=40)
      self.products_image_DISPLAY=Label(self.products_image,image=self.prop,bg="#EEE1C6",width=75,height=75)
      self.products_image_DISPLAY.place(x=10,y=10)


#Listview 
      self.cols=('Ref','Name','Desc','Price','Quantity','Alert Threshold','Day Of Entry','Day Of Removal','Pic')
      self.listview=ttk.Treeview(self.products_frame,columns=self.cols,show='headings')


      for col in self.cols:
          self.listview.heading(col,text=col)
          self.listview.column(col,width=130,stretch=False)
          self.listview.place(x=60,y=300)
          self.listview.column("Desc",width=200)
          self.listview.column('Price',width=70)
          self.listview.column('Quantity',width=70)
          self.listview.column('Pic',width=100)
          self.listview.column('Ref',width=50)
      self.listview.bind("<ButtonRelease-1>",self.getPic)
#buttons
      self.add_button=Button(self.products_frame,text="Add",bg='white',width=12,fg='black',height=2,command=self.addData,font="Times 10 bold",borderwidth=8)
      self.add_button.place(x=150,y=610)
      self.view_button=Button(self.products_frame,text="View Products",bg='white',width=12,height=2,fg='black',command=self.displayData,font="Times 10 bold",borderwidth=8)
      self.view_button.place(x=300,y=610)
      self.reset_button=Button(self.products_frame,text="Reset",bg='white',width=12,height=2,fg='black',command=self.reset,font="Times 10 bold",borderwidth=8)
      self.reset_button.place(x=450,y=610)
      self.back_button=Button(self.products_frame,text="Back",bg='white',width=12,height=2,fg='black',command=self.clickedHOME,font="Times 10 bold",borderwidth=8)
      self.back_button.place(x=600,y=610)
      
 
 
 def clickedHOME(self):
        self.frame.destroy()
        self.parent.changepage(2)
 def addData(self):
    if self.product_name_entry.get()=="" or self.product_desc_entry.get()=="" or self.product_price_entry.get()=="" or self.product_qty_entry.get()=="" or self.product_alertThreshold_entry.get()=="" :
        messagebox.showerror("error","All fields must be entered")
    

    else :
      if(len(self.product_name_entry.get())<3 or len(self.product_desc_entry.get())<3 ):
         messagebox.showerror("error","Product Name or Desc must be at least 3 caracters long")
      else:
       if(self.product_lastEntryDate_DP.get_date()> datetime.datetime.now().date() or self.product_lastRemovalDate_DP.get_date()>= datetime.datetime.now().date()):
          messagebox.showerror("error","Date incorrect ")
       else:
        try:

         database=mysql.connector.connect(
                host="127.0.0.1",
                database="richessedb",
                user="root",
                password="3619"
                 )
               
         cursor=database.cursor()
         sql_research="SELECT * from produits where UPPER(nomProduit)=UPPER(%s)"
         val=self.product_name_entry.get()
         cursor.execute(sql_research,(val,))
         res=cursor.fetchall()
         if(len(res)>0):
            messagebox.showerror("error","Product already exists")
        
         else:
          
          file_path = filedialog.askopenfilename()
          sql="Insert into produits(nomProduit,descProduit,prixUnitaire,quantiteProduit,seuilAlerteProduit,date_entree,date_sortie,imageProduit) values (%s,%s,%s,%s,%s,%s,%s,%s)"
          values=(self.product_name_entry.get(),self.product_desc_entry.get(),self.product_price_entry.get(),self.product_qty_entry.get(),self.product_alertThreshold_entry.get(),self.product_lastEntryDate_DP.get_date(),self.product_lastRemovalDate_DP.get_date(),file_path)
          cursor.execute(sql,values)
          database.commit()
          database.close()
          messagebox.showinfo("Success","Product added successfully")
          self.listview.delete(*self.listview.get_children())
          self.displayData()
        except:
          messagebox.showerror("Error","Connection to DataBase was not successfull ")
          traceback.print_exc() 
 def reset(self):
    self.product_name_entry.delete(0,END)
    self.product_desc_entry.delete(0,END)
    self.product_price_entry.delete(0,END)
    self.product_qty_entry.delete(0,END)
    self.product_alertThreshold_entry.delete(0,END)
    self.product_lastEntryDate_DP.set_date(datetime.datetime.now().date())
    self.product_lastRemovalDate_DP.set_date(datetime.datetime.now().date())

 def displayData(self):
     try:

        database=mysql.connector.connect(
                host="127.0.0.1",
                database="richessedb",
                user="root",
                password="3619"
                 )
               
        cursor=database.cursor()
        sql="select numSerie,nomProduit,descProduit,prixUnitaire,quantiteProduit,seuilAlerteProduit,date_entree,date_sortie,imageProduit from produits"
        cursor.execute(sql)
        result=cursor.fetchall()
        #clear existing items of tree view
        for i in self.listview.get_children():
            self.listview.delete(i)
        if len(result)>0:
           for row in result:
              
              self.listview.insert('', END, values=row)
              self.listview.yview_moveto(0)
              database.commit()
        database.close()
     except:
        messagebox.showerror("Error","Connection to DataBase was not successfull ")
        traceback.print_exc() 
 def displayPhoto(self,pic):
   try:

              
       if(pic !='None' and pic is not None):
    
            img = Image.open(pic)
            img.thumbnail((self.products_image_DISPLAY.winfo_width(), self.products_image_DISPLAY.winfo_height()))
            img = ImageTk.PhotoImage(img)
            self.products_image_DISPLAY.config(image=img)
            self.products_image_DISPLAY.image = img  # to prevent garbage collection
       else:
            
            self.products_image_DISPLAY.config(image=self.prop)
              
   except:
       messagebox.showerror("Error","There was an error while displaying the picture")
       traceback.print_exc() 

 def getPic(self,event): 
    self.reset()
    item_id = self.listview.selection()[0]
    values=self.listview.item(item_id)['values']
    self.product_name_entry.insert(0,values[1])
    pic=values[8]
    self.displayPhoto(pic)

class DU_Page():
   def __init__(self, parent, window):
      self.parent = parent
      self.window=window
      self.frame=Frame(self.window,width=1200,height=800)
      self.info_frame=Frame(self.window,width=1200,height=100,bg='#EEE1C6')
      self.info_frame.place(x=0,y=0)
      self.buttons_frame=Label(self.window,width=1200,height=800)
      self.buttons_frame.place(x=0,y=100)
      self.Delete_image=ImageTk.PhotoImage(Image.open('REMIM.png'))
      self.im_label=Label(self.info_frame,image=self.Delete_image,bg='#EEE1C6')
      self.im_label.place(x=980,y=15)
      self.Update_image=ImageTk.PhotoImage(Image.open('UPDIM.png'))
      self.im_label=Label(self.info_frame,image=self.Update_image,bg='#EEE1C6')
      self.im_label.place(x=50,y=15)
      self.title=Label(self.info_frame,text="Richesse's Inventory Management ",bg='#EEE1C6',fg='black',font=('Times New Roman',25))
      self.title.place(x=390,y=30)
      self.products_frame=Frame(window,width=1200,height=800)
      self.products_frame.place(x=0,y=100)
         #name
      self.product_name=Label(self.products_frame,text="Name : ")
      self.product_name.place(x=10,y=40)
      self.product_name_entry=Entry(self.products_frame)
      self.product_name_entry.place(x=150,y=40)

#desc
      self.product_desc=Label(self.products_frame,text="Description : ")
      self.product_desc.place(x=10,y=80)
      self.product_desc_entry=Entry(self.products_frame)
      self.product_desc_entry.place(x=150,y=80)
#price
      self.product_price=Label(self.products_frame,text="Price : ")
      self.product_price.place(x=10,y=120)
      self.product_price_entry=Entry(self.products_frame)
      self.product_price_entry.place(x=150,y=120)
#quantity
      self.product_qty=Label(self.products_frame,text="Quantity : ")
      self.product_qty.place(x=10,y=160)
      self.product_qty_entry=Entry(self.products_frame)
      self.product_qty_entry.place(x=150,y=160)
#Seuil alerte idk
      self.product_alertThreshold=Label(self.products_frame,text="Alert Threshold : ")
      self.product_alertThreshold.place(x=10,y=200)
      self.product_alertThreshold_entry=Entry(self.products_frame)
      self.product_alertThreshold_entry.place(x=150,y=200)

#dates 

#Entree
      self.product_lastEntryDate=Label(self.products_frame,text="Date of last Entry : ")
      self.product_lastEntryDate.place(x=440,y=40)
      self.product_lastEntryDate_DP=DateEntry(self.products_frame, width= 16, background= "brown", foreground= "white",bd=2)
      self.product_lastEntryDate_DP.place(x=580,y=40)

#Sortie
      self.product_lastRemovalDate=Label(self.products_frame,text="Date of last Removal : ")
      self.product_lastRemovalDate.place(x=440,y=80)
      self.product_lastRemovalDate_DP=DateEntry(self.products_frame, width= 16, background= "brown", foreground= "white",bd=2)
      self.product_lastRemovalDate_DP.place(x=580,y=80)


##Image :) 

      self.product_image=Label(self.products_frame,text="Image :")
      self.product_image.place(x=900,y=60)
      self.prop=ImageTk.PhotoImage(Image.open('box2.png'))

      self.products_image=Frame(self.products_frame,bg="#EEE1C6",width=100,height=100,borderwidth=1, relief="solid", highlightthickness=1, highlightbackground="black")
      self.products_image.place(x=1000,y=40)
      self.products_image_DISPLAY=Label(self.products_image,image=self.prop,bg="#EEE1C6",width=75,height=75)
      self.products_image_DISPLAY.place(x=10,y=10)


#Listview 
      self.cols=('Ref','Name','Desc','Price','Quantity','Alert Threshold','Day Of Entry','Day Of Removal','Pic')
      self.listview=ttk.Treeview( self.products_frame,columns= self.cols,show='headings')


      for col in self.cols:
        self.listview.heading(col,text=col)
        self.listview.column(col,width=130,stretch=False)
        self.listview.place(x=60,y=300)
        self.listview.column("Desc",width=200)
        self.listview.column('Price',width=70)
        self.listview.column('Quantity',width=70)
        self.listview.column('Pic',width=100)
        self.listview.column('Ref',width=50)
        self.listview.bind("<ButtonRelease-1>",self.getInfo)
#buttons
        self.delete_button=Button(self.products_frame,text="Delete",bg='white',width=15,height=2,fg='black',command=self.deleteData,font="Times 10 bold",borderwidth=8)
        self.delete_button.place(x=30,y=600)
        self.update_button=Button(self.products_frame,text="Update",bg='white',width=15,height=2,fg='black',command=self.updateData,font="Times 10 bold",borderwidth=8)
        self.update_button.place(x=180,y=600)
        self.reset_button=Button(self.products_frame,text="Reset",bg='white',width=15,height=2,fg='black',command=self.reset,font="Times 10 bold",borderwidth=8)
        self.reset_button.place(x=330,y=600)
        self.view_button=Button(self.products_frame,text="View Products",bg='white',width=15,height=2,fg='black',command=self.displayData,font="Times 10 bold",borderwidth=8)
        self.view_button.place(x=480,y=600)
        self.back_button=Button(self.products_frame,text="Back",bg='white',width=15,height=2,fg='black',command=self.clickedHOME,font="Times 10 bold",borderwidth=8)
        self.back_button.place(x=630,y=600)
   
   def reset(self):
    self.product_name_entry.delete(0,END)
    self.product_desc_entry.delete(0,END)
    self.product_price_entry.delete(0,END)
    self.product_qty_entry.delete(0,END)
    self.product_alertThreshold_entry.delete(0,END)
    self.product_lastEntryDate_DP.set_date(datetime.datetime.now().date())
    self.product_lastRemovalDate_DP.set_date(datetime.datetime.now().date())
     

   def clickedHOME(self):
        self.frame.destroy()
        self.parent.changepage(2)
        
   

   def getInfo(self,event):
    self.reset()
    item_id=self.listview.selection()
    values=self.listview.item(item_id)['values']
    self.product_name_entry.insert(0,values[1])
    self.product_desc_entry.insert(0,values[2])
    self.product_price_entry.insert(0,values[3])
    self.product_qty_entry.insert(0,values[4])
    self.product_alertThreshold_entry.insert(0,values[5])
    self.product_lastEntryDate_DP.set_date(datetime.datetime.strptime(values[6], '%Y-%m-%d').date())
    self.product_lastRemovalDate_DP.set_date(datetime.datetime.strptime(values[7], '%Y-%m-%d').date())
    pic=values[8]
    self.displayPhoto(pic)
    
   def deleteData(self):

    try:
                database=mysql.connector.connect(
                host="127.0.0.1",
                database="richessedb",
                user="root",
                password="3619"
                 )
                
                cursor=database.cursor()
                selected = self.listview.selection()
                if not selected:
                 raise ValueError("Please select a row to delete.")
                sql="DELETE FROM produits WHERE nomProduit= %s"
                cursor.execute(sql,(self.product_name_entry.get(),))
                database.commit()
                database.close()
                messagebox.showerror("Warning","Data deleted")
                self.listview.delete(*self.listview.get_children())
                self.displayData()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to delete data: {e}")
        traceback.print_exc()
   def updateData(self):
     if self.product_name_entry.get()=="" or self.product_desc_entry.get()=="" or self.product_price_entry.get()=="" or self.product_qty_entry.get()=="" or self.product_alertThreshold_entry.get()=="" :
        messagebox.showerror("error","All fields must be entered")
    

     else :
      if(len(self.product_name_entry.get())<3 or len(self.product_desc_entry.get())<3 ):
         messagebox.showerror("error","Product Name or Desc must be at least 3 caracters long")
      else:
        if(self.product_lastEntryDate_DP.get_date()> datetime.datetime.now().date() or self.product_lastRemovalDate_DP.get_date()>= datetime.datetime.now().date()):
          messagebox.showerror("error","Date incorrect ")
        else:
         try:
             database = mysql.connector.connect(
                 host="127.0.0.1",
                 database="richessedb",
                 user="root",
                 password="3619"
             )
             cursor = database.cursor()

      
             selected = self.listview.selection()
             if not selected:
                 raise ValueError("Please select a row to update.")
             item = self.listview.item(selected)
             row_id = item['values'][0]
             pic=item['values'][8]
       
             sql = "UPDATE produits SET nomProduit=%s, descProduit=%s, prixUnitaire=%s, quantiteProduit=%s, seuilAlerteProduit=%s, date_entree=%s, date_sortie=%s,imageProduit=%s WHERE numSerie=%s"
             cursor.execute(sql, (
             self.product_name_entry.get(),
             self.product_desc_entry.get(),
             self.product_price_entry.get(),
             self.product_qty_entry.get(),
             self.product_alertThreshold_entry.get(),
             self.product_lastEntryDate_DP.get_date(),
             self.product_lastRemovalDate_DP.get_date(),
             pic,
                 row_id
             ))
             database.commit()
             database.close()
        
        
             self.listview.item(selected, values=(
                 row_id,
             self.product_name_entry.get(),
             self.product_desc_entry.get(),
             self.product_price_entry.get(),
             self.product_qty_entry.get(),
             self.product_alertThreshold_entry.get(),
             self.product_lastEntryDate_DP.get_date().strftime('%Y-%m-%d'),
             self.product_lastRemovalDate_DP.get_date().strftime('%Y-%m-%d'),
             pic
             ))
        
             messagebox.showinfo("Info", "Data Updated")
         except Exception as e:
             messagebox.showerror("Error", f"Failed to update data: {e}")
             traceback.print_exc()
 

   def displayPhoto(self,pic):
    try:

              
       if(pic !='None' and pic is not None):
    
            img = Image.open(pic)
            img.thumbnail((self.products_image_DISPLAY.winfo_width(), self.products_image_DISPLAY.winfo_height()))
            img = ImageTk.PhotoImage(img)
            self.products_image_DISPLAY.config(image=img)
            self.products_image_DISPLAY.image = img  # to prevent garbage collection
       else:
            
            self.products_image_DISPLAY.config(image=self.prop)
              
    except:
       messagebox.showerror("Error","There was an error while displaying the picture")
       traceback.print_exc() 
   def displayData(self):
     try:

        database=mysql.connector.connect(
                host="127.0.0.1",
                database="richessedb",
                user="root",
                password="3619"
                 )
               
        cursor=database.cursor()
        sql="select numSerie,nomProduit,descProduit,prixUnitaire,quantiteProduit,seuilAlerteProduit,date_entree,date_sortie,imageProduit from produits"
        cursor.execute(sql)
        result=cursor.fetchall()
        for i in self.listview.get_children():
            self.listview.delete(i)
        if len(result)>0:
           
           for row in result:
             
              self.listview.insert('',END,values=row) 
              self.listview.yview_moveto(0)
              database.commit()
        database.close()
     except:
        messagebox.showerror("Error","Connection to DataBase was not successfull ")
        traceback.print_exc() 

class SEARCH_Page():
    def __init__(self, parent, window):
      self.parent = parent
      self.window=window
      self.frame=Frame(self.window,width=1200,height=800)
      self.info_frame=Frame(self.window,width=1200,height=100,bg='#EEE1C6')
      self.info_frame.place(x=0,y=0)
      self.buttons_frame=Label(self.window,width=1200,height=800)
      self.buttons_frame.place(x=0,y=100)
      self.Search_image=ImageTk.PhotoImage(Image.open('SEARIM.png'))
      self.im_label=Label(self.info_frame,image=self.Search_image,bg='#EEE1C6')
      self.im_label.place(x=980,y=15)
      self.title=Label(self.info_frame,text="Richesse's Inventory Management ",bg='#EEE1C6',fg='black',font=('Times New Roman',25))
      self.title.place(x=390,y=30)
      
      self.products_frame=Frame(window,width=1200,height=800)
      self.products_frame.place(x=0,y=100)
      self.field_frame=Frame(self.products_frame,width= 650,height= 200,bg="#EEE1C6",borderwidth=2,relief="ridge")
      self.field_frame.place(x=10,y=10)

      self.help=Label( self.field_frame,text="Search by :",bg="#EEE1C6")
      self.help.place(x=10,y=10)
      self.orL=Label( self.field_frame,text="Or",bg="#EEE1C6")
      self.orL.place(x=250,y=70)
      self.orL2=Label( self.field_frame,text="Or",bg="#EEE1C6")
      self.orL2.place(x=250,y=150)
#name
      self.product_name=Label( self.field_frame,text="Name : ",bg="#EEE1C6")
      self.product_name.place(x=70,y=40)
      self.product_name_entry=Entry( self.field_frame)
      self.product_name_entry.place(x=50,y=70)

#price
      self.product_price=Label( self.field_frame,text="Price : ",bg="#EEE1C6")
      self.product_price.place(x=370,y=40)
      self.product_price_entry=Entry( self.field_frame)
      self.product_price_entry.place(x=350,y=70)
#quantity
      self.product_qty=Label( self.field_frame,text="Quantity : ",bg="#EEE1C6")
      self.product_qty.place(x=70,y=120)
      self.product_qty_entry=Entry( self.field_frame)
      self.product_qty_entry.place(x=50,y=150)

#Entree
      self.product_lastEntryDate=Label( self.field_frame,text="Date of last Entry : ",bg="#EEE1C6")
      self.product_lastEntryDate.place(x=370,y=120)
      self.product_lastEntryDate_DP=DateEntry( self.field_frame, width= 16, background= "brown", foreground= "white",bd=2)
      self.product_lastEntryDate_DP.place(x=350,y=150)
 
#Image :) 

      self.product_image=Label(self.products_frame,text="Image :")
      self.product_image.place(x=900,y=60)
      self.prop=ImageTk.PhotoImage(Image.open('box2.png'))

      self.products_image=Frame(self.products_frame,bg="#EEE1C6",width=100,height=100,borderwidth=1, relief="solid", highlightthickness=1, highlightbackground="black")
      self.products_image.place(x=1000,y=40)
      self.products_image_DISPLAY=Label(self.products_image,image=self.prop,width=75,height=75,bg="#EEE1C6")
      self.products_image_DISPLAY.place(x=10,y=10)

 #Listview 
      self.cols=('Ref','Name','Desc','Price','Quantity','Alert Threshold','Day Of Entry','Day Of Removal','Pic')
      self.listview=ttk.Treeview(self.products_frame,columns=self.cols,show='headings')


      for col in self.cols:
          self.listview.heading(col,text=col)
          self.listview.column(col,width=130,stretch=False)
          self.listview.place(x=60,y=300)
          self.listview.column("Desc",width=200)
          self.listview.column('Price',width=70)
          self.listview.column('Quantity',width=70)
          self.listview.column('Pic',width=100)
          self.listview.column('Ref',width=50)
      self.listview.bind("<ButtonRelease-1>",self.getPic)




#search button
      self.search_button=Button(self.products_frame,text="Search",bg='white',width=12,height=1,fg='black',command= self.searchData,font="Times 10 bold",borderwidth=8)
      self.search_button.place(x=540,y=70)
      self.reset_button=Button( self.products_frame,text="Reset",bg='white',width=12,height=1,fg='black',command= self.reset,font="Times 10 bold",borderwidth=8)
      self.reset_button.place(x=540,y=150)
      
      self.back_button=Button(self.products_frame,text="Back",bg='white',width=15,height=2,fg='black',command=self.clickedHOME,font="Times 10 bold",borderwidth=8)
      self.back_button.place(x=390,y=600)
    def reset(self):
      self.product_name_entry.delete(0,END)
      self.product_price_entry.delete(0,END)
      self.product_qty_entry.delete(0,END)
      self.product_lastEntryDate_DP.set_date(datetime.datetime.now().date())
   
    def searchData(self):
     self.listview.delete(*self.listview.get_children())
     if (self.product_name_entry.get() != "" and self.product_price_entry.get() != "" and self.product_qty_entry.get() != "" and self.product_lastEntryDate_DP.get_date()== datetime.datetime.now().date()):
        messagebox.showerror('Error', 'Please choose 1 field to search for')
     else:
         try:
            self.database = mysql.connector.connect(
                host="127.0.0.1",
                database="richessedb",
                user="root",
                password="3619"
            )

            cursor = self.database.cursor()
            if self.product_name_entry.get() != "" and self.product_price_entry.get() == "" and self.product_qty_entry.get() == "" and self.product_lastEntryDate_DP.get_date() == datetime.date.today():
                sql = "SELECT * FROM produits WHERE UPPER(nomProduit) like UPPER(%s)"
                cursor.execute(sql, (self.product_name_entry.get() + '%',))
                
            elif self.product_name_entry.get() == "" and self.product_price_entry.get() != "" and self.product_qty_entry.get() == "" and self.product_lastEntryDate_DP.get_date() == datetime.date.today():
                sql = "SELECT * FROM produits WHERE prixUnitaire=%s"
                cursor.execute(sql, (self.product_price_entry.get(),))
            elif self.product_name_entry.get() == "" and self.product_price_entry.get() == "" and self.product_qty_entry.get() != "" and self.product_lastEntryDate_DP.get_date() == datetime.date.today():
                sql = "SELECT * FROM produits WHERE quantiteProduit=%s"
                cursor.execute(sql, (self.product_qty_entry.get(),))
            elif self.product_name_entry.get() == "" and self.product_price_entry.get() == "" and self.product_qty_entry.get() == "" and self.product_lastEntryDate_DP.get_date() <= datetime.datetime.now().date():
                sql = "SELECT * FROM produits WHERE date_entree=%s"
                cursor.execute(sql, (self.product_lastEntryDate_DP.get_date(),)) 
            else:
                   messagebox.showerror('Error','Please choose only 1 field to search for ')
                   return

            rows = cursor.fetchall()
            if len(rows) > 0:
                for row in rows:
                    self.listview.insert("", END, values=row)
                self.reset()
                self.listview.yview_moveto(0)
                self.database.commit()
            
            else:
                messagebox.showerror("Error", "Product was not found")
            self.database.close()
         except :
            messagebox.showerror("Error", "Connection to DataBase was not successfull")
            traceback.print_exc()



    def getPic(self,event): 
      self.reset()
      item_id =self.listview.selection()[0]
      self.values=self.listview.item(item_id)['values']
    
      pic=self.values[8]
      self.displayPhoto(pic)
    
    def displayPhoto(self,pic):
     try:

              
       if(pic !='None' and pic is not None):
    
            img = Image.open(pic)
            img.thumbnail((self.products_image_DISPLAY.winfo_width(), self.products_image_DISPLAY.winfo_height()))
            img = ImageTk.PhotoImage(img)
            self.products_image_DISPLAY.config(image=img)
            self.products_image_DISPLAY.image = img  # to prevent garbage collection
       else:
            
            self.products_image_DISPLAY.config(image=self.prop)
              
     except:
       messagebox.showerror("Error","There was an error while displaying the picture")
       traceback.print_exc()

    def clickedHOME(self):
        self.frame.destroy()
        self.parent.changepage(2)


class VIEW_Page():
    def __init__(self, parent, window):
      self.parent = parent
      self.window=window
      self.frame=Frame(self.window,width=1200,height=800)
      self.info_frame=Frame(self.window,width=1200,height=100,bg='#EEE1C6')
      self.info_frame.place(x=0,y=0)
      self.buttons_frame=Label(self.window,width=1200,height=800)
      self.buttons_frame.place(x=0,y=100)
      self.view_image=ImageTk.PhotoImage(Image.open('VIEWIM.png'))
      self.im_label=Label(self.info_frame,image=self.view_image,bg='#EEE1C6')
      self.im_label.place(x=980,y=15)
      self.title=Label(self.info_frame,text="Richesse's Inventory Management ",bg='#EEE1C6',fg='black',font=('Times New Roman',25))
      self.title.place(x=390,y=30)
      self.products_frame=Frame(window,width=1200,height=800)
      self.products_frame.place(x=0,y=100)
      self.Help=Label(self.products_frame,text="List of inventory products  : ",font=('Times New Roman',20))
      self.Help.place(x=150,y=70)

#image
    
      self.prop=ImageTk.PhotoImage(Image.open('box2.png'))

      self.products_image=Frame(self.products_frame,bg="#EEE1C6",width=100,height=100,borderwidth=1, relief="solid", highlightthickness=1, highlightbackground="black")
      self.products_image.place(x=750,y=40)
      self.products_image_DISPLAY=Label(self.products_image,image=self.prop,width=75,height=75,bg="#EEE1C6")
      self.products_image_DISPLAY.place(x=10,y=10)


#Listview 
      self.cols=('Ref','Name','Desc','Price','Quantity','Alert Threshold','Day Of Entry','Day Of Removal','Pic')
      self.listview=ttk.Treeview( self.products_frame,columns= self.cols,show='headings')


      


      for col in self.cols:
          self.listview.heading(col,text=col)
          self.listview.column(col,width=130,stretch=False)
          self.listview.place(x=100,y=250)
      self.listview.column("Desc",width=200)
      self.listview.column('Price',width=70)
      self.listview.column('Quantity',width=70)
      self.listview.column('Pic',width=100)
      self.listview.column('Ref',width=50)
      self.listview.bind("<ButtonRelease-1>",self.getPic)
      self.displayData()
#button
      self.back_button=Button(self.products_frame,text="Back",bg='white',width=20,height=2,fg='black',command=self.clickedHOME,font="Times 10 bold",borderwidth=8)
      self.back_button.place(x=390,y=600)


    def clickedHOME(self):
        self.frame.destroy()
        self.parent.changepage(2)



    def displayData(self):
     try:

        database=mysql.connector.connect(
                host="127.0.0.1",
                database="richessedb",
                user="root",
                password="3619"
                 )
               
        cursor=database.cursor()
        sql="select numSerie,nomProduit,descProduit,prixUnitaire,quantiteProduit,seuilAlerteProduit,date_entree,date_sortie,imageProduit from produits"
        cursor.execute(sql)
        result=cursor.fetchall()
        for i in self.listview.get_children():
           self.listview.delete(i)
        if len(result)!=0:
           
           for row in result:
             
              self.listview.insert('',END,values=row) 
              self.listview.yview_moveto(0)
              database.commit()
        database.close()
     except:
        messagebox.showerror("Error","Connection to DataBase was not successfull ")
        traceback.print_exc() 


    def getPic(self,event): 
      item_id =self.listview.selection()
      self.values=self.listview.item(item_id)['values']
    
      pic=self.values[8]
      self.displayPhoto(pic)
    
    def displayPhoto(self,pic):
     try:

              
       if(pic !='None' and pic is not None):
    
            img = Image.open(pic)
            img.thumbnail((self.products_image_DISPLAY.winfo_width(), self.products_image_DISPLAY.winfo_height()))
            img = ImageTk.PhotoImage(img)
            self.products_image_DISPLAY.config(image=img)
            self.products_image_DISPLAY.image = img  # to prevent garbage collection
       else:
            
            self.products_image_DISPLAY.config(image=self.prop)
              
     except:
       messagebox.showerror("Error","There was an error while displaying the picture")
       traceback.print_exc()




    
def main():
    root = Tk()
    maingui(root)
    root.mainloop()
    
if __name__ =='__main__':
    main()