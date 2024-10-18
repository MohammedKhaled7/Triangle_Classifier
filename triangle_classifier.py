def classify_triangle(sides):
    if len(sides) != 3:
        return "Error: Two sides missing" if len(sides) == 1 else "Error: Invalid input"
    try:
        a, b, c = map(int, sides)
    except ValueError:
        return "Error: Invalid input"

    if a <= 0 or b <= 0 or c <= 0:
        return "Error: Side lengths must be positive"

    if a + b <= c or a + c <= b or b + c <= a:
        return "NoTriangle"
    elif a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

def main():
    while True:
        user_input = input("Enter side lengths (or Quit/Exit to stop): ").strip()
        if user_input.lower() in ["quit", "exit"]:
            print("Application exiting...")
            break
        sides = user_input.split()
        print(classify_triangle(sides))

if __name__ == "__main__":
    main()
