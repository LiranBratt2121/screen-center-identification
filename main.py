import cv2

cap = cv2.VideoCapture(0)

detector = cv2.CascadeClassifier(r'cascades\haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()

    left_line_x = int(frame.shape[1] // 3)
    right_line_x = int(frame.shape[1] // 1.5)
    
    cv2.line(frame, (left_line_x, 0), (left_line_x, frame.shape[0]), (0, 255, 0), 2) 
    cv2.line(frame, (right_line_x, 0), (right_line_x, frame.shape[0]), (0, 255, 0), 2) 
        
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    detections = detector.detectMultiScale(gray, 1.3, 5)
    
    for detection in detections:
        x, y, w, h =  detection

        left_point = (x, y)
        right_point = (x + w, y + h)
                
        cv2.rectangle(frame, left_point, right_point, (255, 0, 0), 2)
        
        if (left_point[0] >= left_line_x):
            if (right_point[0] <= right_line_x):                
                cv2.putText(frame, 'You Are Perfect', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            else: 
                amount_to_move = right_line_x - right_point[0] 
                cv2.putText(frame, f'Move Left! {abs(amount_to_move):.2f}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
        else:
            amount_to_move = left_line_x - left_point[0] 
            cv2.putText(frame, f'Move Right! {amount_to_move:.2f}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    cv2.imshow('Frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break