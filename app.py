# import cv2
# from ultralytics import YOLO

# model = YOLO('models\yolov11s.pt')
# print("Model loaded")

# WEBCAM = 1
# CAM_WIDTH = 1920  
# CAM_HEIGHT = 1080
# cap = cv2.VideoCapture(WEBCAM)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAM_WIDTH)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAM_HEIGHT)

# while cap.isOpened():
#     success, frame = cap.read()
#     if success:
#         results = model(frame)
#         annotated_frame = results[0].plot()
#         cv2.imshow("PPE Detector", annotated_frame)
#         if cv2.waitKey(1) & 0xFF == ord("q"):
#             break
#     else:
#         break


# cap.release()
# cv2.destroyAllWindows()

import cv2
from ultralytics import YOLO

model = YOLO('models\bestv1.pt')
print("Model loaded")

WEBCAM = 1 # use 0 for web camera or 1 for external camera
cap = cv2.VideoCapture(WEBCAM)

while cap.isOpened():
    success, frame = cap.read()
    if success:
        results = model(frame)
        annotated_frame = results[0].plot()
        cv2.imshow("PPE Detector", annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
