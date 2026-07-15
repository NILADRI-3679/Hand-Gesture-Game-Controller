\# 🎮 Hand Gesture Game Controller



This is a computer vision project where I used MediaPipe and OpenCV to control a racing game using only hand gestures.



The webcam tracks my hand in real time, counts the number of fingers, and converts specific gestures into keyboard inputs. Showing an open palm accelerates the vehicle, while making a fist applies the brake.



I built this project to get hands-on experience with computer vision, real time image processing, and gesture recognition. Along the way, I also learned how to simulate keyboard inputs in Python and optimize webcam performance for smoother detection.



\## Current Limitations



\- Finger counting can occasionally be inaccurate when fingers overlap or the hand is not clearly visible.

\- The project currently supports Windows because keyboard input is simulated using the Windows API.

\- The gesture set is intentionally simple (accelerate and brake) to keep detection reliable.



\## 🛠️ Tech Stack



\- \*\*Programming Language:\*\* Python

\- \*\*Computer Vision:\*\* OpenCV

\- \*\*Hand Tracking:\*\* MediaPipe

\- \*\*Keyboard Input Simulation:\*\* Windows API (ctypes)

\- \*\*Development Environment:\*\* Visual Studio Code





\## ⚙️ How It Works



1\. The webcam continuously captures video frames.

2\. Each frame is processed using MediaPipe Hands to detect hand landmarks.

3\. The positions of the fingertips are compared with their corresponding finger joints to determine whether each finger is open or closed.

4\. The total number of raised fingers is calculated.

5\. Based on the detected gesture:

&#x20;  - \*\*0 Fingers (Closed Fist):\*\* Brake is applied.

&#x20;  - \*\*5 Fingers (Open Palm):\*\* Accelerator is applied.

&#x20;  - \*\*Any Other Gesture:\*\* No key is pressed.

6\. The processed video is displayed along with the detected finger count and live FPS.





Webcam

&#x20;  ↓

MediaPipe

&#x20;  ↓

Hand Landmarks

&#x20;  ↓

Finger Counting

&#x20;  ↓

Gesture Detection

&#x20;  ↓

Keyboard Input

&#x20;  ↓

Game Control





\## 🚀 Installation



1\. Clone the repository:



```bash

git clone https://github.com/NILADRI-3679/Hand-Gesture-Game-Controller.git

```



2\. Navigate to the project folder:



```bash

cd Hand-Gesture-Game-Controller

```



3\. Install the required dependencies:



```bash

pip install mediapipe opencv-python

```



4\. Run the project:



```bash

python main.py

```



\## 📁 Project Structure



```

Hand-Gesture-Game-Controller/

│

├── main.py          # Main application for hand gesture detection and game control

├── directkeys.py    # Simulates keyboard inputs using the Windows API

├── README.md        # Project documentation

└── requirements.txt # Project dependencies

```



\## 🎮 Usage



| Hand Gesture | Action |

|--------------|--------|

| ✊ Closed Fist (0 Fingers) | Brake |

| 🖐️ Open Palm (5 Fingers) | Accelerate |

| ✋ Any Other Gesture | No Action |



\### Running the Project



1\. Connect a webcam.

2\. Launch the project using `python main.py`.

3\. Place your hand in front of the camera.

4\. Use an \*\*open palm\*\* to accelerate.

5\. Make a \*\*closed fist\*\* to apply the brake.

6\. Press \*\*Q\*\* to exit the application.



\## 📸 Project Demo



> \*\*Demo GIF and screenshots will be added soon.\*\*



The project detects hand gestures in real time using a webcam and converts them into keyboard inputs for controlling a racing game.



\*\*Current Features Demonstrated\*\*

\- Real-time hand tracking

\- Finger counting

\- Live FPS display

\- Gesture-based keyboard control

\- Brake and Accelerator actions



\## 💡 Challenges Faced



While developing this project, I encountered several practical challenges:



\- Finger counting occasionally became inaccurate when fingers overlapped.

\- Detection performance varied under poor lighting conditions.

\- Balancing detection accuracy and frame rate required reducing the camera resolution.

\- Simulating keyboard inputs reliably for the game required using the Windows API.







\## 🚀 Future Improvements



\- Improve finger counting accuracy using gesture classification.

\- Add support for multiple games.

\- Recognize additional hand gestures.

\- Support Linux and macOS.

\- Replace finger counting with a trained gesture recognition model.





\## 📚 Key Learnings



Through this project, I gained practical experience with:



\- Real-time computer vision pipelines

\- Hand landmark detection using MediaPipe

\- Finger counting using landmark geometry

\- Keyboard automation with the Windows API

\- Performance optimization for webcam-based applications



\## 👨‍💻 Author



\*\*Niladri Kundu\*\*



GitHub: https://github.com/NILADRI-3679





