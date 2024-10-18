def main():
    i = 0

    while i <= 9:
        j = 1
        while j >= 5:
            print(f"I={i} J={j}")
            j -= 1
        i += 2

if __name__ == "__main__":
    main()