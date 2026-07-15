import mediapipe as mp
import cv2
import time

from directkeys import right_pressed, left_pressed
from directkeys import PressKey, ReleaseKey

break_key_pressed = left_pressed
accelerator_key_pressed = right_pressed

time.sleep(2.0)

mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands

tipIds = [4, 8, 12, 16, 20]

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Camera settings
video.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
video.set(cv2.CAP_PROP_FPS, 60)
video.set(cv2.CAP_PROP_BUFFERSIZE, 1)

video.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

# Autofocus
video.set(cv2.CAP_PROP_AUTOFOCUS, 1)

# Create small window
cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Frame", 320, 240)
cv2.moveWindow("Frame", 10, 10)

with mp_hand.Hands(
    static_image_mode=False,
    max_num_hands=1,
    model_complexity=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.7
) as hands:
    previous_time = 0
    while True:

        ret, image = video.read()
        
        current_time = time.time()
        time_difference = current_time - previous_time
        fps = 1 / max(time_difference, 1e-6)
        previous_time = current_time
        cv2.putText(
    image,
    f"FPS: {int(fps)}",
    (10, 30),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.7,
    (0, 255, 255),
    2)
        
        if not ret:
            break

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        results = hands.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        lmList = []

        if results.multi_hand_landmarks:

            hand_landmarks = results.multi_hand_landmarks[0]

            h, w, c = image.shape

            for id, lm in enumerate(hand_landmarks.landmark):

                cx = int(lm.x * w)
                cy = int(lm.y * h)

                lmList.append([id, cx, cy])

            mp_draw.draw_landmarks(
                image,
                hand_landmarks,
                mp_hand.HAND_CONNECTIONS
            )

        if len(lmList) != 0:

            fingers = []

            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # Other four fingers
            for i in range(1, 5):

                if lmList[tipIds[i]][2] < lmList[tipIds[i] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            total = fingers.count(1)
            cv2.putText(
    image,
    f"Fingers: {total}",
    (10, 60),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.7,
    (255, 255, 0),
    2)

            if total == 0:

                cv2.rectangle(
                    image,
                    (20, 150),
                    (300, 230),
                    (0, 255, 0),
                    cv2.FILLED
                )

                cv2.putText(
                    image,
                    "BRAKE",
                    (25, 205),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.3,
                    (255, 0, 0),
                    3
                )

                PressKey(break_key_pressed)
                ReleaseKey(accelerator_key_pressed)

            elif total == 5:

                cv2.rectangle(
                    image,
                    (20, 150),
                    (300, 230),
                    (0, 255, 0),
                    cv2.FILLED
                )

                cv2.putText(
                    image,
                    "GAS",
                    (85, 205),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.3,
                    (255, 0, 0),
                    3
                )

                PressKey(accelerator_key_pressed)
                ReleaseKey(break_key_pressed)

            else:

                ReleaseKey(break_key_pressed)
                ReleaseKey(accelerator_key_pressed)

        # Show frame
        cv2.imshow("Frame", image)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

video.release()
cv2.destroyAllWindows()