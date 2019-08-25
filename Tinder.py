#Main Programe
import mysql.connector


class Tinder:

    def __init__(self):
        

        #connect to db
        self.conn=mysql.connector.connect(host="remotemysql.com",user="Nl1o0nLTa2", password="V1LODXB4RJ", database="Nl1o0nLTa2",)
        #self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="tinder", )
        self.mycursor=self.conn.cursor()


        self.program_menu()

    def program_menu(self):

        program_input=input ("""Hi! How may i help you?
        1. Enter 1 to register
        2. Enter 2 to login
        3. Exit to anything key:-  """)

        if program_input=="1":
            #print("reg")
            self.register()

        elif program_input=="2":
            #print("login")
            self.login()
        else:
            print("Bye")

    def register(self):
        self.email=enteremail=input("Enter Your Email:- ")
        self.mycursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}'""".format(enteremail))
        enteremail=self.mycursor.fetchall()
        self.number=list(range(200+1))
        self.number=list(map(str,self.number))


        if len(enteremail)>0:
            print("This Email Already Registerd!!!!!! Try Another Email")
            self.program_menu()
        elif len(enteremail)<=0:
            self.name = input("Enter Your Name:- ")
            #email =input("Enter Your Email:- ")
            self.password = input("Enter Your Password:- ")
            self.gender = input("Your Gender:- ")
            self.intage()

    def intage(self):
        self.age = input("Your Age:- ")
        if self.age not in self.number:
            print("Please Enter Your Age")
            self.intage()
        elif self.age in self.number:
            self.city = input("Your city:- ")
            self.hobbies = input("What's Your pass time:- ")
            self.mycursor.execute(
                """INSERT INTO `users` (`user_id`, `name`, `email`, `password`, `gender`, `age`,`city`, `hobbies`) VALUES(Null,'{}','{}','{}','{}','{}','{}','{}')""".format(
                    self.name, self.email, self.password, self.gender, self.age, self.city, self.hobbies))
            self.conn.commit()
            print("You Have Register Sucessfully")
            self.program_menu()

    def login(self):
        emaillogin=input("Enter Email For Login:- ")
        passwordlogin=input("Enter Password:- ")

        self.mycursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(emaillogin,passwordlogin))

        user_info=self.mycursor.fetchall()

        #print(user_info)

        if len(user_info)>0:
            print("Wellcome User")
            self.current_user_id=user_info[0][0]
            #display next menu
            self.user_menu()


        else:
            print("Wrong Email/Password")
            self.program_menu()

    def user_menu(self):

        user_input = input("""Hi! how you like to process
        1.view all user
        2.view who proposed you
        3.view your proposal
        4.view all matches
        5.Update Profile
        6.Logout:- """)

        if user_input == "1":
            self.view_user()
        elif user_input == "2":
            self.view_proposed()
        elif user_input == "3":
            self.view_proposal()
        elif user_input == "4":
            self.view_matches()
        elif user_input == "5":
            self.update_profile()
        elif user_input == "6":
            self.logout()

        else:
            print("You Have Entered Wrong Key")
            self.user_menu()

    def view_user(self):
        self.mycursor.execute("""SELECT * FROM `users` WHERE `user_id` NOT LIKE '{}'""".format(self.current_user_id))
        all_user=self.mycursor.fetchall()


        for i in all_user:
            print(i[0], "|", i[1], "|" , i[4], "|", i[5], "|", i[6], "|", i[7], "|")
            print("----------------------------------------------------------------")




        juliet_id=input("Enter the user id of user whom you to proposed? if Not Enter 0 :- ")
        if juliet_id == "0":
            self.user_menu()
        else:
            self.propose(self.current_user_id, juliet_id)



    def propose(self, romeo_id, juliet_id):

        self.mycursor.execute("""INSERT INTO `proposals` (`proposal_id`,`romeo_id`,`juliet_id`) VALUES (NULL, '{}', '{}')""".format(romeo_id,juliet_id))
        self.conn.commit()

        print("Proposal Sucessfully. Fingers crossed!")

        self.user_menu()

    def view_proposed(self):
        self.mycursor.execute("""SELECT * FROM `proposals` p JOIN `users` u ON u.`user_id`=p. `romeo_id` WHERE p. `juliet_id`='{}'""".format(self.current_user_id))

        proposal_for_you=self.mycursor.fetchall()

        if len(proposal_for_you) <= 0:
            print("You Dont Have Any Proposed")
            self.view_user()

        else:
            for i in proposal_for_you:
                print(i[4], "|", i[7], "|", i[8], "|", i[9], "|", i[10])
                print("---------------------------------------")

            self.user_menu()

    def view_proposal(self):
        self.mycursor.execute("""SELECT * FROM `proposals` p JOIN `users` u ON u.`user_id`=p. `juliet_id` WHERE p. `romeo_id`='{}'""".format(self.current_user_id))

        proposal_for_you = self.mycursor.fetchall()

        if len(proposal_for_you)<=0:
            print("You Dont Have Any Proposal")
            self.view_user()

        else:
            for i in proposal_for_you:
                print(i[4], "|", i[7], "|", i[8], "|", i[9], "|", i[10])
                print("---------------------------------------")

            self.user_menu()



    def view_matches(self):
        self.mycursor.execute("""SELECT * FROM `proposals` p JOIN `users` u ON u.`user_id`=p.`romeo_id` WHERE p.`romeo_id`
        IN (SELECT `juliet_id` FROM `proposals` WHERE `romeo_id` LIKE '{}') AND p.`juliet_id` LIKE '{}'""".format(self.current_user_id,self.current_user_id))

        matches = self.mycursor.fetchall()

        if len(matches)<=0:
            print("You Dont Have Any Matched")
            self.view_user()
        else:
            for i in matches:
                print(i[4], "|", i[7], "|", i[8], "|", i[9], "|")
                print("---------------------------------------")

            self.user_menu()


    def update_profile(self):

        self.mycursor.execute("""SELECT * FROM `users` WHERE `user_id` LIKE '{}'""".format(self.current_user_id))
        user = self.mycursor.fetchall()

        for i in user:

            print("User ID - ", i[0], "|", "Name - ", i[1], "|", "Email - ", i[2], "|", "Password - ", i[3], "|", "Gender - ", i[4], "|", "Age - ", i[5], "|", "City - ", i[6], "|", "Hobbies - ", i[7], "|")
            print("----------------------------------------------------------------")
            update=input("""What Do You Want To Change
            1.Name
            2.Email
            3.Password
            4.Gender
            5.Age
            6.City
            7.Hobbies
            For Main Menu Enter any key""")

        if update =="1":
            name1=input("Enter Your Name")
            self.mycursor.execute("""UPDATE `users` SET `name` = '{}' WHERE `users`.`user_id` = '{}';""".format(name1, self.current_user_id))
            self.conn.commit()
            print("Profile Update")
            self.update_profile()
        elif update =="2":
            email1= input("Enter Your Email:- ")
            self.mycursor.execute("""UPDATE `users` SET `email` = '{}' WHERE `users`.`user_id` = '{}';""".format(email1,self.current_user_id))
            self.conn.commit()
            print("Profile Update")
            self.update_profile()
        elif update == "3":
            password1 = input("Enter Your Password:- ")
            self.mycursor.execute("""UPDATE `users` SET `password` = '{}' WHERE `users`.`user_id` = '{}';""".format(password1,self.current_user_id))
            self.conn.commit()
            print("Profile Update")
            self.program_menu()
        elif update == "4":
            gender1 = input("Your Gender:- ")
            self.mycursor.execute("""UPDATE `users` SET `gender` = '{}' WHERE `users`.`user_id` = '{}';""".format(gender1,self.current_user_id))
            self.conn.commit()
            print("Profile Update")
            self.update_profile()
        elif update == "5":
            age1 = input("Your Age:- ")
            self.mycursor.execute("""UPDATE `users` SET `age` = '{}' WHERE `users`.`user_id` = '{}';""".format(age1,self.current_user_id))
            self.conn.commit()
            print("Profile Update")
            self.update_profile()
        elif update == "6":
            city = input("Your city:- ")
            self.mycursor.execute("""UPDATE `users` SET `city` = '{}' WHERE `users`.`user_id` = '{}';""".format(city1,self.current_user_id))
            self.conn.commit()
            print("Profile Update")
            self.update_profile()
        elif update == "7":
            hobbies1 = input("What's Your pass time:- ")
            self.mycursor.execute("""UPDATE `users` SET `hobbies` = '{}' WHERE `users`.`user_id` = '{}';""".format(hobbies1,self.current_user_id))
            self.conn.commit()
            print("Profile Update")
            self.update_profile()
        else:
            self.user_menu()











        self.user_menu()






    def logout(self):
        self.current_user_id=0
        print("You Are Logged out")
        self.program_menu()



obj=Tinder()
