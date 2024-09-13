def get_weathher_report() -> str:
    weather: str = input("What is the weather?")

    if weather == ("rainy" or "cold"):
        print("bring a jacket")
    elif weather == ("hot"):
        print("keep cool out there!")
    else:
        print("I don't recognize this weather")

    return weather


get_weathher_report()
