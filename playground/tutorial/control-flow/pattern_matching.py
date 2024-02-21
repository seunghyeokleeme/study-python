def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 401 | 403 | 418:
            return "Not allowed"
        case 404:
            return "Not Found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

class Point:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

match points:
    case []:
        print("No points")
    case [Point(0, 0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")

match point:
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal")