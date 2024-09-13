"""Will calculate number of items for guests at a party"""

__author__ = "730741975"


def main_planner(guests: int) -> None:
    """The main function that runs the tea party planner."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests))))


def tea_bags(people: int) -> int:
    """the function below provides number of teabags for guests"""
    return people * 2


def treats(people: int) -> int:
    """Calculates the number of treats needed based on the number of teas guests will drink"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the total cost of tea bags and treats."""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
