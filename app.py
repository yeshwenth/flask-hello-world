import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import boto3

app = Flask(__name__)

boto3.setup_default_session(region_name='us-west-2')
aws_access_key_id_= os.environ['aws_access_key_id_']
aws_secret_access_key_=os.environ['aws_secret_access_key_']
s3 = boto3.resource('s3',aws_access_key_id=aws_access_key_id_,aws_secret_access_key=aws_secret_access_key_)


@app.route('/')
def home():
	return "home"


@app.route('/upload')
def upload_file():
   return render_template('index.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_files():
	if request.method == 'POST':
		f = request.files['file']
		# create a unique file name
		f.save(secure_filename(f.filename))
		print("Test test")
		return redirect(url_for('yesh'))
		

@app.route('/yesh')
def yesh():
	return "redirect to yesh"


if __name__ == '__main__':
   app.run(debug = True)


 # steps
 # 1. Upload the image
 # 2. Once the image is uploaded, save the image in unique name, put it in S3
 # 3. Use that image, pass it to the ML function, that returns the predicted output
 # 4. Return that output to the user
