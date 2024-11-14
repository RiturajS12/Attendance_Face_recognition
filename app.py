import cv2
import numpy as np
import face_recognition
from datetime import datetime, timedelta
import os
import csv

attendance_records = {}
recent_faces = []
TOLERANCE = 0.45
BUFFER_DURATION = timedelta(seconds=5)

csv_file = "attendance.csv"
if not os.path.exists(csv_file):
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Timestamp"])

def record_attendance_in_csv(name, timestamp):
    with open(csv_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, timestamp])

image_folder = "images/"
known_face_encodings = []
known_face_names = []

for filename in os.listdir(image_folder):
    image_path = os.path.join(image_folder, filename)
    image = face_recognition.load_image_file(image_path)
    face_encodings = face_recognition.face_encodings(image)
    for face_encoding in face_encodings:
        known_face_encodings.append(face_encoding)
        known_face_names.append(filename.split(".")[0])

def mark_attendance(name):
    current_time = datetime.now()
    if name in attendance_records:
        last_attendance_time = attendance_records[name]
        if current_time - last_attendance_time >= timedelta(hours=2):
            attendance_records[name] = current_time
            record_attendance_in_csv(name, current_time.strftime('%Y-%m-%d %H:%M:%S'))
    else:
        attendance_records[name] = current_time
        record_attendance_in_csv(name, current_time.strftime('%Y-%m-%d %H:%M:%S'))

video_capture = cv2.VideoCapture(0)

while True:
    _, frame = video_capture.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    equalized_frame = cv2.equalizeHist(gray_frame)
    color_frame = cv2.cvtColor(equalized_frame, cv2.COLOR_GRAY2BGR)
    small_frame = cv2.resize(color_frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    
    for face_encoding, face_location in zip(face_encodings, face_locations):
        current_time = datetime.now()
        if any(np.linalg.norm(face_encoding - rec_face) < TOLERANCE for rec_face, rec_time in recent_faces if current_time - rec_time < BUFFER_DURATION):
            continue
        recent_faces.append((face_encoding, current_time))
        recent_faces = [(enc, time) for enc, time in recent_faces if current_time - time < BUFFER_DURATION]

        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, TOLERANCE)
        name = "Unknown"
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            mark_attendance(name)
        
        top, right, bottom, left = [v * 4 for v in face_location]
        if name in attendance_records:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, f"{name} - Present", (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        else:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
    
    cv2.imshow("Attendance System", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
