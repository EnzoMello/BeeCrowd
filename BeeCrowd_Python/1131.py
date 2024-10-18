def main():
    grenais = 0
    vitorias_inter = 0
    vitorias_gremio = 0
    empates = 0

    continuar = 1

    while continuar == 1:
        gols_inter, gols_gremio = input().split()
        gols_inter = int(gols_inter)
        gols_gremio = int(gols_gremio)

        if gols_inter > gols_gremio:
            vitorias_inter += 1
        if gols_gremio > gols_inter:
            vitorias_gremio += 1
        if gols_inter == gols_gremio:
            empates += 1
        
        grenais += 1

        print("Novo grenal (1-sim 2-nao)")
        continuar = int(input())

    print(f"{grenais} grenais")
    print(f"Inter:{vitorias_inter}")
    print(f"Gremio:{vitorias_gremio}")
    print(f"Empates:{empates}")

    if vitorias_inter > vitorias_gremio:
        print("Inter venceu mais")
    if vitorias_gremio > vitorias_inter:
        print("Gremio venceu mais")
    if vitorias_inter == vitorias_gremio:
        print("Nao houve vencedor")

if __name__ == "__main__":
    main()
