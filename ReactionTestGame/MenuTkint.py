# Import tkinter library  
from tkinter import *  
from tkinter import messagebox
import os
import tkinter  
import sys
import pygame
import random as r
from pygame.event import Event 

#game start
pygame.init()  #initialise

size = width, height = 800, 400
black = 0, 0, 0

screen = pygame.display.set_mode(size)   #screen parameters
pygame.display.set_caption('Game')
clock = pygame.time.Clock()



class Target:
    def __init__(self, position):

        self.x, self.y = position   #creates x and y values from position argument


        self.font = pygame.font.SysFont("Arial", 30)   #defines the font of the text
        self.text = self.font.render("    ", 1, pygame.Color("White")) #creates the text 

        self.size = self.text.get_size()     #defines size of the target  
        self.surface = pygame.Surface(self.size)     #creates a surface for the target
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1]) 
        #creates a rectangle that is the same size as the target

        self.surface.fill("red")     #sets the colour of the target

        self.score = 0   
        self.startTime = 0
        self.totalReactTime = 0
        self.totalClicks = 0

    def show(self):
        screen.blit(self.surface, (self.x, self.y))
 
    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.totalClicks += 1
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
              

                    #increasing the score each time a target is hit
                    self.score += 1
                    print(self.score)

                    #record time between user hitting the targets
                    self.totalReactTime +=  pygame.time.get_ticks() - self.startTime


                    #create new position
                    self.x ,self.y = (r.randint(0, 400), r.randint(0,300))
                    self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

                    #changes screen 
                    screen.fill(black)
                    self.show()


                        
                   

target1 = Target((r.randint(0, 760), r.randint(0,350)))




def Menu():  
    global loggedIn
    loggedIn = False
    # Create an instance of tkinter window  
    global win  
    win = Tk()  
    win.geometry("700x450")   
    win.title("Menu")  

    #designing the form
    MenuLbl = Label (win, text = "Menu", font = "Verdana 15 bold").pack(pady= 15)  
    Play_btn = Button(win, text="Play", command = Game).pack(pady=10)  
    Login_btn = Button(win, text="Login", command=login).pack(pady=10)  
    Register_btn = Button(win, text="Register", command=register).pack(pady=10)  
    Results_btn = Button(win, text="Show previous results", command=showResults).pack(pady=10)
    Instructions_btn = Button(win, text = "How to play", command = instructions).pack()


    win.mainloop()  

  

def instructions():
    win = Tk()  
    win.geometry("600x200")   
    win.title("Instructions")      
    Label (win, text = "Instructions", font = "Verdana 15 bold").pack(pady= 15) 
    Label (win, text = "click the squares as quickly as you can, the game starts once you click the first square!").pack()

  

def register():   
    global register_win  #making the window global so other functions can use it 
    register_win = Toplevel(win)   
    register_win.title("Create Account")   
    register_win.geometry("300x250")  
  

    global username   
    global password   
    global username_entry   
    global password_entry  

    username = StringVar()   
    password = StringVar()   

    username_lable = Label(register_win, text="Username").pack()    
    username_entry = Entry(register_win, textvariable=username).pack()    
    password_lable = Label(register_win, text="Password").pack()   
    password_entry = Entry(register_win, textvariable=password, show='*').pack()   
    Button(register_win, text="Register", command = registerAcc).pack()   


def registerAcc():   

    #import the information from the textboxes 
    usernameInfo = username.get()   
    passwordInfo = password.get()  

    file = open(usernameInfo, "w")    #makes a new file with the text from the username textbox 
    file.write(usernameInfo + "\n")  #writes the username to the file 
    file.write(passwordInfo)    #writes the password to the file 
    file.close()    

    Label(register_win, text="Account created", fg="green").pack()  #shows when account is made successfully 


def login():  
    #Creating window 
    global login_win  
    login_win = Toplevel(win)  
    login_win.title("Login")  
    login_win.geometry("300x250")  

  

    #Making attributes global  
    global username 
    global password 
    global username_login_entry 
    global password_login_entry  

    #Username label and textbox 
    Label(login_win, text="Enter Login details").pack()    
    Label(login_win, text="Username").pack()  
    username = StringVar()  
    username_login_entry = Entry(login_win, textvariable=username).pack() 

  

    #Password label and textbox 

    Label(login_win, text="Password").pack()  

    password = StringVar()  

    password_login_entry = Entry(login_win, textvariable=password, show= '*').pack() 

   

    #Login button 

    Button(login_win, text="Login", width=10, height=1, command = verifyLogin).pack()  

  

   

  

