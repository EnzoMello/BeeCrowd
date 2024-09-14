def main():
    N = int(input())
    numero = 1
    i = 1
    
    while i <= N:
         print(f"{i} {numero} {numero * i}")
         numero += 1
         i += 1

if __name__ == "__main__":
    main()

