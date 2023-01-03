from flask import Flask, jsonify, request
from rembg import remove
from PIL import Image

app = Flask(__name__)

image = [
  {
    "path": "error.jpg",
    "name": "error.jpg",
  }
]

#return data
@app.route('/imagem', methods = ['GET'])
def return_image():
  return jsonify(image)

#remove background
@app.route('/imagem/envio', methods = ['PUT'])
def remover_background():
  image_content = request.get_json()
  image_data = Image.open(image_content)
  removing_bg = remove(image_data).save("foto.png")  
  image[0].update(removing_bg)
  return jsonify(image)

app.run(port=5000, host='localhost', debug=True)