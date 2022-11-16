import numpy as np
from PIL import Image
from feature_extractor import FeatureExtractor
from datetime import datetime
from flask import Flask, request, render_template
from flask_cors import CORS
from flask_restful import Api
from pathlib import Path
import flask
import base64
import cv2
import requests
import json
from data_list import load_img_list

### 원본 코드 ###
# app = Flask(__name__)

# # Reading img features
# fe = FeatureExtractor()
# features = []
# img_paths = []

# for feature_path in Path("./static/feature").glob("*.npy"):
#     features.append(np.load(feature_path))
#     img_paths.append(Path("./static/img") / (feature_path.stem + ".jpg"))
# features = np.array(features)

# @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         file = request.files["query_img"]
        
#         # Save query img
#         img = Image.open(file.stream) # PIL image
#         uploaded_img_path = "static/uploaded/" + datetime.now().isoformat().replace(":", ".") + "_" + file.filename
#         img.save(uploaded_img_path)
        
#         # Run Search
#         query = fe.extract(img)
#         dists = np.linalg.norm(features - query, axis=1) # L2 distance to the features
#         ids = np.argsort(dists)[:30]    # Top 30 results
#         scores = [(dists[id], img_paths[id]) for id in ids]
        
#         print(scores)
        
#         return render_template("index.html", query_path=uploaded_img_path, scores=scores)
#     else:
#         return render_template("index.html")

# if __name__=="__main__":
#     app.run()
     
### 여기까지 ###







app = Flask(__name__)
CORS(app, supports_credentials=True) # 다른 포트번호에 대한 보안 제거
api = Api(app)

# Reading img features
fe = FeatureExtractor()

features_top, features_bottom, df_top, df_bottom = load_img_list()

@app.route("/upload", methods=["POST"])
def upload():
    if request.method == "POST":
        file = request.get_json()["file"].split(",")[1]
        
        decoded_file = base64.b64decode(file)
        
        img_np = np.fromstring(decoded_file, dtype=np.uint8)
        
        img = cv2.imdecode(img_np, flags=cv2.IMREAD_COLOR)
        
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        img = Image.fromarray(img.astype('uint8'))
        
        # img.show() 
        
        # image_parsing {"outer" : [np.array, ...], "shortsleeve" : [np.array, ...], }
        array_top, array_bottom = run(img)
        
        if array_top:
            imgs_top = [Image.fromarray(img.astype('uint8')) for img in array_top]
            
            # Run Search
            dict_top = {}
            
            for idx, img_top in enumerate(imgs_top):
                query_top = fe.extract(img_top)
                dists_top = np.linalg.norm(features_top - query_top, axis=1)
                ids_top = np.argsort(dists_top)[:30] # top result sort
                
                result_img_path_top = [df_top.iloc[id]['path_url'] for id in ids_top]
                result_img_link_top = [df_top.iloc[id]['url'] for id in ids_top]
                result_img_score_top = [dists_top[id] for id in ids_top]
                
                dict_top[f'top_{idx}'] = {"result_img_path_top" : result_img_path_top,
                                        "result_img_link_top" : result_img_link_top,
                                        "result_img_score_top" : result_img_score_top}
        
            
            
        if array_bottom:
            imgs_bottom = [Image.fromarray(img.astype('uint8')) for img in array_bottom]
        
            # Run Search
            dict_bottom = {}
            
            for idx, img_bottom in enumerate(imgs_bottom):
                query_bottom = fe.extract(img_bottom)
                dists_bottom = np.linalg.norm(features_bottom - query_bottom, axis=1)
                ids_bottom = np.argsort(dists_bottom)[:30] # top result sort
                
                result_img_path_bottom = [df_bottom.iloc[id]['path_url'] for id in ids_bottom]
                result_img_link_bottom = [df_bottom.iloc[id]['url'] for id in ids_bottom]
                result_img_score_bottom = [dists_bottom[id] for id in ids_bottom]
                
                dict_bottom[f'bottom_{idx}'] = {"result_img_path_bottom" : result_img_path_bottom,
                                                "result_img_link_bottom" : result_img_link_bottom,
                                                "result_img_score_bottom" : result_img_score_bottom}
        
        
        return flask.jsonify({"result" : "true",
                              "number_of_top" : str(len(array_top)),
                              "top" : str(dict_top),
                              "number_of_bottom" : str(len(array_bottom)),
                              "bottom" : str(dict_bottom)})
    else:
        return flask.jsonify({"result" : "false"})
    

if __name__=="__main__":
    # app.run(host=0.0.0.0, port=5000) 모든 호스트로 접속 가능.
    app.run()   
