import os
import cv2


DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

on = True
dataset_size = 100
j = 0
cap = cv2.VideoCapture(0)
while on:
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    print('Collecting data for class {}'.format(j))

    done = False
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'To collect press "R" or to quit press "Q"', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 1,
                    cv2.LINE_AA)
        cv2.putText(frame, f'Class Number: {j}', (20, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 1,
                    cv2.LINE_AA)

        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('r'):
            break

        elif cv2.waitKey(25) == ord('q'):
            on=False
            break

    if not on:
        break       
    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        cv2.putText(frame, f'Class Number: {j}', (20, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 1,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)

        counter += 1
    j +=1
cap.release()
cv2.destroyAllWindows()
