# name = input('enter your name')
# height1 = int(input('enter your height'))
# name2 = input('enter your name')
# height2 = int(input('enter your heigght'))

# if (height1 > height2):
#   print(f'{name}is taller than {name2}')
# elif(height1==height2):
#   print(f'{name} and {name2} are equal in height')
# else:
#   print(f'{name2} is taller than {name}')

# stock1 = 'vanilla'
# stock2 = 'lime'
# stock3 = 'chocolate'

fav = input('enter your favorite flavor')
# # if(fav==stock1 or fav==stock2 or fav==stock3):
# or
shop_stock = 'vanila', 'lime', 'chocolate'
# if(fav in shop_stock)

#   print('yes,we do have it')

# else:
#   print('No,we ran out of stock')
print('yes we do have it' if fav in shop_stock else 'no we ran out of stock')
