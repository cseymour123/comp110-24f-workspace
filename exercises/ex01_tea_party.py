"""This excercise handles a tea party where the # of treats and tea are caluclated
And the total cost of the entire tea party."""

__author__: str = "730674510"


# The purpose of this is to be able to call all of the sub functions
# Allowing more efficient use of code
"""The strings before are to make the output more readable."""


def main_planner(guests: int) -> None:
    """This is the main function which calls all of the sub functions
    It Will print out what is is caluclating and then the number"""
    print("A Cozy Tea Party for " + str(guests) + " People")
    print("Tea Bags:", tea_bags(people=guests))
    print("Treats:", treats(people=guests))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests)),
        )
    )
    return None


# The tea_bags function is called using people and setting it equal to guests
# a main_planner parameter. Allowing it to pass infomration amongst sub functions.
# This function assigns people = to guests to calculate the amount
# of treats and tea bags
# This allows the # of bags and treats to be put into the function

"""By returning 2 times the amount of people it calculates how much tea."""


def tea_bags(people: int) -> int:
    """This takes the amount of people multiplies it by
    and then gives the # of tea bags needed"""
    return (people) * 2


"""This gives the # of tea bags based on an amt of people"""


# This defines treats and takes the amount tea bags and multiplies it by 1.5
"""The int in front of tea_bags, makes the answer an integer to avoid error"""


def treats(people: int) -> int:
    """The int in front of tea_bags, makes the answer and integer to avoid error
    It defines treats and takes the amount of tea bags and multiplies it by 1.5"""
    return int(tea_bags(people=people) * 1.5)


# This function adds the amount of money up for treats and snacks
"""This return type must be a float because of the decimal multiplication"""

"""This takes the tea_count and treat_count and multiply and add them up to get the cost
I set tea_count and treat_count as parameters"""


def cost(tea_count: int, treat_count: int) -> float:
    """This takes the tea_count and treat_count and calculate the cost of the party
    tea_count and treat_count as parameters help to call the functions in main_planner
    """
    return (treat_count * 0.75) + (tea_count * 0.50)


# this function is what allows you to input how many guests are attending your tea party
if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
