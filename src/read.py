import os
import cv2

def read_frames(name, path):
    # Opens the Video file
    # Sauce: https://learnopencv.com/reading-and-writing-videos-using-opencv/#read-video-from-file
    video = cv2.VideoCapture(path)
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

    print("Creating folder")
    if not os.path.exists(name):
        os.makedirs(name)

    print("Reading video")
    while video.isOpened():
        ret, frame = video.read()
        if ret == False:
            break

        if time == 0:
            print("Found first frame")

        image_path = f"{name}/frame-{str(time)}.jpg"
        # cv2.imwrite(image_path, frame)
        time += 1

    print("Done!")
    video.release()
    cv2.destroyAllWindows()
