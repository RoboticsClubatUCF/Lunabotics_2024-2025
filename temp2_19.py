import cv2
import time

# Initialize the camera
cap = cv2.VideoCapture(0)

# Set video parameters (adjust as needed)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 'mp4v' for .mp4 format
out = cv2.VideoWriter('sample.mp4', fourcc, 30, (640, 480))

start_time = time.time()
while time.time() - start_time < 3:  # Record for 3 seconds
    ret, frame = cap.read()
    if not ret:
        break
    out.write(frame)  # Write frame to file

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()

print("Video recorded as 'sample.mp4'")

