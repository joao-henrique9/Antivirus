import os

def localizar_arquivos(caminho_inicial, extensoes, nomes_especificos=None):
    """
    Localiza arquivos específicos em um diretório e seus subdiretórios.

    :param caminho_inicial: Diretório inicial para busca.
    :param extensoes: Lista de extensões de arquivo a serem buscadas.
    :param nomes_especificos: Lista opcional de nomes de arquivos a serem buscados.
    :return: Lista de caminhos dos arquivos encontrados.
    """
    arquivos_encontrados = []

    for root, dirs, files in os.walk(caminho_inicial):
        for file in files:
            if any(file.endswith(ext) for ext in extensoes):
                if nomes_especificos:
                    if any(nome.lower() in file.lower() for nome in nomes_especificos):
                        arquivos_encontrados.append(os.path.join(root, file))
                else:
                    arquivos_encontrados.append(os.path.join(root, file))

    return arquivos_encontrados


# Configuração inicial
caminho_inicial = input("Digite o local do arquivo que deseja encontrar: ").strip()  # Exemplo: C:/Users/SeuUsuario/Downloads
extensoes = ['.bat', '.exe']

# Opcional: nomes de arquivos específicos
print("Digite os nomes de arquivos específicos para buscar (separados por vírgula), ou pressione Enter para mostrar todos:")
nomes_input = input().strip()

if nomes_input:
    nomes_especificos = [nome.strip() for nome in nomes_input.split(",")]
else:
    nomes_especificos = None

# Localizando os arquivos
arquivos = localizar_arquivos(caminho_inicial, extensoes, nomes_especificos)

# Exibindo resultados
if arquivos:
    print(f"Arquivos encontrados: ({len(arquivos)})")
    for arquivo in arquivos:
        print(arquivo)
else:
    print(f"Não foi encontrado nenhum arquivo com o seguinte nome: {nomes_input}")
