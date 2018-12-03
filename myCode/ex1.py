'''print ("Hello World!")

print ("Hello Again")
print("I coude have code like this")

print("I will now count my chickens:")
print("Hens",25+30/6)
print("Roosters",100-25*3%4)
print("Now I will count the eggs:")
print(3+2+1-5+4%2-1/4+6)
print("Is it true that 3+2<5-7?")
print(3+2<5-7)
print("What is 3+2?",3+2)
print("What is 5-7?",5-7)
print("oh,that's why it's False.")

print("How about some more.")
print("Is it greater?",5>=-2)
print("Is it less or equal?",5<=-2)

cars=100
space_in_a_car=4
drivers=30
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_a_car
average_passengers_per_car=passengers/cars_driven

print("There are",cars,"cars available.")
print("There are only",drivers,"drivers available")
print("There will be ",cars_not_driven,"empty cars today")
print("We can transport",carpool_capacity,"people today")
print("We have",passengers,"to carpool today")
print("We need to put about",average_passengers_per_car,"in each car")

my_name='Zed A.Shaw'
my_age=35 #not a lie
my_height=74 #inches
my_weight=180 #lbs
my_eyes='Blue'
my_teeth='White'
my_hair='Brown'

print("Let's talk about %s." % my_name)
print("He's %d inches tall." % my_height)
print("He's %d pounds heavy." % my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." %(my_eyes,my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)
print("If I add %d,%d,and %d I get %d." %(
    my_age,my_height,my_weight,my_age+my_height+my_weight))

#ex6.py
x="There are %d types of people." % 10
binary="binary"
do_not="don't"
y="Those who know %s and those who %s." %(binary,do_not)

print(x)
print(y)

print("I said:%r." % x)
print("I also said:'%s'." % y)

hilarious=False
joke_evaluation="Isn't that joke so funny?! %r"#去了%r 就错了

print(joke_evaluation % hilarious)

w="This is the left side of..."
e="a string with a right side."

print(w+e)

#ex7.py
print("Mary had a little lamb.")
print("Its fleece was white as %s." % 'snow')
print("And everywhere that Mary went.")
print("."*10) #what'd that do?,print 10 numbers .

end1="C"
end2="h"
end3="e"
end4="e"
end5="s"
end6="e"
end7="B"
end8="u"
end9="r"
end10="8"
end11="e"
end12="r"

print(end1+end2+end3+end4+end5+end6,end7+end8+end9+end10+end11+end12)
#print(end7+end8+end9+end10+end11+end12)

#ex8.py
formatter="%r %r %r %r"

print (formatter % (1,2,3,4))
print(formatter %("one","two","three","four"))
print(formatter %(True,False,False,True))
print(formatter %(formatter,formatter,formatter,formatter))
print(formatter %("I had this thing.",
                  "That you could type up right.",
                  "But it didn't sing.",
                  "So I said goodnight."))
#ex9.py
days="Mon Tue Web Thu Fri Sat Sun"
months="Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days:",days)
print("Here are the month:" ,months)#%,add .
print("""
 There's something going on here.
 With the three double-quotes.
 We'll be able to type as much as we like.
 Even 4 lines if we want,or 5,or 6.""")
print("I am 6'2\" tall.")
print('I am 6\'2" tall.')
tabby_cat="\tI'm tabbed in."#\t空两格
print(tabby_cat)

persian_cat="I'm split\non a line." # \n转到下一行
print(persian_cat)
backslash_cat="I'm\\a\\cat." # 打出\
print(backslash_cat)

 # 三个单引号与双引号的效果是一样的
#fat_cat='''

#I'll do a list:
#\t* Cat food
#\t* Fishies
#\t* Catnip\n\t* Grass
#'''
#print(fat_cat)

#ex11.py
print("How old are you?",age=input())


print("So,you're %r old." % age)

