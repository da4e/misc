#!/usr/bin/python
'''
this script is for calculate the coins need on tecent plane game.
'''
# initial coin
# total of the coin need.
total = 2500
step = total
for x in range(30):
    print '-'*50 + '\r\n' + 'step =' + str(step) 
    if step < 1000:
        step = step + 100
        total = total + step 
    elif step < 10000:
        step = step + 500
        total = total + step
    else:
        total  = total + 10000
    # print 'total=' + str(total)

# print the total of coins need.
print 'total=' + str(total)

