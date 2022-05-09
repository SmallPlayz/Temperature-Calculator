valid = False

while not valid: #loop until the user enters a valid int
    try:
        temp = float(input('Whats the current temperature? '))
        valid = True #if this point is reached, temp is a valid int
    except ValueError:
        print('Please only input digits\n')
valid = False

while not valid: #loop until the user enters a valid int
    try:
        print('1. Fahrenheit to Celsius\n2. Celsius to Fahrenheit')
        convertPick = int(input('What do you want to convert to? '))
        if(convertPick == 1 or convertPick == 2):
            valid = True #if this point is reached, convertPick is a valid int
        else:
            print('Please only input "1" or "2"\n')
    except ValueError:
        print('Please only input digits\n')
      
if(convertPick == 1):
  print('\n' + str(round(temp, 3)) + ' degrees Fahrenheit in Celsius is ' + str(round((((temp-32)*5)/9), 2)) + ' degrees.')
else:
  print('\n' + str(round(temp, 3)) + ' degrees Celsius in Fahrenheit is ' + str(round(((temp-32)*.5556), 2)) + ' degrees.')