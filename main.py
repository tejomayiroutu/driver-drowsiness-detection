import cv2
import mediapipe as mp
import math
from playsound import playsound
import threading

# Initialize MediaPipe
mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(
    refine_landmarks=True,
    max_num_faces=1
)

# Webcam
cap = cv2.VideoCapture(0)

# Eye landmark indices
LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

# Drowsiness variables
closed_frames = 0
THRESHOLD = 0.23
FRAME_LIMIT = 15

alarm_on = False


def distance(p1, p2):
    return math.sqrt(
        (p1.x - p2.x) ** 2 +
        (p1.y - p2.y) ** 2
    )


def calculate_ear(landmarks, eye):

    p1 = landmarks[eye[0]]
    p2 = landmarks[eye[1]]
    p3 = landmarks[eye[2]]
    p4 = landmarks[eye[3]]
    p5 = landmarks[eye[4]]
    p6 = landmarks[eye[5]]

    vertical1 = distance(p2, p6)
    vertical2 = distance(p3, p5)
    horizontal = distance(p1, p4)

    ear = (vertical1 + vertical2) / (2.0 * horizontal)

    return ear


def play_alarm():

    global alarm_on

    playsound("alarm.mp3")

    alarm_on = False


while True:

    success, frame = cap.read()

    if not success:
        break

    # Flip frame
    frame = cv2.flip(frame, 1)

    # Convert to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process frame
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:

        for face_landmarks in results.multi_face_landmarks:

            landmarks = face_landmarks.landmark

            # Calculate EAR
            left_ear = calculate_ear(landmarks, LEFT_EYE)
            right_ear = calculate_ear(landmarks, RIGHT_EYE)

            avg_ear = (left_ear + right_ear) / 2

            # Display EAR
            cv2.putText(
                frame,
                f"EAR: {avg_ear:.2f}",
                (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            # Detect drowsiness
            if avg_ear < THRESHOLD:
                closed_frames += 1
            else:
                closed_frames = 0

            # Trigger alert
            if closed_frames > FRAME_LIMIT:

                cv2.putText(
                    frame,
                    "DROWSINESS ALERT!",
                    (70, 100),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.2,
                    (0, 0, 255),
                    3
                )

                if not alarm_on:

                    alarm_on = True

                    threading.Thread(
                        target=play_alarm,
                        daemon=True
                    ).start()

    cv2.imshow("Driver Drowsiness Detection", frame)

    # Quit with Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()