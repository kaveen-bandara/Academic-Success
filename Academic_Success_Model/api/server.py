from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import pickle

app = Flask(__name__)
model_file = open('api/model.pkl', 'rb')
model = pickle.load(model_file)
CORS(app)

@app.get('/')
def read_root():
    return {'message': 'Iris model API!'}

@app.route('/predict', methods = ['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided!'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected!'}), 400
    
    try:
        data = pd.read_csv(file)
        predictions = model.predict(data)
        return jsonify({'prediction': predictions.tolist()})
    
    except pd.errors.EmptyDataError:
        return jsonify({'error': 'The provided file is empty!'}), 400
    
    except pd.errors.ParserError:
        return jsonify({'error': 'Error parsing file!'}), 400
    
    except Exception as e:
        return jsonify({'error': f'Error processing file: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8000, debug = True)