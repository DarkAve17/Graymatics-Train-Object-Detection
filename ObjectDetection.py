import cv2
from ultralytics import YOLO
import torch

model = YOLO("Pizza-TrainedModel/pizzav4.pt")

capture=cv2.VideoCapture(r"C:\Users\mridu\Documents\GitHub Repos\Graymatics-Train-Object-Detection\Final Test Video\pizza test.mp4")
while True:
    
    isFrame,frame = capture.read()
    if not isFrame:
        break
    
    if torch.cuda.is_available():
        print("using GPU")
        device = "cuda"
        model.to(device)  # Move the model to the GPU
        results = model(frame.to(device)) 
    
    else:
        print("using CPU")
        results = model(frame)
    
    
    for result in results:
        bboxes = result.boxes.xyxy.cpu().numpy().astype("int")
        
        for bbox in bboxes:
            (x,y,x2,y2) = bbox
            cv2.rectangle(frame,(x,y),(x2,y2),(0,255,0),2)
    
    
    #print(results)
    cv2.imshow("Video", frame)
    key = cv2.waitKey(1)
    if key==27:
        break

capture.release()
cv2.destroyAllWindows()


