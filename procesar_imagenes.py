from rembg import remove
from PIL import Image
import io
import os

input_folder = r'D:\PY\a'
output_folder = r'D:\PY\a\procesadas_sin_fondo'  # Carpeta para guardar las imágenes sin fondo
final_folder = r'D:\PY\a\finales_fondo_blanco'  # Carpeta para guardar las imágenes con fondo blanco

# Crear las carpetas de salida si no existen
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
if not os.path.exists(final_folder):
    os.makedirs(final_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg')):  # Filtrar imágenes
        input_image_path = os.path.join(input_folder, filename)
        
        # Abrir la imagen y procesarla para eliminar el fondo
        with open(input_image_path, 'rb') as input_file:
            input_data = input_file.read()
            output_data = remove(input_data)
        
        # Guardar la imagen sin fondo (en formato PNG para mantener la transparencia)
        output_image_path = os.path.join(output_folder, filename)
        with open(output_image_path, 'wb') as output_file:
            output_file.write(output_data)
        
        # Abrir la imagen procesada (con fondo transparente)
        image = Image.open(output_image_path)

        # Redimensionar la imagen para que se ajuste dentro de 1000x1000 sin distorsionar
        image.thumbnail((1000, 1000))  # Mantiene la relación de aspecto original

        # Crear un fondo blanco de 1000x1000 píxeles
        background = Image.new("RGBA", (1000, 1000), (255, 255, 255, 255))

        # Pegar la imagen procesada sobre el fondo blanco, centrada
        offset = ((1000 - image.width) // 2, (1000 - image.height) // 2)  # Centrar la imagen
        background.paste(image, offset, image.convert("RGBA"))

        # Guardar la imagen final con fondo blanco en la carpeta final
        final_image_path = os.path.join(final_folder, filename)
        final_image_path = final_image_path.replace('.jpg', '.png').replace('.jpeg', '.png')  # Reemplazar la extensión a PNG
        background.save(final_image_path)

        print(f"Imagen procesada y guardada en: {final_image_path}")