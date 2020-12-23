import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    font = cv2.FONT_HERSHEY_SIMPLEX
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]  # region of interest
        roi_color = img[y:y + h, x:x + w]
        cv2.imshow('roi_face_gray', roi_gray)
        eyes = eye_cascade.detectMultiScale(roi_gray)
        if len(eyes) >= 2:
            (ex, ey, ew, eh) = eyes[0]
            cv2.rectangle(img, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (0, 255, 0), 2)
            roi_gray_eye1 = gray[y + ey:y + ey + eh, x + ex:x + ex + ew]
            roi_color_eye1 = img[y + ey:y + ey + eh, x + ex:x + ex + ew]
            cv2.putText(img, 'left eye', (x + ex, y + ey), font, 0.6, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.imshow('roi_gray_eye1', roi_gray_eye1)

            (ex, ey, ew, eh) = eyes[1]
            cv2.rectangle(img, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (0, 255, 0), 2)
            roi_gray_eye2 = gray[y + ey:y + ey + eh, x + ex:x + ex + ew]
            roi_color_eye2 = img[y + ey:y + ey + eh, x + ex:x + ex + ew]
            cv2.putText(img, 'right eye', (x + ex, y + ey), font, 0.6, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.imshow('roi_gray_eye2', roi_gray_eye2)

        cv2.putText(img, 'eyes: ' + str(len(eyes)), (x, y+w-2), font, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('main_frame', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
