import torch
from PIL import Image
from torchvision import transforms, models
import requests

class Model:
    def __init__(self):
        torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.weights  = models.ResNet50_Weights.DEFAULT
        self.model = models.resnet50(weights=self.weights)
        self.preprocess = self.weights.transforms()

    def predict(self, imageURL):
        image = Image.open(requests.get(imageURL, stream=True).raw)
        image = self.preprocess(image)
        image = image.unsqueeze(0)
        output = self.model(image).squeeze(0).softmax(0)
        class_id = output.argmax().item()
        print(class_id)
        category = self.weights.meta["categories"][class_id]
        return category