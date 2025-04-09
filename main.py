from PIL import Image
from rembg import remove
import io

# Caminho da imagem original (com fundo)
input_path = "davi.jpg"
output_path = "foto_3x4.png"

# Tamanho padrão 3x4 cm em 300 DPI = 354x472 pixels
final_size = (354, 472)

# 1. Remover o fundo da imagem
with open(input_path, "rb") as f:
    img_bytes = f.read()
removed_bytes = remove(img_bytes)

# 2. Abrir imagem já sem fundo
img = Image.open(io.BytesIO(removed_bytes)).convert("RGBA")

# 3. Redimensionar proporcionalmente
img.thumbnail(final_size, Image.LANCZOS)

# 4. Criar fundo branco e centralizar imagem
background = Image.new("RGBA", final_size, (255, 255, 255, 255))
x = (final_size[0] - img.width) // 2
y = (final_size[1] - img.height) // 2
background.paste(img, (x, y), img)

# 5. Salvar imagem final (com fundo branco e sem transparência)
final_img = background.convert("RGB")
final_img.save(output_path)

print("✅ Imagem 3x4 salva com sucesso em:", output_path)
