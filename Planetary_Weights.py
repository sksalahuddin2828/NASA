# Use constants
MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14

def main():
    # Prompt user to enter weight and store weight as well
    earth_weight = float(input("Enter a weight on Earth: "))

    # Prompt the user for a planet
    planet = input("Enter a planet: ")
    planet = planet.lower().capitalize()
    
    # Ensure that the user enters a planet
    while planet != "Mercury" and planet != "Venus" and planet != "Mars" and planet != "Jupiter" and planet != "Saturn" and planet != "Uranus" and planet != "Neptune":
        if planet == "Earth":
            print("Please select a planet other than Earth.")
        else: 
            print("Error: " + planet + " is not a planet.")

        planet = input("Enter a planet: ").lower().capitalize()

    # Calculate corresponding weight on the inputted planet
    # Assume that the user entered a planet correctly
    if planet == "Mercury":
        planet_weight = earth_weight * MERCURY_GRAVITY

    elif planet == "Venus":
        planet_weight = earth_weight * VENUS_GRAVITY

    elif planet == "Mars":
        planet_weight = earth_weight * MARS_GRAVITY

    elif planet == "Jupiter":
        planet_weight = earth_weight * JUPITER_GRAVITY

    elif planet == "Saturn":
        planet_weight = earth_weight * SATURN_GRAVITY
    
    elif planet == "Uranus":
        planet_weight = earth_weight * URANUS_GRAVITY
    
    else:
        planet_weight = earth_weight * NEPTUNE_GRAVITY

    # Round it two decimal places
    planet_weight_rounded = round(planet_weight, 2)

    # Print the output
    print("The equivalent weight on " + planet + ": " + str(planet_weight_rounded))
    
if __name__ == "__main__":
    main()

  
# Answer: Enter a weight on Earth: 3.15
#         Enter a planet: mars
#         The equivalent weight on Mars: 1.19

  
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

  
# Planetary Weights Solution
# There are two key parts to this solution:

# 1. Everything from the first part of the problem: getting a user's input, converting it to a float to do the calculation, and covering it to a string to print it out.
# 2. Using if statements to check which gravitational constant to use based on the user's input.  
