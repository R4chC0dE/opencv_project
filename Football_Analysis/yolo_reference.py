from ultralytics import YOLO

model = YOLO('yolov8x')
# model.to('cuda')

result = model.predict('input_video/08fd33_4.mp4', save=True)

print(result[0])
print('================')

for box in result[0].boxes:
    print(box)
