"""
1. Create a while loop with the following characteristics:

• The initial value of the variable x will be 0.
• The increment value will be 1.
• The exit condition of the loop will be greater than or equal to 30.
• The execution must be broken when x is equal to 15.
• You must print the following sentence each time the loop executes: 'The value of the loop is: ' + x.
• You must skip the executions with the value of x in 4, 6 and 10.
• At each execution jump, you must display the jumped values with this message: 'The value ' + x ' of x was skipped'.
• When the execution of the loop is broken, you must show a message indicating it: 'The execution of the loop was broken when x was ' + x.
"""

# Respuesta

x = 0
while x < 30:
    if x == 15:
        print(f"The execution of the loop was broken when x was {x}.")
        x += 1
        break
    elif x == 4 or x == 6 or x == 10:
        print(f"The value {x} of x was skipped.")
        x += 1
        continue
    else:
        print('The value of the loop is: ', x)
    x += 1

