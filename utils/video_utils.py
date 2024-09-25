import cv2

def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    frame_rate = cap.get(cv2.CAP_PROP_FPS)  # Get the frame rate of the video
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()
    return frames, frame_rate  # Return frames and frame rate

def save_video(output_video_frames, output_video_path, frame_rate):
    if not output_video_frames:
        raise ValueError("No frames to save.")
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    height, width = output_video_frames[0].shape[:2]
    out = cv2.VideoWriter(output_video_path, fourcc, frame_rate, (width, height))
    
    for frame in output_video_frames:
        out.write(frame)
    
    out.release()
