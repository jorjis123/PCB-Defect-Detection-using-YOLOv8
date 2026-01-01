# PCB-Defect-Detection-using-YOLOv8

This repository contains an end-to-end implementation of an automated Printed Circuit Board (PCB) defect detection system using YOLOv8. The project focuses on detecting and localizing common PCB manufacturing defects from high-resolution images using deep learning–based object detection.

The dataset is organized in YOLO format and was converted from Pascal VOC annotations. The model was trained and evaluated using YOLOv8-m on Google Colab with GPU acceleration, achieving high detection accuracy across multiple defect classes.

🔍 Detected PCB Defect Classes:

Open Circuit

Short

Mouse Bite

Spur

Spurious Copper

🚀 Key Features

✅ Pascal VOC → YOLO annotation conversion pipeline

✅ Structured dataset split (train / validation)

✅ YOLOv8-m training and evaluation

✅ Performance metrics: mAP@50 ≈ 0.99, mAP@50–95 ≈ 0.65

✅ Inference on new PCB images (CPU/GPU supported)

✅ Fully reproducible training setup

🛠 Tech Stack

Python

Ultralytics YOLOv8

PyTorch

OpenCV

Google Colab

📈 Results

The trained YOLOv8-m model demonstrates strong localization and classification performance on PCB defects, with particularly high precision on common defect categories. Some visually similar defects remain challenging, providing scope for future improvement through targeted data augmentation and class-specific fine-tuning.

🔮 Future Improvements

Class-balanced augmentation for under-represented defects

Training with YOLOv8-l or YOLOv8-x

Real-time inspection pipeline integration

Industrial deployment and edge optimization

👤 Author

Syed Abrar Rafid
Electronics / Embedded / AI Engineering
📍 Malaysia



**Here are some detection results for starters**



<img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/1c78432e-3fa8-4ee7-be57-e021c730717a" />




<img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/614b22ba-6aed-4ac5-9b89-95c2bc5a2e5e" />




<img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/e67bc153-8841-4ec9-a651-22b3187e8080" />
