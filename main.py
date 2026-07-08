from ultralytics import YOLO
import cv2

# Load model YOLO
model = YOLO("yolov8n.pt")

# Kamera laptop
cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()

    if not success:
        break

    results = model(frame)

    annotated_frame = results[0].plot()

    cv2.imshow("Deteksi Objek", annotated_frame)

    if cv2.waitKey(1) == 27:  # AKU NAK TIDORRRRRRR
        break


for r in results:
    print("Objek terdeteksi:")
    
    for box in r.boxes:
        cls = int(box.cls[0])
        nama = model.names[cls]
        print("-", nama)

        #NGEBUG DIMANA LAGI INIIIIIIII NAK TIDORRRRRRRRRR
        #MODELNYA KENAPA GA PINTERRRRRR CEK BESOK AJA YE UDH JAM 5 PAGI
cap.release()
cv2.destroyAllWindows()
