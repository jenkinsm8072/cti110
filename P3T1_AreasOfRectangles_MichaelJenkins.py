#compare areas of rectangles
#28 June 2020
#CTI-110 P3T1-Areas of Rectangles
#

#input length and width of rectangle 1
length1= int(input('What is the length of Rectangle 1?: '))
width1= int(input('What is the width of Rectangle 1?: '))

#input length and width of rectangle 2
length2= int(input('What is the length of Rectangle 2?: '))
width2= int(input('What is the width of Rectangle 2?: '))
#Calculate area of rectangle 1
area1= length1 * width1
#calculate area of rectangle 2
area2= length2 *width2
#if area1>area2
#display "Rectangle 1 has the greatest area."
if area1 > area2:
    print('Rectangle 1 has the greater area.')
#elif area2 > area1
#display "Rectangle 2 has the greatest area."
elif area2 >area1:
    print('Rectangle 2 has the greater area.')
#else
#display "Both rectangles have the same area."
else:
    print('Both rectangles have the same area.')



