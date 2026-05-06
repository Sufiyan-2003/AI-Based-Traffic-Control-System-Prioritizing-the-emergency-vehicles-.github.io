# 🚦 AI Smart Traffic Control System

An AI-powered real-time traffic management system built using **YOLOv8**, **FastAPI**, **OpenCV**, and **WebSockets** to optimize traffic flow and intelligently manage traffic signals based on live vehicle detection.

---

# 📌 Project Overview

The AI Smart Traffic Control System analyzes live traffic video feeds from multiple cameras and dynamically controls traffic signals based on vehicle density and emergency vehicle detection. The system uses Computer Vision and Artificial Intelligence to improve road efficiency, reduce congestion, and prioritize emergency vehicles in real time.

---

# ✨ Features

- 🚗 Real-time vehicle detection using YOLOv8
- 🚑 Emergency vehicle prioritization
- 🚦 Intelligent traffic signal management
- 📹 Multi-camera live monitoring
- ⚡ Real-time frontend updates using WebSockets
- 📊 Vehicle counting and ETA estimation
- 🖥 Modern cyberpunk-style dashboard UI
- 🔄 Automatic signal switching system
- 📜 Live system logs

---

# 🛠 Tech Stack

## Frontend
- HTML5
- CSS3
- JavaScript

## Backend
- FastAPI
- Python
- WebSocket

## AI / Computer Vision
- YOLOv8
- OpenCV
- NumPy

---

# 📂 Project Structure

```bash
Traffic-video-control/
│
├── backend/
│   ├── main.py
│   ├── detection.py
│   ├── tracker.py
│   ├── eta.py
│   ├── report.py
│   └── yolov8n.pt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
│
├── videos/
│   ├── video0.mp4
│   ├── video1.mp4
│   ├── video2.mp4
│   └── video3.mp4
│
├── requirements.txt
└── README.md
```

---

# ⚙ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Traffic-video-control.git
```

---

## 2️⃣ Open Project

```bash
cd Traffic-video-control
```

---

## 3️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

## Start Backend Server

```bash
cd backend
python main.py
```

Server will run at:

```text
http://localhost:8000
```

Open in browser:

```text
http://127.0.0.1:8000
```

---

# 🧠 How It Works

1. Multiple traffic videos are processed simultaneously.
2. YOLOv8 detects vehicles in each frame.
3. Emergency vehicles are identified and prioritized.
4. Traffic signals dynamically change based on traffic conditions.
5. Live updates are sent to the frontend using WebSockets.
6. Dashboard displays:
   - Live camera feeds
   - Vehicle count
   - Signal state
   - ETA
   - Emergency alerts

---

# 🚑 Emergency Vehicle Priority

When an emergency vehicle is detected:
- The corresponding lane signal turns GREEN
- Other lanes turn RED
- Signal timer updates instantly
- Emergency alert is displayed on dashboard

---

# 📸 Screenshots

## Dashboard UI
(Add project screenshots here)

## Vehicle Detection
(Add detection screenshots here)

## Signal Control
(Add traffic signal screenshots here)

---

# 🔮 Future Improvements

- AI-based adaptive timing
- Real CCTV integration
- Number plate recognition
- Traffic analytics dashboard
- Cloud deployment
- Mobile app integration

---

# 👨‍💻 Team Project

Developed as a collaborative AI + Computer Vision based smart city project.

---

# 📄 License

This project is developed for educational and research purposes.

---

# ⭐ Support

If you like this project:
- Star the repository ⭐
- Fork the project 🍴
- Share with others 🚀