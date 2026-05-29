# info ={
#         "Small size": 15,
#         "Meduim size": 20,
#         "Large size": 25,
#         "Pep s": 2,
#         "Pep m and l": 3,
#         "Chesse": 2   
#         }
# print('''
#             Small size pizza is Ghc100
#             Meduim size pizza is Ghc125
#             Large size pizza is Ghc150
#             Family size is Ghc200
#             ''')
# y = input("What type of pizza do you want, answer with these words(Small size,Meduim size,Large size): ")
# info[y]

# p =input("Do you want peproni? ")
# if p =="yes":
#     print(f'Your bill now is {info[y]} ')
# ss=str(17)
# ms=str(23)
# ls=str(28)
# Small_size=str(15)
# Meduim_size= str(20)
# Large_size= str(25)

# a=input("Which size of pizza do you want? ")
# if a.lower()=="small":
#     print(f'Your bill now is ${Small_size}')

# elif a.lower()=="medium":
#     print(f'Your bill now is ${Meduim_size}')

# elif a.lower()=="large":
#     print(f'Your bill now is ${Large_size}')

# add_pep=input("Do you want peproni added?")
# if add_pep.lower()=="yes":
#     if a.lower()=="small":
#         print(f'Your bill is ${15+2}')
#     elif a.lower()=="medium":
#         print(f'Your bill is ${20+3}')
#     elif a.lower()=="large":
#         print(f'Your bill is ${25+3}')
# chesse=input("Do you want extra chesse? ")
# if chesse.lower()=="yes":
#     if add_pep=="17":
#         print(f'Your bill is ${ss+2}')
#     elif add_pep=="23":
#         print(f'Your bill is ${ms+2}')
#     elif add_pep=="25":
#         print(f'Your bill is ${ls+2}')
# else:
#     print("O")
while True:
    size=str(input("What size of pepperoni do you want? S,M,L "))
    add_pepperoni=str(input("Do want pepperoni added? Y OR N "))
    add_chesse= input("Do you want extra chesse added? ")
    pepperoni_for_small=2
    pepperoni_for_medium=3
    pepperoni_for_large=3
    chesse=2
    bill=0
    small_pizza=15
    meduim_pizza=20
    large_pizza=25
    if size=="S":
        bill+=small_pizza
        if add_pepperoni =="Y":
            bill+= pepperoni_for_small
    elif size== "M":
        bill+= meduim_pizza
        if add_pepperoni =="Y":
            bill+= pepperoni_for_medium
    elif size== "L":
        bill+= large_pizza
        if add_pepperoni =="Y":
            bill+= pepperoni_for_large
    else:
        print("Enter the right alphabet to get your actual bill")

    if add_chesse=="Y":
        bill+=chesse
    else:
        bill

    print(f'Your bill is ${bill}')

