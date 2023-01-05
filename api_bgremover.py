from flask import Flask, request, send_file, jsonify
from rembg import remove
from PIL import Image
import base64
import sys
import json

app = Flask(__name__)

@app.route('/remove_bg', methods = ['PUT'])
def send_image():
  file = request.files['image']
  img = Image.open(file.stream)
  removing_bg = remove(img).save("foto.png")
  return send_file("./foto.png", as_attachment=True)


@app.route('/remove_bg64', methods = ['PUT'])
def send_image64():
  file = request.files['image']
  img = Image.open(file.stream)
  removing_bg = remove(img).save("foto.png")
  with open("foto.png", 'rb') as image_file:
    data64 = base64.b64encode(image_file.read())
  return json.dumps({ "image": str(data64).split("'")[1]})


app.run(port=5000, host='0.0.0.0', debug=True)
