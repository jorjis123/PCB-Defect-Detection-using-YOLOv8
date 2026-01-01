from ultralytics import YOLO
import sys

model = YOLO("best.pt")

image_path = sys.argv[1]
results = model.predict(source=image_path, conf=0.3)

for r in results:
    r.show()
