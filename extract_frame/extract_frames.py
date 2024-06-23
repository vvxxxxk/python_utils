import os
import cv2

# config
input_path = os.getcwd() + '/input/'
output_path = os.getcwd() + '/output/'
filename = "test.avi"
frame_interval = 10

def extract_frames(filename, output_path):
    video = cv2.VideoCapture(filename)

    fps = video.get(cv2.CAP_PROP_FPS)

    # frame_interval = int(round(fps))
    frame_count = 0

    while True:
        success, frame = video.read()
        
        if not success:
            break
        
        # Extract frames at the desired interval
        if frame_count % frame_interval == 0:
            output_path = os.getcwd() + '/output/frame_' + str(frame_count) + '.jpg'
            cv2.imwrite(output_path, frame)
        frame_count += 1

    video.release()

extract_frames(filename, output_path)