from PIL import Image
import random


tamanhoDoLote = 1
imagemBase = "logoBase.jpeg"
nomeImagens = "NovasImagens\logo"
contadorArquivo = "contagem.txt"


# Função para criar as imagens 
def addNoise(imagemDeBase, nomeNovasImagens, noiseLevel):
    imagem = Image.open(imagemBase)
    width, height = imagem.size
    
    pixels = imagem.load()
    
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x,y]
            
            noise = random.randint(-noiseLevel, noiseLevel)
            r += noise
            g += noise
            b += noise

            r = max(0, min(255, r))
            g = max(0, min(255, g))
            b = max(0, min(255, b))

            pixels[x,y] = (r, g, b)
    
    imagem.save(nomeNovasImagens, "PNG")
    

# Abrir documento do contador
try:
    with open(contadorArquivo, "r") as file:
        numeroAtual = int(file.read())
except FileNotFoundError:
    print(f"Não encontrei o documento -> {contadorArquivo}")
    numeroAtual = 0

# Criar imagens em lote
for i in range(numeroAtual, numeroAtual + tamanhoDoLote):
    nomeNovaImagem = f"{nomeImagens} {i}.png"
    addNoise(imagemBase, nomeNovaImagem, noiseLevel=10)
    
# Atualizar a contagem
numeroAtual += tamanhoDoLote
with open(contadorArquivo, "w") as file:
    file.write(str(numeroAtual))