from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
app = Flask(__name__)

dic = {0 : 'Cat', 1 : 'Dog'}

model = load_model('dog_cat_model.h5')

model.make_predict_function()

def predict_label(img_path):
	i = image.load_img(img_path, target_size=(150,150))
	i = image.img_to_array(i)/255.0
	i = i.reshape(1, 150,150,3)
	p = np.argmax(model.predict(i),axis=1)
	return dic[p[0]]

# routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")

@app.route("/about")
def about_page():
	return "Please subscribe  Artificial Intelligence Hub..!!!"

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']

		img_path = "static/" + img.filename	
		img.save(img_path)

		p = predict_label(img_path)

	return render_template("index.html", prediction = p, img_path = img_path)


if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)
