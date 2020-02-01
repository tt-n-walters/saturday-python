from math import floor

def calcuate_fuel(mass):
    # divided = mass / 3
    # floored = floor(divided)
    # subtracted = floored - 2
    # return subtracted
    print("Calculating fuel to carry {}".format(mass))

    return floor(mass / 3) - 2
    return mass // 3 - 2


def total_fuel(masses):
    totals = []
    for mass in masses:
        total = 0
        total += calcuate_fuel(mass)
        print("Now has a total of {}".format(total))

        print("Calculating fuel to carry {}".format(total))
        fuel_to_carry_fuel = calcuate_fuel(total)
        while fuel_to_carry_fuel > 0:
            print("Adding {} to the total.".format(fuel_to_carry_fuel))
            total += fuel_to_carry_fuel
            fuel_to_carry_fuel = calcuate_fuel(fuel_to_carry_fuel)

        totals.append(total)
    return sum(totals)



if __name__ == "__main__":

    import requests

    result = requests.get("https://adventofcode.com/2019/day/1/input", headers={"Cookie": "session=53616c7465645f5fa83960b1e99f2bfb3666e735109ba7aaa30e6e76b8f4fe458e74e9745c89fb3d8bc76b152ed1d446"})

    if result.status_code == 200:
        text = result.text
        split_lines = text.splitlines()

        # converted = []
        # for num in split_lines:
        #     converted.append(int(num))

        converted = list(map(int, split_lines))

        print(total_fuel(converted))

    else:
        print("Error.", result.status_code)