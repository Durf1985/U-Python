import cv2

face_cascade = cv2.CascadeClassifier('file1.txt')

cap = cv2.VideoCapture(0)

while True:
    # Захват кадра
    ret, frame = cap.read()

    # Преобразование в оттенки серого
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Обнаружение лиц
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Рисование прямоугольника вокруг лиц
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Отображение обработанного кадра
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
