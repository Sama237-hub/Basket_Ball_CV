# 🏀 Basketball Shot Detection & Prediction

## 📌 Overview
This project applies **Computer Vision** and **Polynomial Regression** to detect a basketball in a video, track its trajectory, and predict whether the ball will land inside the basket or not.  

It uses:
- [OpenCV](https://opencv.org/) → for video & image processing  
- [cvzone](https://pypi.org/project/cvzone/) → for contour detection and visualization  
- [NumPy](https://numpy.org/) → for regression & math calculations  

---

## 🚀 Features
- Detects basketball using **color segmentation (HSV range)**  
- Tracks ball movement across frames in real-time  
- Fits a **parabolic equation (y = Ax² + Bx + C)** for trajectory  
- Predicts basket outcome based on intersection with hoop area  
- Live visualization with annotated frames  

---

## 📂 Project Structure
```
BasketBallProject/
│── venv/                   # Virtual environment
│── Files/
│   └── Videos/             # Folder containing basketball videos
│── main.py                 # Main project script
│── README.md               # Documentation (this file)
```

---

## ⚙️ Installation

1. **Clone the repository** (or copy project files):
   ```bash
   git clone https://github.com/yourusername/BasketBallProject.git
   cd BasketBallProject
   ```

2. **Create & activate a virtual environment (recommended):**
   ```bash
   python -m venv venv
   venv\Scripts\activate       # On Windows
   source venv/bin/activate    # On Mac/Linux
   ```

3. **Install dependencies:**
   ```bash
   pip install opencv-python cvzone numpy
   ```

---

## ▶️ Usage

1. Place your video file inside the `Files/Videos/` folder.  
2. Update the video path in `main.py`:
   ```python
   cap = cv2.VideoCapture(r"Files/Videos/vid (7).mp4")
   ```
3. Run the project:
   ```bash
   python main.py
   ```
4. Press **Q** to quit the window at any time.  

---

## 🎯 Example Output
- Ball positions → shown with green circles and connected lines  
- Predicted curve → drawn as purple points across the screen  
- Prediction result:
  - ✅ "Basket" → if trajectory passes through hoop area  
  - ❌ "No Basket" → if trajectory misses  

---

## 📌 Notes
- HSV values are adjustable for different basketball colors:
  ```python
  hsvVals = {'hmin': 8, 'smin': 96, 'vmin': 115,
             'hmax': 14, 'smax': 255, 'vmax': 255}
  ```
- If no frame is detected, program exits safely with a warning.  
- Works best on clear, well-lit videos.  

---

## 🛠️ Tech Stack
- **Language:** Python 3.x  
- **Libraries:** OpenCV, cvzone, NumPy  

---

## 👨‍💻 Author
Developed as part of a **Self-Study Basketball Vision Project**.  

📧 Contact: your.email@example.com  
🔗 GitHub: [yourusername](https://github.com/yourusername)  
