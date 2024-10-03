#tulpla
campos = ("Nome", "idade", "profissão", "email")

usuario = {}
#entrada de dados
for campo in campos:
    usuario[campo] = input(f"Informe o valor do campo {campo}: ")
#exibe os valores do dicionario
    print("DADOS DO USUARIO:\n")
    for campo in campos:
        print(f"{campo}: {usuario.get("campo")}.")

       






