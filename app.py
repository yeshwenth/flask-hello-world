import os
from flask import Flask, render_template, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
import boto3
from uuid import uuid4

app = Flask(__name__)

boto3.setup_default_session(region_name='us-west-2')
aws_access_key_id_= os.environ['aws_access_key_id_']
aws_secret_access_key_=os.environ['aws_secret_access_key_']
s3 = boto3.resource('s3',aws_access_key_id=aws_access_key_id_,aws_secret_access_key=aws_secret_access_key_)
dyn = boto3.resource('dynamodb',aws_access_key_id=aws_access_key_id_,aws_secret_access_key=aws_secret_access_key_)
bucket_name = 'infer-test'
image_table = "ramji"
table_name = dyn.Table(image_table)


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
		print(type(f))
		f_new_file_name = str(uuid4())
		print(f_new_file_name)
		f.save(secure_filename(f_new_file_name))
		print("Test test")
		local_path = os.path.abspath(os.getcwd()) + "/" + f_new_file_name
		s3.meta.client.upload_file(local_path, bucket_name, f_new_file_name, ExtraArgs={'ACL':'public-read'})
		# write to dyn
# 		response = table.get_item(
#     Key={
#         'ph_no': '+17752201448'
#     }
# )
		response = table_name.put_item(
	   											Item={
													        'image_id': f_new_file_name,
													        'first_name': 'Jane',
													        'last_name': 'Doe',
													        'age': 25,
													        'account_type': 'standard_user',
	    													}
															)
		return send_file(f_new_file_name, mimetype='image/gif')
		# return redirect(url_for('yesh'))
		

@app.route('/yesh')
def yesh():
	return "redirect to yesh"


if __name__ == '__main__':
   app.run(debug = True)
