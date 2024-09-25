from ultralytics import YOLO

model = YOLO('yolov8x')

model.predict('input_video/')