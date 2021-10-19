from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

class SVMPrediction:
    def load(data):
        return load_model(data)
    
    def convertImagetoArray(data):
        return img_to_array(data)
        
