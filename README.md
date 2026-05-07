#  AI Smart Traffic Control System 

An AI-powered real-time traffic management system built using **YOLOv8**, **FastAPI**, **OpenCV**, and **WebSockets** to optimize traffic flow and intelligently manage traffic signals based on live vehicle detection.

---

#  Project Overview

The AI Smart Traffic Control System analyzes live traffic video feeds from multiple cameras and dynamically controls traffic signals based on vehicle density and emergency vehicle detection. The system uses Computer Vision and Artificial Intelligence to improve road efficiency, reduce congestion, and prioritize emergency vehicles in real time.

---

#  Features

-  Real-time vehicle detection using YOLOv8
-  Emergency vehicle prioritization
-  Intelligent traffic signal management
-  Multi-camera live monitoring
-  Real-time frontend updates using WebSockets
-  Vehicle counting and ETA estimation
-  Modern cyberpunk-style dashboard UI
-  Automatic signal switching system
-  Live system logs

---

#  Tech Stack

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

#  Project Structure

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

#  Installation

## 1️ Clone Repository

```bash
git clone https://github.com/Sufiyan-2003/AI-Based-Traffic-Control-System-Prioritizing-the-emergency-vehicles-.github.io
```

---

## 2️ Open Project

```bash
cd Traffic-video-control
```

---

## 3️ Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

## 4️ Install Dependencies

```bash
pip install -r requirements.txt
```

---

#  Running the Project

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

#  How It Works

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

# Emergency Vehicle Priority

When an emergency vehicle is detected:
- The corresponding lane signal turns GREEN
- Other lanes turn RED
- Signal timer updates instantly
- Emergency alert is displayed on dashboard

---

#  Screenshots

## Dashboard UI
<img width="1919" height="875" alt="image" src="https://github.com/user-attachments/assets/dbb402d9-531c-4a1c-888e-2ca76e837514" />


## Vehicle Detection
<img width="1914" height="868" alt="image" src="https://github.com/user-attachments/assets/6f9ea726-3ea4-41dc-8356-5af047005ab3" />


---

#  Future Improvements

- AI-based adaptive timing
- Real CCTV integration
- Number plate recognition
- Traffic analytics dashboard
- Cloud deployment
- Mobile app integration

---

# Team Project

Developed as a collaborative AI + Computer Vision based smart city project.

---

#  License

This project is developed for educational and research purposes.

---

#  Support

If you like this project:
- Star the repository 
- Fork the project 
- Share with others 

#  Research Papers & References

This project is inspired by and developed with reference to the following research papers and intelligent traffic management studies:

---

# Paper 1 - Intelligent VANET-based Traffic Signal Control System

## Title
Intelligent VANET-based Traffic Signal Control System for Emergency Vehicle Prioritization and Improved Traffic Management

## Overview
This research paper presents an intelligent traffic signal control system designed for emergency vehicle prioritization using VANET (Vehicular Ad-hoc Networks) and Vehicle-to-Infrastructure (V2I) communication.

The system dynamically adjusts traffic signals in real time to reduce emergency vehicle delays and improve overall traffic efficiency in urban environments.

## Key Concepts
- Emergency Vehicle Prioritization
- Intelligent Traffic Signal Control
- VANET Communication
- V2I Communication
- Smart Traffic Management
- Adaptive Signal Timing
- Traffic Optimization

## Technologies & Methods
- Vehicular Ad-hoc Networks (VANET)
- Vehicle-to-Infrastructure Communication (V2I)
- Adaptive Traffic Algorithms
- Traffic Simulation
- ETA-based Signal Control

## Relevance to Our Project
This paper is highly relevant to our AI-Based Smart Traffic Control System because it focuses on:
- Real-time emergency vehicle prioritization
- Dynamic traffic signal management
- Intelligent transportation systems
- Smart city traffic optimization

The methodologies discussed in this paper helped us understand adaptive traffic signal systems and emergency vehicle handling mechanisms.

## Key Contributions of the Paper
- Real-time emergency vehicle detection and prioritization
- Adaptive traffic signal control
- Reduced emergency vehicle travel time
- Improved urban traffic efficiency
- Smart transportation framework

