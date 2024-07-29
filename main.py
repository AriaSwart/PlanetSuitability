# This is the main function that is called on
# The function will check a list of strings for the most viable planet based on a set of rules
def find_suitable_planet(planets: list, max_size: int):
    best_world = ""
    best_size = 0

    # Run through list and compare potential worlds
    for world in planets:
        size = planet_suitability(world)
        if max_size >= size and size > best_size:
            best_world = world
            best_size = size

    # If an eligible world was not found, then best_world should still be an empty string
    return(best_world)
    

# This function returns a score to determine a planet's sutability score, which will be used for comparison
# The string must include "H", "O", "N", "C", "P", "Ca" to be an eligible planet
# Any ineligibility will be returned as 0
def planet_suitability(world: str) -> int:
    eligible = False

    # Check if all elements other than C are present - Check for C separately to prevent false positives
    if ("H" in world) and ("O" in world) and ("N" in world) and ("P" in world) and ("Ca" in world):
        track = ""
        size = ""

        # Run through string and check for a lonestanding C
        for character in world:
            if character != "a" and track == "C":
                eligible = True

            # This section catches the size of the planet
            elif track == "_":
                size = size + character

            # Use variable to iterate and track work through the string
            if track != "_":
                track = character

    # Attempt to return size of eligible planets
    try:
        if eligible == True:
            return(int(size))

    # Catches all ineligible planets and returns 0
    except:
        return(0)
    
    # This line was added because using the finally clause created issues and only using the except 
    # clause caused other issues
    return(0)


# Test print line
print(find_suitable_planet(["HONCCaPC_100", "HONCaPC_150", "HOCCaPC_175", "HONCCaPC_300"], 250))
