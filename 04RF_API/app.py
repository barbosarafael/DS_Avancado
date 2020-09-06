from flask import Flask
from flask import request
import numpy as np
from pickle import load

app = Flask(__name__)
model = load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return "Funcionou essa desgraça? Sim"

@app.route('/results', methods=['POST'])
def predict():
    
    r = request.form

    data = [float(x) for x in r.values()]
    data = np.array(data).reshape(1, -1)

    prediction = model.predict(data)
    prediction = str(prediction)
    
    return {'prediction': prediction}

if __name__ == "__main__":
    app.run(debug=True)