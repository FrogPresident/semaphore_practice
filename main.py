import json
import numpy


# json
# x = {
#     "name": "jason",
#     "age": "20",
#     "city": "Taipei"
# }


def main():

    x = {
        "name": "John",
        "age": 30,
        "married": True,
        "divorced": False,
        "children": ("Ann", "Billy"),
        "pets": None,
        "cars": [
            {"model": "BMW 230", "mpg": 27.5},
            {"model": "Ford Edge", "mpg": 24.1}
        ]
    }
    k = [123, 4232321]
    y = json.dumps(k)
    z = json.loads(y)
    print(repr(y))
    print(repr(z))
    print(json.dumps(y, indent=4, separators=("`123 ", " = "), sort_keys=True))


if __name__ == '__main__':
    main()
