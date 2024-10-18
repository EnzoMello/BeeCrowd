#ENTRADA
def main():
  N = int(input())

contador = 1

#PROCESSO
while contador<= 10000:
    if contador % N == 2:
        print(contador)
    contador +=1

main()