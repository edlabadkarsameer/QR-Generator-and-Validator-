import csv
import cv2
with open('sameersir.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    included_cols = [0]
    next(reader)  # skip first row
    gateways = []
    for row in reader:
        content = row[0]
        gateways.append(content)

print(*gateways)

a="sameersir65hh4"


vid = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
while True:

    ret, frame = vid.read()
    data, bbox, straight_qrcode = detector.detectAndDecode(frame)
    if len(data) > 0:
        print(data)

    cv2.putText(frame, data, (135,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 3)

    if data in gateways:
        cv2.putText(frame, "QR is authenticated", (130, 360), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
        print("QR is authenticated!!")
    else:
        cv2.putText(frame, "QR is not authenticated", (130, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()