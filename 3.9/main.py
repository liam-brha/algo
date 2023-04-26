# recursive example

def nSquares(n, total):
    match n:
        case 1: return total + 1
        case _: return nSquares(n - 1, total + n**2)

countNsquares = lambda n: nSquares(n, 0)

print(nSquares(10, 0))
