from PIL import Image
import numpy as np
import random
import os
import multiprocessing

tamanhoDoLote = 42
imagemBase = "logo02.jpeg"
nomeImagens = "novasImagens3/logo"
contadorArquivo = "contagem.txt"
num_processos = multiprocessing.cpu_count()  # Use todos os núcleos disponíveis

# Função para criar imagens com ruído
def addNoise(imagemDeBase, nomeNovaImagem, noiseLevel):
    imagem = Image.open(imagemDeBase)
    imagem_array = np.array(imagem)

    noise = np.random.randint(-noiseLevel, noiseLevel, size=imagem_array.shape, dtype=int)
    imagem_array = np.clip(imagem_array + noise, 0, 255).astype(np.uint8)

    imagem_com_ruido = Image.fromarray(imagem_array)
    imagem_com_ruido.save(nomeNovaImagem, "PNG")

# Função para processar em paralelo
def processar_em_paralelo(i):
    nomeNovaImagem = f"{nomeImagens} {i}.png"
    addNoise(imagemBase, nomeNovaImagem, noiseLevel=10)

if __name__ == "__main__":
    # Abrir documento do contador
    try:
        with open(contadorArquivo, "r") as file:
            numeroAtual = int(file.read())
    except FileNotFoundError:
        print(f"Não encontrei o documento -> {contadorArquivo}")
        numeroAtual = 0

    # Criar imagens em lote em paralelo
    pool = multiprocessing.Pool(processes=num_processos)
    pool.map(processar_em_paralelo, range(numeroAtual, numeroAtual + tamanhoDoLote))
    pool.close()
    pool.join()

    # Atualizar a contagem
    numeroAtual += tamanhoDoLote
    with open(contadorArquivo, "w") as file:
        file.write(str(numeroAtual))

# [Done] exited with code=0 in 15.609 seconds