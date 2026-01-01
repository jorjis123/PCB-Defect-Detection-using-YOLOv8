from ultralytics import YOLO

model = YOLO("yolov8m.pt")

model.train(
    data="data/data.yaml",
    epochs=50,
    imgsz=640,
    batch=16
)
