import numpy as np
import pandas as pd
import requests
import pickle
import io
import torch
from torchvision import transforms
from PIL import Image
import sys
from disease import disease_dic  # Importing disease_dic from disease.py

# Load the pre-trained model for crop disease detection
disease_model_path = r"C:\xampp\htdocs\agriculture-portal-main\farmer\ML\crop_disease_detection\plant_disease_model.pth"
disease_classes = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']

# Creating an instance of ResNet9 model
try:
    from model import ResNet9
    disease_model = ResNet9(3, len(disease_classes))
except Exception as e:
    print("Error creating ResNet9 model:", e)
    sys.exit(1)

# Loading the model's state dictionary from the saved file
try:
    disease_model.load_state_dict(torch.load(disease_model_path, map_location=torch.device('cpu')))
except Exception as e:
    print("Error loading model state dictionary:", e)
    sys.exit(1)

# Setting the model to evaluation mode
try:
    disease_model.eval()
except Exception as e:
    print("Error setting model to evaluation mode:", e)
    sys.exit(1)

# Custom functions for calculations
def preprocess_image(image_data):
    """
    Preprocess image data for prediction
    """
    try:
        image = Image.open(io.BytesIO(image_data))
        transform = transforms.Compose([
            transforms.Resize(256),
            transforms.ToTensor(),
        ])
        image = transform(image)
        image = torch.unsqueeze(image, 0)  # Add batch dimension
        return image
    except Exception as e:
        print("Error preprocessing image:", e)
        return None

def predict_image(image_data, model=disease_model, classes=disease_classes):
    """
    Predict disease label from image data
    """
    try:
        image = preprocess_image(image_data)
        with torch.no_grad():
            output = model(image)
            _, predicted = torch.max(output, 1)
            prediction = classes[predicted[0].item()]
            return prediction
    except Exception as e:
        print("Error predicting image:", e)
        return None

# Read image data from stdin
try:
    image_data = sys.stdin.buffer.read()
except KeyboardInterrupt:
    print("Error: Interrupted by user.")
    sys.exit(1)
except Exception as e:
    print("Error reading image data:", e)
    sys.exit(1)

# Perform disease prediction on the image data
try:
    prediction_result = predict_image(image_data, model=disease_model, classes=disease_classes)
    if prediction_result is not None:
        # Output the prediction result
        print("<b>Disease Prediction:</b>", prediction_result)
        # Check if the predicted disease exists in the disease dictionary
        if prediction_result in disease_dic:
            print("<br><b>Disease Information==></b></br>", disease_dic[prediction_result])
        else:
            print("No information available for the predicted disease.")
    else:
        print("Failed to predict disease.")
        sys.exit(1)
except Exception as e:
    print("Error performing disease prediction:", e)
    sys.exit(1)
















# import numpy as np
# import pandas as pd
# import requests
# import pickle
# import io
# import torch
# from torchvision import transforms
# from PIL import Image
# import sys

# # Load the pre-trained model for crop disease detection
# disease_model_path = r"C:\xampp\htdocs\agriculture-portal-main\farmer\ML\crop_disease_detection\plant_disease_model.pth"
# disease_classes = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']

# # Creating an instance of ResNet9 model
# try:
#     from model import ResNet9
#     disease_model = ResNet9(3, len(disease_classes))
# except Exception as e:
#     print("Error creating ResNet9 model:", e)
#     sys.exit(1)

# # Loading the model's state dictionary from the saved file
# try:
#     disease_model.load_state_dict(torch.load(disease_model_path, map_location=torch.device('cpu')))
# except Exception as e:
#     print("Error loading model state dictionary:", e)
#     sys.exit(1)

# # Setting the model to evaluation mode
# try:
#     disease_model.eval()
# except Exception as e:
#     print("Error setting model to evaluation mode:", e)
#     sys.exit(1)

# # Custom functions for calculations
# def preprocess_image(image_data):
#     """
#     Preprocess image data for prediction
#     """
#     try:
#         image = Image.open(io.BytesIO(image_data))
#         transform = transforms.Compose([
#             transforms.Resize(256),
#             transforms.ToTensor(),
#         ])
#         image = transform(image)
#         image = torch.unsqueeze(image, 0)  # Add batch dimension
#         return image
#     except Exception as e:
#         print("Error preprocessing image:", e)
#         return None

# def predict_image(image_data, model=disease_model, classes=disease_classes):
#     """
#     Predict disease label from image data
#     """
#     try:
#         image = preprocess_image(image_data)
#         with torch.no_grad():
#             output = model(image)
#             _, predicted = torch.max(output, 1)
#             prediction = classes[predicted[0].item()]

#             return prediction
#     except Exception as e:
#         print("Error predicting image:", e)
#         return None

# # Read image data from stdin
# try:
#     image_data = sys.stdin.buffer.read()
# except KeyboardInterrupt:
#     print("Error: Interrupted by user.")
#     sys.exit(1)
# except Exception as e:
#     print("Error reading image data:", e)
#     sys.exit(1)

# # Perform disease prediction on the image data
# try:
#     prediction_result = predict_image(image_data, model=disease_model, classes=disease_classes)
#     if prediction_result is not None:
#         # Output the prediction result
#         print("Disease Prediction:-", prediction_result)
#     else:
#         print("Failed to predict disease.")
#         sys.exit(1)
# except Exception as e:
#     print("Error performing disease prediction:", e)
#     sys.exit(1)






