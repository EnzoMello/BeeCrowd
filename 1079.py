#ENTRADA
def main():
    N = int(input())
    contador = 0

#PROCESSO
    while contador <= N:
      valores = input().split()
      valor1 = float(valores[0])
      valor2 = float(valores[1])
      valor3 = float(valores[2])

      media_ponderada = (valor1 * 2 + valor2 * 3 + valor3 * 5)/ 10
      print(f"{media_ponderada:.1f}")
    
main()