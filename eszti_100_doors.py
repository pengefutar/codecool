# Lukács Eszti's 100 doors program! 

# Here I define the doors function. 
# Inside the bracket you will define how many doors you want to run the program with.
def doors(num_of_doors):

    # This creates the list of the desired amount (= ***) of closed doors
    open = [False] * num_of_doors

    # y opens/closes the necessary doors on the list of *** doors created above, 
    # x repeats it *** times
    for x in range(0, num_of_doors):
        for y in range(x, num_of_doors, x+1):
            if open[y] == False:
                open[y] = True
            else:
                open[y] = False

    # A list of the index numbers of the opened doors.
    # We also need to add one to the index numbers, because it starts with 0.
    a = []    
    for z in range(0, num_of_doors):
        if open[z] == True:
            a.append(z+1)

    # Print out the doors in the desired format.
    print("The following doors are open:", end=' ')
    print(*a, sep=', ')


# The function needs to be called. 
# We define the number of doors inside the brackets.
# I wrote 100, because that was what the assignment asked us to do,
# but I could change this number very easily if I wanted to.
doors(100)


