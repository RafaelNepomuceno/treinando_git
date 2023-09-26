def numerador_lines(arquivo):
    try:
        with open(arquivo, 'r') as file:
            for idx, line in enumerate(file, start=0):
                print(f"{idx}{line.strip()}")
    except FileNotFoundError:
        print(f"O arquivo '{arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


arquivo = "exemplo.txt"  
numerador_lines(arquivo)

