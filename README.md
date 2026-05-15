# Driver Drowsiness Detection System

A real-time computer vision project that detects driver drowsiness using Eye Aspect Ratio (EAR) and facial landmark tracking.

---

## Features

- Real-time webcam monitoring
- Facial landmark detection using MediaPipe
- Eye Aspect Ratio (EAR) calculation
- Drowsiness detection using consecutive frame analysis
- Audio alert system
- Real-time visual warning display

---

## Tech Stack

- Python
- OpenCV
- MediaPipe
- NumPy
- playsound

---

## Project Workflow

Webcam Feed → Face Mesh Detection → Eye Landmark Extraction → EAR Calculation → Drowsiness Detection → Audio Alert

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/driver-drowsiness-detection.git
cd driver-drowsiness-detection
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Project

```bash
python main.py
```

Press `Q` to quit.

---

## Eye Aspect Ratio (EAR)

The system uses Eye Aspect Ratio to determine whether the eyes are closed.

Low EAR over consecutive frames indicates drowsiness.

---

## Future Improvements

- Yawning detection
- CNN-based classification
- Fatigue scoring
- Dashboard analytics
- Browser-based deployment

---

## Author

Your Name
