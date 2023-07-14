# Use constants
MARS_MULTIPLE = 0.378

def main():
    earth_weight_str = input('Enter a weight on Earth: ')

    # Get the numeric value since input() returns a value in string form
    earth_weight = float(earth_weight_str)

    # Having a variable for each piece of information is a good habit
    mars_weight = earth_weight * MARS_MULTIPLE
    rounded_mars_weight = round(mars_weight, 2)

    # Note the string concatenation!
    print('The equivalent weight on Mars: ' + str(rounded_mars_weight))

if __name__ == '__main__':
    main()


#--------------------------------------------------------------------------------------------

# Mars Weight Solution
# There are three key stages to solving this problem:

# 1. Getting the Earthling's weight from them, which I need the input function for. 

# 2. Converting the Earthing's weight from a string to a number so I can do math with it. 
# I use the float function to do this, since the weight isn't necessarily a whole number

# 3. Calculating the weight on Mars, which I do by multiplying the Earth weight by 0.378. 
# To make the program easy to read, I store this number in a constant called MARS_MULTIPLE.
