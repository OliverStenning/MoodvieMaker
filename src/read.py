from PIL import Image
import cv2

# Sauce: https://learnopencv.com/reading-and-writing-videos-using-opencv/#read-video-from-file
def read_frames(video_path, limit):
    name = video_path.split("/").pop()

    video = cv2.VideoCapture(video_path)
    time = 0

    if video.isOpened() is False:
        raise Exception("Error opening the video file")

    stats = {
        "width": video.get(cv2.CAP_PROP_FRAME_WIDTH),
        "height": video.get(cv2.CAP_PROP_FRAME_HEIGHT),
        "fps": video.get(cv2.CAP_PROP_FPS),
        "frame_count": video.get(cv2.CAP_PROP_FRAME_COUNT),
    }
    print(f"Found video {name} with stats:", stats)

    print("Reading video")
    rounded_fps = round(stats["fps"])
    frames = []

    while video.isOpened():
        ret, frame = video.read()
        if ret == False or time >= limit:
            break

        is_first_frame_of_current_second = (time % rounded_fps) == 0
        if is_first_frame_of_current_second:
            frames.append(frame)

        time += 1

    video.release()
    cv2.destroyAllWindows()

    return frames