## Summary
The paper proposes a smart traffic management framework using VANET and adaptive traffic control strategies to minimize emergency vehicle delays and improve traffic flow in urban road networks.

## Paper Link
https://www.sciencedirect.com/science/article/pii/S1110866525000933

## Authors
Pijush Bairi, Sujata Swain, Anjan Bandyopadhyay, Khursheed Aurangzeb, Musaed Alhussein, Saurav Mallik

## Journal
Egyptian Informatics Journal (2025)


# Paper 2 - Machine Learning Approaches to Traffic Signal Control

## Title
Adaptability and Sustainability of Machine Learning Approaches to Traffic Signal Control

## Overview
This research paper explores machine learning and reinforcement learning approaches for adaptive traffic signal control in smart city environments.

The paper focuses on improving traffic efficiency, reducing congestion, minimizing emissions, and creating sustainable urban traffic management systems.

## Key Concepts
- Machine Learning
- Reinforcement Learning
- Adaptive Traffic Signal Control
- Smart City Transportation
- Sustainable Traffic Systems
- Traffic Optimization
- Deep Q Learning

## Technologies & Methods
- Reinforcement Learning (RL)
- Deep Q Networks (DQN)
- GuidedLight Agent
- Pressure-based Traffic Optimization
- Adaptive Signal Control
- Smart Traffic Decision Systems

## Relevance to Our Project
This paper is highly relevant to our AI-Based Smart Traffic Control System because it focuses on:
- Intelligent traffic signal optimization
- Adaptive traffic management
- AI-based traffic decision making
- Real-time traffic analysis

The concepts from this paper helped us understand how AI and machine learning can dynamically control traffic signals efficiently.

## Key Contributions of the Paper
- Reinforcement Learning-based traffic optimization
- Adaptive signal control methods
- Reduced congestion and travel time
- Sustainable traffic management
- Smart city traffic infrastructure

## Summary
The paper proposes intelligent machine learning-based traffic control systems capable of adapting to different traffic conditions and optimizing urban transportation efficiency.

## Paper Link
https://www.nature.com/articles/s41598-022-21125-3

## Author
Marcin Korecki

## Journal
Scientific Reports (Nature, 2022)

# Paper 3 - AI-Based Smart Traffic Control System for Emergency Vehicle Prioritization

## Title
AI-Based Smart Traffic Control System For Emergency Vehicle Prioritization

## Overview
This paper presents an AI-driven smart traffic control system that uses YOLOv8 and computer vision techniques to detect ambulances in real time and dynamically control traffic signals.

The system prioritizes emergency vehicles by automatically switching traffic lights to green when an ambulance is detected.

## Key Concepts
- Emergency Vehicle Prioritization
- Ambulance Detection
- Computer Vision
- YOLOv8
- Deep Learning
- Smart Traffic Control
- Real-time Video Processing

## Technologies & Methods
- YOLOv8
- OpenCV
- Python
- Deep Learning
- Computer Vision
- Real-time Traffic Analysis
- Adaptive Signal Control

## Relevance to Our Project
This paper is directly related to our project because it implements:
- Real-time ambulance detection
- YOLOv8-based object detection
- Dynamic traffic signal switching
- AI-powered emergency traffic management

This paper closely matches the architecture and workflow of our implemented system.

## Key Contributions of the Paper
- Real-time ambulance detection
- Adaptive traffic signal control
- Reduced emergency response delay
- AI-based smart transportation system
- Automated emergency traffic management

## Summary
The paper proposes a real-time AI-based traffic management system that uses YOLOv8 and computer vision to detect ambulances and prioritize emergency vehicles through intelligent traffic signal control.

## Paper Link
https://ijsart.com/public/storage/paper/pdf_2/IJSARTV12I3104634.pdf

## Author
Aishwarya

## Journal
IJSART - International Journal for Science and Advanced Research in Technology (2026)

# Research Contribution

The implementation of this project combines:
- YOLOv8-based vehicle detection
- Real-time video processing
- Intelligent traffic signal switching
- Emergency vehicle prioritization
- AI-based traffic monitoring concepts

These research works provided valuable insights into building scalable and efficient smart traffic management systems for future smart cities.
