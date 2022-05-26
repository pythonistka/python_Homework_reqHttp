import requests

names = ["Thanos", "Hulk", "Captain America"]
powers = {}

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def get_intelligence(name):
    url = "https://www.superheroapi.com/api.php/2619421814940190/search/" + name
    resp = requests.get(url).json()
    result = resp["results"][0]
    intelligence = result["powerstats"]["intelligence"]
    return int(intelligence)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for name in names:
        intelligence = get_intelligence(name)
        powers[name] = intelligence
    print(powers)

    x = 0
    winner = ""
    for k, v in powers.items():
        if v > x:
            x = v
            winner = k
    print(f"Самый умный супергерой {winner} его уровень равен: {x}")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
