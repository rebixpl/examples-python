import turtle

qazi_turtle = turtle.Turtle()

#you can DEFNE FUNCTION this way
# Square
def square():
    qazi_turtle.forward(100)
    qazi_turtle.right(90)
    qazi_turtle.forward(100)
    qazi_turtle.right(90)
    qazi_turtle.forward(100)
    qazi_turtle.right(90)
    qazi_turtle.forward(100)

square()
qazi_turtle.forward(200)
square()
qazi_turtle.forward(200)
square()
qazi_turtle.forward(200)
square()
qazi_turtle.forward(200)



#FUNCTION WITH ARGUMENT
def my_function(inputVorname, inputSurname):
    print("Your name's " + inputVorname + " " + inputSurname)

my_function("Chris", "Gulas")



#KEYWORD ARGUMENTS IN FUNCTION
def my_kids_kappa(child3, child2, child1):
    print("The youngest child is " + child3)

my_kids_kappa(child1="Emil", child2="Tobias", child3="Adolf") # It prints: The youngest child is Adolf



#DEFAULT PARAMETER VALUE IN FUNCTION
def my_country(country = "Poland"):
    print("I am from " + country)

my_country("Afganistan")
my_country()



#prvevent window from closing
PAUSE = input()
