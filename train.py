from ultralytics import YOLO

# Se carga el modelo
model = YOLO("yolov8n.pt")

# Use the model
model.train(data="config.yaml", epochs=150, imgsz=640, batch=16)