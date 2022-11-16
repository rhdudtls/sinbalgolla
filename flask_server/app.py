from flask import Flask, request
from sklearn.cluster import KMeans
import random as rng
from imutils import contours
from skimage.io import imread
import os
from utils import *
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

app = Flask(__name__)
cred = credentials.Certificate('newbal.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
@app.route('/',methods = ["GET", "POST"])

def home():
    
    img = request.files['image']
    oimg = imread(img)
    if not os.path.exists('output'):
        os.makedirs('output')
    
    preprocessedOimg = preprocess(oimg)
    clusteredImg = kMeans_cluster(preprocessedOimg)
    edgedImg = edgeDetection(clusteredImg)
    boundRect, contours, contours_poly, img = getBoundingBox(edgedImg)
    pdraw = drawCnt(boundRect[1], contours, contours_poly, img)
    croppedImg, pcropedImg = cropOrig(boundRect[1], clusteredImg)
    newImg = overlayImage(croppedImg, pcropedImg)
    fedged = edgeDetection(newImg)
    fboundRect, fcnt, fcntpoly, fimg = getBoundingBox(fedged)
    fdraw = drawCnt(fboundRect[2], fcnt, fcntpoly, fimg)
    ofs, ofb = calcFeetSize(pcropedImg, fboundRect)
    widthsize = footsizeChange(ofs, ofb)
    footsize = {'footsize':ofs, 'width':ofb}
    ofs = str(ofs)
    ofb = str(ofb)
    users_ref = db.collection(u'users')
    docs = users_ref.stream()
    id_list = []
    for doc in docs:
        id_list.append(doc.id)
    users_ref = db.collection(u'users')
    docs = users_ref.stream()
    list1 = []
    for doc in docs:
        list1.append(doc.to_dict())
    list2 = []
    for i in range(len(list1)):
        if(list1[i]['footsize'] == '270'):
            list2.append(i)
    for j in list2:
        user_ref = db.collection(u'users').document(id_list[j])
        user_ref.update({
            'footsize': ofs,
            'width': ofb,
            'widthsize' : widthsize
        })

    return footsize

if __name__ == '__main__':
    app.run(port=4040, debug=True)