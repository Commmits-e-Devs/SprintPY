from CaptarFoto import tirar_foto

opc = int(input("""
Bem vindo a Camera jovi!!!!!!
O que deseja fazer?:
1- Tirar foto
2-(Ainda pensando)
3-(Ainda pensando)
4-Sair
"""))

while opc !=4:
    match opc:
        case 1:
            print("você ira tirar foro agora")
            print("Estamos abrindo")
            tirar_foto()

        case 4:
            break
        case _:
            print("Opão invalida chefe")