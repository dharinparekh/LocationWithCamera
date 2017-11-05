from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import os
import json
from flask import Flask , request , send_file , send_from_directory
from flask_cors import CORS
from tensorflow_for_poets_2.scripts import label_image
import time
import math
import os
import sys
import tensorflow as tf
import time

# Add the ptdraft folder path to the sys.path list
fileCount= 1
app = Flask(__name__)
CORS(app)
BASE_FOLDER = '/home/snc19/Server'
UPLOAD_FOLDER = BASE_FOLDER+'/images'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
sys.path.append('/root')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/getStringImage',methods=['POST'])
def getStringImage():
    global fileCount
    jsonData = json.loads(request.data)
    strImage = jsonData['image']
    tstamp = int(time.time())
    filename = str(tstamp)+'.jpg'
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    print(file_path)
    fh = open(file_path,'wb')
    fh.write(strImage.decode('base64'))
    fh.close()
    #call location model and get the location
    locationOfImage = label_image.main_label(file_path)
    print("---------------------")
    print(locationOfImage)
    print("---------------------")
    return_str = "Location: "+str(locationOfImage)
    return json.dumps({'out':return_str})

app.run(host='192.168.43.23',port=5000,debug=True)
