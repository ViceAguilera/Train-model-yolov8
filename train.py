from ultralytics import YOLO

# Se carga el modelo
model = YOLO("yolov8n.yaml", device='gpu')  # Se crear un nuevo modelo con Yolo nano

# Use the model
model.train(data="config.yaml", epochs=5)  # Se entrena el modelo por 3 ciclos