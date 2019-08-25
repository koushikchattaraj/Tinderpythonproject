import mysql.connector
from tkinter import *
from tkinter import messagebox


class tinder:
    def __init__(self):

        # connect to db
        self.conn = mysql.connector.connect(host="remotemysql.com", user="Nl1o0nLTa2", password="V1LODXB4RJ",database="Nl1o0nLTa2", )
        #self.conn = mysql.connector.connect(host="localhost", user="root", password="",database="tinder", )
        self.mycursor = self.conn.cursor()

        self.root=Tk()
        self.root.title("Tinder")
        self.root.minsize(400,350)
        self.root.maxsize(400,350)
        self.main_menu()
        self.root.mainloop()









    def main_menu(self):
        Label(text="Wellcome to Tinder",bg="Orange").grid(row=0, column=0)
        Button(text="Login", bg="Red", width=10, height=2, command=lambda: self.login_id()).grid(row=1, column=0)

        Button(text="Register", bg="Red", width=10, height=2, command=lambda: self.register_id()).grid(row=1, column=1)

    def register_id(self):

        self.destory()
        Label(text="Wellcome to Tinder",bg="Orange").grid(row=0, column=0)
        Label(text="Enter Email").grid(row=1, column=0)
        Label(text="Enter Name").grid(row=2, column=0)
        Label(text="Enter Password").grid(row=3, column=0)
        Label(text="You are").grid(row=4, column=0)
        Label(text="Your Age").grid(row=5, column=0)
        Label(text="Your City").grid(row=6, column=0)
        Label(text="Your Hobbies").grid(row=7, column=0)
        self.emailerror=Label(text="",fg="red")
        self.emailerror.grid(row=1, column=2)
        self.nameerror = Label(text="", fg="red")
        self.nameerror.grid(row=2, column=2)
        self.passworderror = Label(text="", fg="red")
        self.passworderror.grid(row=3, column=2)
        self.gendererror = Label(text="", fg="red")
        self.gendererror.grid(row=4, column=2)
        self.ageerror = Label(text="", fg="red")
        self.ageerror.grid(row=5, column=2)
        self.cityerror = Label(text="", fg="red")
        self.cityerror.grid(row=6, column=2)
        self.hobbieserror = Label(text="", fg="red")
        self.hobbieserror.grid(row=7, column=2)

        self.email=Entry()
        self.email.grid(row=1, column=1)
        self.name = Entry()
        self.name.grid(row=2, column=1)
        self.password = Entry()
        self.password.grid(row=3, column=1)
        self.gender = Entry()
        self.gender.grid(row=4, column=1)
        self.age = Entry()
        self.age.grid(row=5, column=1)
        self.city = Entry()
        self.city.grid(row=6, column=1)
        self.hobbies = Entry()
        self.hobbies.grid(row=7, column=1)
        Button(text="Register", bg="Red", width=10, height=2, command=lambda: self.register()).grid(row=8, column=0)


    def register(self):

        self.mycursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}'""".format(self.email.get()))
        checkemail = self.mycursor.fetchall()
        if self.email.get()=="":
            messagebox.showinfo("Hi "+self.name.get(),"Please Enter Email")
        elif self.name.get()=="":
            messagebox.showinfo("Hi User","Please Enter Name")
        elif self.password.get()=="":
            messagebox.showinfo("Hi "+self.name.get(),"Please Enter Password")
        elif self.gender.get()=="":
            messagebox.showinfo("Hi "+self.name.get(),"Please Enter Gender")
        elif self.age.get()=="":
            messagebox.showinfo("Hi "+self.name.get(),"Please Enter Age")
        elif self.city.get()=="":
            messagebox.showinfo("Hi "+self.name.get(),"Please Enter City")
        elif self.hobbies.get()=="":
            messagebox.showinfo("Hi "+self.name.get(),"Please Enter Hobbies")
        elif len(checkemail)>0:
            messagebox.showinfo("Hi "+self.name.get(),"Your Email Have Already Registrer")
            Button(text="Login", bg="Red", width=10, height=2, command=lambda: self.login_id()).grid(row=8, column=1)





        else:

            self.mycursor.execute(
                """INSERT INTO `users` (`user_id`, `name`, `email`, `password`, `gender`, `age`,`city`, `hobbies`) VALUES(Null,'{}','{}','{}','{}','{}','{}','{}')""".format(
                    self.name.get(), self.email.get(), self.password.get(), self.gender.get(), self.age.get(), self.city.get(), self.hobbies.get()))

            self.conn.commit()
            self.emailerror.configure(text="")
            self.destory()
            self.sucess()
    def sucess(self):
        Label(text="Wellcome to Tinder", bg="Orange").grid(row=0, column=0)
        self.sucessmessage = Label(text="", fg="green")
        self.sucessmessage.grid(row=1, column=0)
        self.sucessmessage.configure(text="You Have Sucessfully Register!!!!!")
        Label(text="Do You Want To Login Now???????", fg="green", font=(30)).grid(row=2, column=0)
        Button(text="Login", bg="Red", width=10, height=2, command=lambda: self.login_id()).grid(row=2, column=1)
















    def login_id(self):
        self.destory()
        Label(text="Wellcome to Tinder",bg="Orange").grid(row=0, column=0)
        Label(text="Email_Id").grid(row=1, column=0)
        Label(text="Password").grid(row=2, column=0)
        self.message=Label(text="", fg="red")
        self.message.grid(row=3, column=0)
        self.loginemail=Entry()
        self.loginemail.grid(row=1, column=1)
        self.loginemail.focus()
        self.loginpassword=Entry()
        self.loginpassword.grid(row=2, column=1)
        Button(text="Login", bg="Red", width=10, height=2, command=lambda: self.login()).grid(row=4, column=0)



    def login(self):









        self.mycursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(self.loginemail.get(),self.loginpassword.get()))
        user_info = self.mycursor.fetchall()


        if len(user_info)>0:
            self.message.configure(text="Wellcome User")
            self.current_user_id=user_info[0][0]
            #display next menu
            self.user_menu()


        else:

            self.message.configure(text="Wrong Email/Password")


            self.loginemail.delete(0, 'end')
            self.loginpassword.delete(0, 'end')
            self.loginemail.focus()
            Label(text="Do You Want To Register!!!!",fg="green",font=(30)).grid(row=5,column=0)
            Button(text="Register", bg="Red", width=10, height=2, command=lambda: self.register_id()).grid(row=5,column=1)


    def user_menu(self):
        self.destory()
        self.mycursor.execute("""SELECT * FROM `users` WHERE `user_id` LIKE '{}'""".format(self.current_user_id))
        self.user_name=self.mycursor.fetchall()


        for i in self.user_name:
            user_name=(i[1],)




        self.displayname="".join(user_name)




        self.msg=("Hi",self.displayname)


        Label(text="Wellcome to Tinder", bg="Orange").grid(row=0, column=0)
        Label(text=self.msg, bg="green" ,font=(40)).grid(row=1, column=0)
        #Label(text=user_name, bg="green", font=(40)).grid(row=1, column=1)
        Label(text="", font=(40)).grid(row=2, column=1)
        Button(text="Profile", bg="Red", width=10, height=2, command=lambda: self.profile_id()).grid(row=3, column=0)
        Button(text="All User", bg="Red", width=10, height=2, command=lambda: self.alluser()).grid(row=4, column=0)
        Button(text="Request", bg="Red", width=10, height=2, command=lambda: self.view_request()).grid(row=5, column=0)
        Button(text="Your Request", bg="Red", width=10, height=2, command=lambda: self.your_request()).grid(row=6, column=0)
        Button(text="Friends", bg="Red", width=10, height=2, command=lambda: self.friends()).grid(row=7, column=0)
        Button(text="Logout", bg="Red", width=10, height=2, command=lambda: self.logout()).grid(row=8, column=0)

    def profile_id(self):
        for i in self.user_name:
            self.profilename=(i[1])
            self.profilemail=(i[2])
            self.profilegender=(i[4])
            self.profileage=(i[5])
            self.profilecity=(i[6])
            self.profilehobbies=(i[7])




        self.destory()
        Label(text="Wellcome to Tinder", bg="Orange").grid(row=0, column=0)

        Label(text="Name:-",font=(40)).grid(row=1,column=0)
        Label(text="Email:-", font=(40)).grid(row=2, column=0)
        Label(text="Gender:-", font=(40)).grid(row=3, column=0)
        Label(text="Age:-", font=(40)).grid(row=4, column=0)
        Label(text="City:-", font=(40)).grid(row=5, column=0)
        Label(text="Hobbies:-", font=(40)).grid(row=6, column=0)
        Label(text=self.profilename,font=(40)).grid(row=1,column=1)
        Label(text=self.profilemail,font=(40)).grid(row=2,column=1)
        Label(text=self.profilegender, font=(40)).grid(row=3, column=1)
        Label(text=self.profileage, font=(40)).grid(row=4, column=1)
        Label(text=self.profilecity, font=(40)).grid(row=5, column=1)
        Label(text=self.profilehobbies, font=(40)).grid(row=6, column=1)
        Button(text="Edit Profile", bg="Red", width=10, height=2, command=lambda: self.edit_profile()).grid(row=8, column=0)
        Button(text="Main Menu", bg="Red", width=10, height=2, command=lambda: self.user_menu()).grid(row=8, column=1)
        Button(text="Alluser", bg="Red", width=10, height=2, command=lambda: self.alluser()).grid(row=9, column=0)
        Button(text="Logout", bg="Red", width=10, height=2, command=lambda: self.logout()).grid(row=9, column=1)


    def edit_profile(self):

        self.destory()
        Label(text="Name:-", font=(40)).grid(row=1, column=0)
        #Label(text="Email:-", font=(40)).grid(row=2, column=0)
        Label(text="Gender:-", font=(40)).grid(row=3, column=0)
        Label(text="Age:-", font=(40)).grid(row=4, column=0)
        Label(text="City:-", font=(40)).grid(row=5, column=0)
        Label(text="Hobbies:-", font=(40)).grid(row=6, column=0)

        self.editname1=Entry()
        self.editname1.grid(row=1, column=1)
        self.editname1.insert(0,str(self.profilename))



        self.editgender = Entry()
        self.editgender.grid(row=3, column=1)
        self.editgender.insert(0,self.profilegender)



        self.editcity = Entry()
        self.editcity.grid(row=5, column=1)
        self.editcity.insert(0,self.profilecity)

        self.edithobbies = Entry()
        self.edithobbies.grid(row=6, column=1)
        self.edithobbies.insert(0,self.profilehobbies)

        self.editage = Entry()
        self.editage.grid(row=4, column=1)
        self.editage.insert(0, int(self.profileage))






        Button(text="Update", bg="Red", width=10, height=2, command=lambda: self.update()).grid(row=8, column=0)
        Button(text="Main Menu", bg="Red", width=10, height=2, command=lambda: self.user_menu()).grid(row=8, column=1)
        Button(text="Alluser", bg="Red", width=10, height=2, command=lambda: self.alluser()).grid(row=9, column=0)
        Button(text="Logout", bg="Red", width=10, height=2, command=lambda: self.logout()).grid(row=9, column=1)

    def update(self):

        self.editname = "".join(self.editname1.get())



        Button(text="View Profile", bg="Red", width=10, height=2, command=lambda: self.profile_id()).grid(row=8,column=0)
        Button(text="Main Menu", bg="Red", width=10, height=2, command=lambda: self.user_menu()).grid(row=8, column=1)
        Button(text="Alluser", bg="Red", width=10, height=2, command=lambda: self.alluser()).grid(row=9, column=0)
        Button(text="Logout", bg="Red", width=10, height=2, command=lambda: self.logout()).grid(row=9, column=1)
        self.updatemsg = Label(text="", font=(30), fg="white", bg="red")
        self.updatemsg.grid(row=7, column=0)
        self.updatemsg.configure(text="Your Profile Sucessfully Updated!!!!")






        self.mycursor.execute("""UPDATE `users` SET `name` = '{}' WHERE `users`.`user_id` = '{}';""".format(self.editname, self.current_user_id))

        self.mycursor.execute("""UPDATE `users` SET `gender` = '{}' WHERE `users`.`user_id` = '{}';""".format(self.editgender.get(),self.current_user_id))

        self.mycursor.execute("""UPDATE `users` SET `age` = '{}' WHERE `users`.`user_id` = '{}';""".format(self.editage.get(),self.current_user_id))

        self.mycursor.execute("""UPDATE `users` SET `city` = '{}' WHERE `users`.`user_id` = '{}';""".format(self.editcity.get(),self.current_user_id))

        self.mycursor.execute("""UPDATE `users` SET `hobbies` = '{}' WHERE `users`.`user_id` = '{}';""".format(self.edithobbies.get(),self.current_user_id))

        self.conn.commit()
        self.updatemsg.focus()

    def alluser(self):

        self.destory()

        self.mycursor.execute("""SELECT * FROM `users` WHERE `user_id` NOT LIKE '{}'""".format(self.current_user_id))
        self.all_user = self.mycursor.fetchall()
        self.alluserlist=Listbox(self.root,borderwidth=10,height=10,font=("Algerian",10))
        self.alluserlist.grid(row=1,column=0)

        for i in self.all_user:
            self.alluserlist.insert(END, i[0:2])

        self.showprofilebtn = Button(text="Show Profile", bg="Red", width=10, height=2, command=lambda: self.datafetch())
        self.showprofilebtn.grid(row=2, column=0)
        Button(text="Send Request", bg="Red", width=10, height=2, command=lambda: self.send_request()).grid(row=2, column=1)

        Button(text="Main Menu", bg="Red", width=10, height=2, command=lambda: self.user_menu()).grid(row=3, column=0)

        Button(text="Logout", bg="Red", width=10, height=2, command=lambda: self.logout()).grid(row=3, column=1)



    def datafetch(self):
        self.destroybtn()
        self.showprofilebtn = Button(text="Show Profile", bg="Red", width=10, height=2, command=lambda: self.datafetch1())
        self.showprofilebtn.grid(row=2, column=0)

        Button(text="Send Request", bg="Red", width=10, height=2, command=lambda: self.send_request()).grid(row=2, column=1)

        Button(text="Main Menu", bg="Red", width=10, height=2, command=lambda: self.user_menu()).grid(row=3, column=0)

        Button(text="Logout", bg="Red", width=10, height=2, command=lambda: self.logout()).grid(row=3, column=1)

        self.datastore = self.alluserlist.get(ACTIVE)
        self.data=self.datastore[0]

        self.mycursor.execute("""SELECT * FROM `users` WHERE `user_id` LIKE '{}'""".format(self.data))
        data = self.mycursor.fetchall()

        #print(data)
        self.id=data[0][0]
        #self.id1=data[1]

        self.xname=data[0][1]
        self.xgender=data[0][4]
        self.xage=data[0][5]
        self.xcity=data[0][6]
        self.xhobbies=data[0][7]
        self.x()





    def x(self):

        self.frame=Frame(self.root)
        self.frame.grid(row=1,column=1)
        frame=self.frame

        Label(frame,text="Name:-", font=(40)).grid(row=2, column=0)
        #Label(text="Email:-", font=(40)).grid(row=3, column=0)
        Label(frame,text="Gender:-", font=(40)).grid(row=4, column=0)
        Label(frame,text="Age:-", font=(40)).grid(row=5, column=0)
        Label(frame,text="City:-", font=(40)).grid(row=6, column=0)
        Label(frame,text="Hobbies:-", font=(40)).grid(row=7, column=0)

        Label(frame,text=self.xname, font=(40)).grid(row=2, column=1)
        #Label(text="", font=(40)).grid(row=3, column=1)
        Label(frame,text=self.xgender, font=(40)).grid(row=4, column=1)
        Label(frame,text=self.xage, font=(40)).grid(row=5, column=1)
        Label(frame,text=self.xcity, font=(40)).grid(row=6, column=1)
        Label(frame,text=self.xhobbies, font=(40)).grid(row=7, column=1)






    def datafetch1(self):

        showprofilebtn = Button(text="Show Profile", bg="Red", width=10, height=2, command=lambda: self.datafetch())
        showprofilebtn.grid(row=2, column=0)
        Button(text="Send Request", bg="Red", width=10, height=2, command=lambda: self.send_request()).grid(row=2, column=1)

        Button(text="Main Menu", bg="Red", width=10, height=2, command=lambda: self.user_menu()).grid(row=3, column=0)

        Button(text="Logout", bg="Red", width=10, height=2, command=lambda: self.logout()).grid(row=3, column=1)
        #self.frame.destroy()


    def send_request(self):
        self.mycursor.execute(
            """INSERT INTO `proposals` (`proposal_id`,`romeo_id`,`juliet_id`) VALUES (NULL, '{}', '{}')""".format(
                self.current_user_id, self.id))
        self.conn.commit()
        messagebox.showinfo(self.msg, "Proposal Sucessfully to " + self.xname)



    def view_request(self):


        self.mycursor.execute(
            """SELECT * FROM `proposals` p JOIN `users` u ON u.`user_id`=p. `juliet_id` WHERE p. `romeo_id`='{}'""".format(
                self.current_user_id))

        proposal_for_you = self.mycursor.fetchall()

        if len(proposal_for_you) <= 0:
            messagebox.showinfo("Hi "+self.displayname,"You Dont Have Any Proposal")
            #self.view_user()

        else:
            self.destory()
            self.request=Listbox(self.root,borderwidth=10,height=10,font=("Algerian",10))
            self.request.grid(row=1,column=0)
            #self.frame.grid(row=1, column=1)






            Button(text="Show Profile", bg="Red", width=10, height=2, command=lambda: self.showreq()).grid(row=2,column=0)
            Button(text="Your Request", bg="Red", width=10, height=2, command=lambda: self.your_request()).grid(row=2,column=1)
            Button(text="Main Menu", bg="Red", width=10, height=2, command=lambda: self.user_menu()).grid(row=3,column=0)
            Button(text="Logout", bg="Red", width=10, height=2, command=lambda: self.logout()).grid(row=3, column=1)

            for i in proposal_for_you:
                self.request.insert(0,i[3:5])


    def showreq(self):

        self.reqdata = self.request.get(ACTIVE)
        self.reqdata = self.reqdata[0]

        self.mycursor.execute("""SELECT * FROM `users` WHERE `user_id` LIKE '{}'""".format(self.reqdata))
        data = self.mycursor.fetchall()
        #print(self.reqdata)
        for i in data:
            name = i[1]
            gender = i[4]
            age = i[5]
            city = i[6]
            hobbies = i[7]

        self.reqframe = Frame(self.root)
        self.reqframe.grid(row=1, column=1)
        frame = self.reqframe

        Label(frame, text="Name:-", font=(40)).grid(row=2, column=0)
        # Label(text="Email:-", font=(40)).grid(row=3, column=0)
        Label(frame, text="Gender:-", font=(40)).grid(row=4, column=0)
        Label(frame, text="Age:-", font=(40)).grid(row=5, column=0)
        Label(frame, text="City:-", font=(40)).grid(row=6, column=0)
        Label(frame, text="Hobbies:-", font=(40)).grid(row=7, column=0)

        Label(frame, text=name, font=(40)).grid(row=2, column=1)
        # Label(text="", font=(40)).grid(row=3, column=1)
        Label(frame, text=gender, font=(40)).grid(row=4, column=1)
        Label(frame, text=age, font=(40)).grid(row=5, column=1)
        Label(frame, text=city, font=(40)).grid(row=6, column=1)
        Label(frame, text=hobbies, font=(40)).grid(row=7, column=1)









    def your_request(self):

        self.mycursor.execute(
            """SELECT * FROM `proposals` p JOIN `users` u ON u.`user_id`=p. `romeo_id` WHERE p. `juliet_id`='{}'""".format(
                self.current_user_id))


        proposal_for_you = self.mycursor.fetchall()

        if len(proposal_for_you) <= 0:
            messagebox.showinfo("Hi "+self.displayname,"You Dont Have Any Proposed")
            #(text="You Dont Have Any Proposed",font=(30)).grid(row=1,column=0)

        else:
            self.destory()
            for i in proposal_for_you:
                req=Listbox(self.root,borderwidth=10,height=10,font=("Algerian",10))
                req.grid(row=1,column=0)
                req.insert(0,i[3:5])

                self.namebtn=Button(text="Show Profile",font=(30),command=lambda: self.viewpropose())
                self.namebtn.grid(row=2,column=0)




    def viewpropose(self):
        self.mycursor.execute(
            """SELECT * FROM `proposals` p JOIN `users` u ON u.`user_id`=p. `romeo_id` WHERE p. `juliet_id`='{}'""".format(
                self.current_user_id))
        proposal_for_you = self.mycursor.fetchall()
        for i in proposal_for_you:
            frame=Frame()
            frame.grid(row=1,column=1)
            Label(frame,text="Name",font=(40)).grid(row=1,column=1)
            Label(frame,text="Gender", font=(40)).grid(row=2, column=1)
            Label(frame,text="Age", font=(40)).grid(row=3, column=1)
            Label(frame,text="City", font=(40)).grid(row=4, column=1)
            Label(frame,text="Hobbies", font=(40)).grid(row=5, column=1)

            Label(frame,text=i[4], font=(40)).grid(row=1, column=2)
            Label(frame,text=i[7], font=(40)).grid(row=2, column=2)
            Label(frame,text=i[8], font=(40)).grid(row=3, column=2)
            Label(frame,text=i[9], font=(40)).grid(row=4, column=2)
            Label(frame,text=i[10], font=(40)).grid(row=5, column=2)










    def destory(self):
        for i in self.root.grid_slaves():
            i.destroy()

        Label(text="Wellcome to Tinder", bg="Orange").grid(row=0, column=0)

    def destroybtn(self):
        for i in self.showprofilebtn.grid_slaves():
            i.destroy()



    def logout(self):
        self.current_user_id = 0
        self.destory()
        Label(text="Wellcome to Tinder", bg="Orange").grid(row=0, column=0)
        Label(text="You Are Logged out", bg="Orange").grid(row=4, column=0)

        self.main_menu()













obj=tinder()