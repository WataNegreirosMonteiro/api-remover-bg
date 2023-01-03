from flask import Flask, request, send_file
from rembg import remove
from PIL import Image

app = Flask(__name__)

@app.route('/remove_bg', methods = ['PUT'])
def send_image():
  file = request.files['image']
  img = Image.open(file.stream)
  removing_bg = remove(img).save("foto.png")
  return send_file("./foto.png", as_attachment=True)

app.run(port=5000, host='0.0.0.0', debug=True)