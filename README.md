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
git clone https://github.com/Sufiyan-2003/AI-Based-Traffic-Control-System-Prioritizing-the-emergency-vehicles-.github.io
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
<img width="1919" height="875" alt="image" src="https://github.com/user-attachments/assets/dbb402d9-531c-4a1c-888e-2ca76e837514" />


## Vehicle Detection
<img width="1914" height="868" alt="image" src="https://github.com/user-attachments/assets/6f9ea726-3ea4-41dc-8356-5af047005ab3" />


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

# 📚 Research Papers & References

This project is inspired by and developed with reference to the following research papers and intelligent traffic management studies:

---

## 1️⃣ Real-time Traffic Monitoring System based on Deep Learning and YOLOv8

This paper explains the implementation of a real-time traffic monitoring system using YOLOv8 for vehicle detection and traffic analysis. It highlights how deep learning improves traffic surveillance accuracy and supports smart city infrastructure development. The concepts of vehicle detection, object tracking, and intelligent monitoring helped shape the AI detection pipeline used in this project. :contentReference[oaicite:0]{index=0}

🔗 Research Paper:  
https://www.researchgate.net/publication/375675748_Real-time_Traffic_Monitoring_System_based_on_Deep_Learning_and_YOLOv8

---

## 2️⃣ Intelligent Traffic Signal and Smart Transportation Research

This research focuses on intelligent traffic systems, adaptive traffic signal management, and AI-driven transportation optimization. The study inspired the dynamic traffic signal control mechanism and emergency vehicle prioritization implemented in this project. :contentReference[oaicite:1]{index=1}

🔗 Research Paper:  
https://www.sciencedirect.com/science/article/abs/pii/S1051200424002197?utm_source=chatgpt.com

---

## 3️⃣ Smart Traffic Detection and Monitoring using Computer Vision

This paper discusses smart traffic detection methods using computer vision and deep learning techniques for real-time monitoring systems. The research contributed ideas related to multi-camera traffic analysis, traffic optimization, and intelligent surveillance architecture used in this system. :contentReference[oaicite:2]{index=2}

🔗 Research Paper:  
https://jutif.if.unsoed.ac.id/index.php/jurnal/article/view/4867?utm_source=chatgpt.com

---

# 📖 Research Contribution

The implementation of this project combines:
- YOLOv8-based vehicle detection
- Real-time video processing
- Intelligent traffic signal switching
- Emergency vehicle prioritization
- AI-based traffic monitoring concepts

These research works provided valuable insights into building scalable and efficient smart traffic management systems for future smart cities.
