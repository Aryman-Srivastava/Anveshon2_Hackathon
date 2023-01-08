import cv2

# Read the video file
capture = cv2.VideoCapture('dense_traffic.mp4')

# Set the start and end frame
start_frame = 0
end_frame = 1000

# Extract frames from the video file
for i in range(start_frame, end_frame+1):
    # Set the position of the video file to the current frame
    capture.set(cv2.CAP_PROP_POS_FRAMES, i)

    # Read the frame from the video file
    success, frame = capture.read()

    # Save the frame to an image file
    cv2.imwrite(f'Video_Frames/frame_{i}.jpg', frame)

# Close the VideoCapture object
capture.release()