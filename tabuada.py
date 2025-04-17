while True: 
    try:
        numero = int(input("Digite um número: "))
    except ValueError: 
        print("❌ Entrada inválida! Por favor, digite um número inteiro.\n")
    else: 
        print(f"\n📌 Tabuada do {numero}:")
        for i in range(1,11):
            print(f'{numero} x {i} = {numero * i}')
        opcao = input('Digite S para sair ou C para continuar: ').upper()
        if opcao[0] == 'S':
            break
        else:
            continue
