import datetime

def criar_arquivo(nome_completo, data, local, idade, bairro):
    cabecalho = f"Nome completo: {nome_completo}\nData de hoje: {data}\nLocalidade: {local}\nIdade: {idade}\nBairro: {bairro}\n"

    with open("amanha.txt", "w") as arquivo:
        arquivo.write(cabecalho)
        
        disciplina = input("Informe a disciplina (ou 'sair' para terminar): ")
        while disciplina.lower() != "sair":
            nota = input("Informe sua nota: ")
            arquivo.write(f"{disciplina}, {nota}\n")
            disciplina = input("Informe a disciplina (ou 'sair' para terminar): ")

nome_completo = "ANTONY"
data = datetime.datetime.now().strftime("%d/%m/%Y")
local = "MANAUS, AM"
idade = "19"
bairro = "REDECA"

criar_arquivo(nome_completo, data, local, idade, bairro)
