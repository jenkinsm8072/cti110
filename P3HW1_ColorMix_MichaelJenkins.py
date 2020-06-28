#CTI-110
#P3HW1-Color Mixer
#Michael Jenkins
#28 June 2020
#

#input color1
#if color1=red, blue, or yellow
#Display "First color accepted"
#else
#display "ERROR! You entered an incorrect primary color."

#input color2
#if color1=red, blue, or yellow
#Display "Second color accepted"
#else
#display "ERROR! You entered an incorrect primary color."

#if color1 is a valid primary color and color2 is a different valid primary color:
#print(your secondary color is (mix of colors))
#else
#print(ERROR...)

color1=(input('Enter a primary color: '))
if color1== 'red':
    print('First color accepted.')
elif color1== 'blue':
    print('First color accepted.')
elif color1== 'yellow':
    print('First color accepted.')
else:
    print('ERROR! You entered an incorrect primary color!')
 
color2=(input('Enter another primary color: '))
if color2== 'red':
    print('Second color accepted.')
elif color2== 'blue':
    print('Second color accepted.')
elif color2== 'yellow':
    print('Second color accepted.')
else:
    print('ERROR! You entered an incorrect primary color!')

if color1=='red' and color2=='blue':
    print('Your secondary color is PURPLE!')
elif color1=='blue' and color2=='red':
    print('Your secondary color is PURPLE!')
elif color1=='red' and color2=='yellow':
    print('Your secondary color is ORANGE!')
elif color1=='yellow' and color2=='red':
    print('Your secondary color is ORANGE!')
elif color1=='blue' and color2=='yellow':
    print('Your secondary color is GREEN!')
elif color1=='yellow' and color2=='blue':
    print('Your secondary color is GREEN!')
else:
    print('ERROR! You may have entered duplicate colors or nonprimary colors. Please try running the program again.')
