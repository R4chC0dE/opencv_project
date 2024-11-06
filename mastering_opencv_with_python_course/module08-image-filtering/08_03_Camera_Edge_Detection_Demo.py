import cv2
import time

s = 1  # Specify 1 for accessing the web camera.
source = cv2.VideoCapture(s)

# Create a window to display the video stream.
win_name = 'Filter Demo'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

PREVIEW = 0   # Preview Mode
CANNY   = 1   # Canny Edge Detector
image_filter = PREVIEW
result = None
# Used to record the time when we processed last frame.
prev_frame_time = 0
# Used to record the time at which we processed current frame.
new_frame_time = 0

while True:
    has_frame, frame = source.read()
    if not has_frame:
        break
    # Flip video frame for convenience.
    frame = cv2.flip(frame,1)
    frame = cv2.GaussianBlur(frame, (13, 13), 0)
    if image_filter == PREVIEW:
        result = frame
    elif image_filter == CANNY:
        result = cv2.Canny(frame, 50, 70)

    # Calculating the FPS.
    new_frame_time = time.time()
    fps = int(1 / (new_frame_time - prev_frame_time))
    prev_frame_time = new_frame_time

    result = cv2.putText(
        result, str(fps) + 'FPS', (200, 100),
        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    cv2.imshow(win_name, result)

    key = cv2.waitKey(1)
    if key == ord('Q') or key == ord('q') or key == 27:
        break
    elif key == ord('C') or key == ord('c'):
        image_filter = CANNY
    elif key == ord('P') or key == ord('p'):
        image_filter = PREVIEW

source.release()
cv2.destroyWindow(win_name)
