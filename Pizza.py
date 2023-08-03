z=input(print('Do you want to order a pizza(yes or no) :'))
while z == 'yes':
    print("What type of Pizza you want Veg or Non-veg ? ")
    x = int(input('Select 1 for Veg or Select 2 for Non-Veg : '))
    y = ['chicken = 10 SEK','lamb = 12 SEK','salami = 15 SEK','prawn = 20 SEK','fish = 18 SEK']

    if x == 1:
        b =input('Do you want Margarita or Veg pizza :')
        c = int(input('How many pizzas :'))
        if b == 'Margarita':
            print('That would be : ',c*10, 'Kronos')
        else:
            print('That would be : ', c * 12, 'Kronos')

    elif x == 2:
        print('Please choose from the following :')
        for i in y:
            print (i)

        a= input('Enter your choice of Non Veg Pizza :')
        c= int(input('How many pizzas :'))
        if a== 'chicken':
            print('That would be :',c*10,'Kronos')
        elif a=='lamb':
            print('That would be :',c*12,'Kronos')
        elif a=='salami':
            print('That would be :',c*15,'Kronos')
        elif a=='prawn':
            print('That would be :',c*20,'Kronos')
        else:
            print('That would be :',c*18,'Kronos')
    z = input(print('Anything else (yes or no):'))

print('Thank you for ordering pizza')