def verifyLogin():  

    #import user input from text boxes 

    user = username.get()  

    userPassword = password.get()  

    global currentUser #create a global variable to store the currentUser
    currentUser = ""
  

    list_of_files = os.listdir() #gets a list of all the files in the project folder 
  
    #Searching for the user's file in the directory 

    if user in list_of_files:     

        currentFile = open(user, "r")  
        verify = currentFile.read().splitlines()  

#searching for the password in the file it 

        if userPassword in verify:  
            currentUser = user
            global loggedIn
            loggedIn = True
            login_sucess()  




        else:  

            wrongPassword()  

  

    else:  
        userNotFound()  

  

   

  

  

   

  

def login_sucess():  
    global login_success_screen  
    login_success_screen = Toplevel(login_win)  
    login_success_screen.title("Success")  
    login_success_screen.geometry("150x100")  

    loggedIn = True

    Label(login_success_screen, text="Login Success").pack() 
    Button(login_success_screen, text="OK", command=login_sucess).pack()  


# Designing popup for login invalid password  

def wrongPassword():  

    global password_not_recog_screen  
    password_not_recog_screen = Toplevel(login_win)  
    password_not_recog_screen.title("Success")  
    password_not_recog_screen.geometry("150x100")  

    Label(password_not_recog_screen, text="Invalid Password ").pack()  

  

    #Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()  

  

   

  

# Designing popup for user not found  

  

   

  

def userNotFound():  

    global user_not_found_screen  
    user_not_found_screen = Toplevel(login_win)  
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")  

    Label(user_not_found_screen, text="User Not Found").pack()  

  

    #Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()  

  
def showResults():
    try:
        file = open(currentUser,'r')  #opens file
        #cycle to the right line
        file.readline()
        file.readline()

        #set variables for reaction time and accuracy
        react = file.readline()
        coordination = file.readline()

        file.close()


        #create window
        resultsScreen = Toplevel(win)  
        resultsScreen.title("Results")  
        resultsScreen.geometry("400x550") 

        Label(resultsScreen, text="Your highest reaction time is " + react).pack(pady = 10)
        Label(resultsScreen, text="Your best accuracy is " + coordination).pack(pady = 10)  
        
    except :

        messagebox.showinfo("Error", "You need to login before you can view results")
         
def GameOverScreen():

        EndResultsScreen = Toplevel(win)  
        EndResultsScreen.title("Results")  
        EndResultsScreen.geometry("450x300")

        Label(EndResultsScreen, text="Your reaction time that game was " + str(AvgReactTime)).pack(pady=10)
        Label(EndResultsScreen, text="Your accuracy that game was " + str(accuracy)).pack(pady=10)
    


def Game():
    run = True
    gameLength = 0
    Clicked = 0 
    timeSet = False

    screen.fill(black)
    target1.show()

    gameLength = int(input("How long should the game be (seconds)"))
    while run == True:
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if target1.rect.collidepoint(x, y):
                        Clicked = 1

            if Clicked == 1 & timeSet == False:
                target1.startTime = pygame.time.get_ticks()
                timeSet = True
            


            target1.click(event)
            pygame.display.update()
            clock.tick(60)
            pygame.display.flip()
            try:
                if pygame.time.get_ticks() - target1.startTime  > gameLength * 1000: #stop after time check
                    run = False        
                    pygame.quit()
                    recordReactTime(gameLength, target1.score)
                    recordAccuracy(target1.score, target1.totalClicks)
                    GameOverScreen()
            except:
                pass
        
def recordReactTime(totalTime, score): 
    print(loggedIn)
    global AvgReactTime
    AvgReactTime = totalTime / score  #finds average for reaction time 

    if loggedIn == True:

        resultsScreen = Toplevel(win)  
        resultsScreen.title("Results")  
        resultsScreen.geometry("150x100") 

        file = open(currentUser,'r') 
        file.readline()
        file.readline()

        #set variables for reaction time and accuracy
        react = file.readline()
        print(react)

        if AvgReactTime > int(react):
            file = open(currentUser,'a+')
            file.write('\n' + str(AvgReactTime))
            file.close()   


def recordAccuracy(score, clicks):


    global accuracy
    accuracy = score / clicks #creates accuracy rating  
    accuracy = accuracy * 100  #gives accuracy as a percentage  

    if loggedIn == True:

        resultsScreen = Toplevel(win)  
        resultsScreen.title("Results")  
        resultsScreen.geometry("150x100") 

        file = open(currentUser,'r') 
        file.readline()
        file.readline()

        #set variables for reaction time and accuracy
        file.readline()
        coordination = file.readline()
        
        if accuracy > int(coordination):
            file = open(currentUser,'a+')
            file.write('\n' + str(accuracy))
            file.close()   
   

  

Menu() 