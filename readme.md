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
    git clone https://github.com/yourusername/FaceRecognitionAttendanceSystem.git
    cd FaceRecognitionAttendanceSystem
    ```

2. Install the required packages:
    ```bash
    pip install opencv-python opencv-python-headless numpy pandas
    ```

## Usage

1. **Database Setup**: Set up your database to store attendance logs. You can use the provided `database_setup.py` file (if included) or manually create a table to store the attendance data.

2. **Train the System**: Run the `train_model.py` file to capture images of faces for training. This will generate feature data required for recognition.

3. **Run the Attendance System**: Execute the main script:
    ```bash
    python attendance_system.py
    ```
   This script will access the camera feed and automatically recognize and mark attendance for individuals already in the database.

4. **View Attendance Records**: Use the `view_attendance.py` script to display attendance logs in the terminal or export them as a CSV file.

## Project Structure

- `train_model.py`: Script to capture images and train the recognition model.
- `attendance_system.py`: Main script to run the attendance system.
- `view_attendance.py`: Script to view or export attendance logs.
- `data/`: Contains trained face data and attendance logs.
- `models/`: Stores the trained face recognition model.
- `README.md`: Project documentation.

## Customization

- Adjust face detection parameters in `attendance_system.py` to improve recognition accuracy.
- Modify database configurations in `database_config.py` (if included) to fit your preferred setup.

## Contributing

Feel free to fork this repository, create feature branches, and submit pull requests. Contributions, suggestions, and improvements are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.