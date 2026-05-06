"""
detection.py — YOLOv8 vehicle detector (FINAL FIXED VERSION)
"""

from ultralytics import YOLO
import numpy as np
import torch
import cv2
import base64
from ultralytics.nn.tasks import DetectionModel

# 🔥 FIX: PyTorch 2.6 compatibility
torch.serialization.add_safe_globals([DetectionModel])
torch.set_grad_enabled(False)

# COCO classes we care about
VEHICLE_CLASSES = {
    2: "car",
    3: "motorcycle",
    5: "bus",
    7: "truck",
}

# Emergency class (if custom model used)
EMERGENCY_CLASSES = {"ambulance"}

CONFIDENCE_THRESHOLD = 0.4


# ─────────────────────────────────────────────
# 🚗 VEHICLE DETECTOR
# ─────────────────────────────────────────────
class VehicleDetector:
    def __init__(self, model_path: str = "yolov8n.pt"):
        try:
            self.model = YOLO(model_path)
            print(f"[Detector] Model loaded: {model_path}")
        except Exception as e:
            print("❌ YOLO load failed:", e)
            raise e

    def detect(self, frame) -> list:
        """
        Returns:
        [
            {
                "bbox": [x1, y1, x2, y2],
                "confidence": float,
                "class_name": str,
                "is_emergency": bool
            }
        ]
        """

        detections = []

        try:
            results = self.model(frame, verbose=False)[0]
        except Exception as e:
            print("❌ Detection error:", e)
            return []

        if results.boxes is None:
            return []

        for box in results.boxes:
            try:
                conf = float(box.conf[0])
                cls_id = int(box.cls[0])
                label = self.model.names[cls_id].lower()

                # Filter only vehicles
                if cls_id not in VEHICLE_CLASSES and label not in EMERGENCY_CLASSES:
                    continue
                if conf < CONFIDENCE_THRESHOLD:
                    continue

                x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                class_name = VEHICLE_CLASSES.get(cls_id, label)

                # 🚨 Emergency logic
                is_emergency = (
                    label in EMERGENCY_CLASSES
                    or (class_name in ["car", "truck"] and conf > 0.82)
                )

                detections.append({
                    "bbox": [x1, y1, x2, y2],
                    "confidence": round(conf, 2),
                    "class_name": class_name,
                    "is_emergency": is_emergency
                })

            except Exception as e:
                print("⚠️ Box processing error:", e)
                continue

        return detections

    # ─────────────────────────────────────────────
    # 🎨 DRAW DETECTIONS
    # ─────────────────────────────────────────────
    def draw_detections(self, frame, detections, tracker_map=None, etas=None):
        for i, det in enumerate(detections):
            x1, y1, x2, y2 = det["bbox"]
            label = det["class_name"]
            conf = det["confidence"]
            is_emergency = det["is_emergency"]

            color = (0, 255, 0) if not is_emergency else (0, 0, 255)

            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

            text = f"{label} {conf}"
            if is_emergency:
                text = "🚑 EMERGENCY"

            cv2.putText(
                frame,
                text,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                color,
                2
            )

        return frame


# ─────────────────────────────────────────────
# 📦 FRAME → BASE64 (FOR FRONTEND)
# ─────────────────────────────────────────────
def frame_to_base64(frame, quality=70):
    try:
        _, buffer = cv2.imencode(".jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
        return base64.b64encode(buffer).decode("utf-8")
    except Exception as e:
        print("❌ Frame encode error:", e)
        return ""