from rembg import remove
from PIL import Image
input_path = 'input.jpeg'
output_path = 'output.jpeg'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)