from flask import Flask, request, jsonify
import pickle
import os

from training.train import train_model


app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "alive"

@app.route("/train", methods=["GET"])
def train():
    """
    GET route "/train" to train a model and save it into /models/model.pickle. 
    """
    train_model()
    return 'Model trained.'

@app.route("/predict", methods=["POST"])
def predict():
    print('Prossessing post request at /predict...')
    # Get data Expect data formatted like: {"data": [3,5,4,2]}
    data_request = request.get_json()
    # Get the value of data_request['data']
    data_to_predict = data_request.get('data', [])
    print('request data: ', data_to_predict)
    # Load model
    model = pickle.load(open('models/model.pickle', 'rb'))
    # Do the prediction
    prediction = model.predict([data_to_predict])[0]
    print("model prediction: ", prediction)
    # Return prediction to user
    return jsonify({'prediction': str(prediction)})



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=os.environ.get("PORT", 5000))