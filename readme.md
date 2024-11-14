# Face Recognition Attendance System

This project implements a Face Recognition Attendance System using OpenCV, allowing for real-time face detection and recognition to automate attendance marking.

## Features

- **Real-time Face Detection and Recognition**: Utilizes OpenCV to detect and recognize faces from a live camera feed or saved images.
- **Attendance Tracking**: Marks attendance for recognized individuals and logs the time of recognition.
- **Database Integration**: Stores recognized faces in a database and updates attendance records.
- **Easy Enrollment**: Allows adding new faces to the system for future recognition.

## Prerequisites

- Python 3.x
- OpenCV
- NumPy
- Pandas (for data management)
- SQLite3 or any database for storing attendance logs
- Optionally, a camera for real-time recognition

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/RiturajS12/Attendance_Face_recognition.git
    cd Attendance_Face_recognition
    ```

2. Install the required packages:
    ```bash
    pip install opencv-python opencv-python-headless numpy pandas
    ```

## Project Structure

- `video cam.ipynb`: Script to capture images and train the recognition model.
- `attendance.csv`: Script to view or export attendance logs.
- `Images/`: Contains trained face data and attendance logs.
- `README.md`: Project documentation.

## Customization

- Adjust face detection parameters in `video_cam.ipynb` to improve recognition accuracy.

## Contributing

Feel free to fork this repository, create feature branches, and submit pull requests. Contributions, suggestions, and improvements are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
