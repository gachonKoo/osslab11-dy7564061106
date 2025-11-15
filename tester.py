from geo.utils import distance, circle_area

def main():
    c = distance((0, 0), (3, 4))
    area = circle_area(10)
    print(f"c = {c}")
    print(f"area = {area}")

if __name__ == "__main__":
    main()
