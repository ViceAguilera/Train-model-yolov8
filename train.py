from ultralytics import YOLO

# Se carga el modelo
model = YOLO("yolov8n.pt")  # Se crear un nuevo modelo con Yolo nano

# Use the model
model.train(data="config.yaml", epochs=5, imgsz=640, batch=8)  # Se entrena el modelo por 3 ciclos