def main():
    N = int(input())
    i = 1
    while i <= N:
        print(f"{i} {i} {i * i}")
        print(f"{i} {i + 1} {i * (i + 1)}")
        i += 1


main()
