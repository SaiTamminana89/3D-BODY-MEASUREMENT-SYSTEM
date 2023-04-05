from flask import Flask, request, render_template
import trimesh
import numpy as np
import pickle
from tensorflow.keras.models import load_model
import os
from io import BytesIO
model = load_model('nemodel.h5')
app = Flask(__name__)

@app.route('/')
def ma():
    return render_template("me.html")

@app.route('/predict', methods=['POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        data = file.read()
        mesh = trimesh.load(BytesIO(data), file_type='obj')
        vertices = np.array(mesh.vertices)
        remaining_rows=62244-vertices.shape[0]
        if remaining_rows>0:
            for i in range(remaining_rows):
                vertices = np.append(vertices,np.array([[0,0,0]]),axis=0)
        vertices = vertices/vertices.max()
        p = np.reshape(vertices, [1,62244,3,1])
        predictions = model.predict(p).tolist()
        pred = predictions[0]
        results = {'Seat_Back_Angle':pred[0],'MEASURE CrotchLength_Front':pred[1],'MEASURE CrotchLength_Back':pred[2],'MEASURE Knee_Circ':pred[3],'MEASURE Calf_Circ':pred[4],'MEASURE Outseam':pred[5],'MEASURE Inseam':pred[6],'MEASURE Shoulder_to_Wrist':pred[7],'MEASURE Bicep_Circ':pred[8],'MEASURE Elbow_Circ':pred[9],'MEASURE Wrist_Circ':pred[10],' MEASURE Shoulder_to_Shoulder':pred[11],'MEASURE Across_Front':pred[12],'MEASURE Neck_Circ':pred[13]}
          												
    return results
if __name__ == '__main__':
    app.run(debug=True)
   		 			
