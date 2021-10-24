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
    frames = []

    while video.isOpened():
        ret, frame = video.read()
        if ret == False or time >= limit:
            break

        if time == 0:
            print("Found first frame")

        # frames.append(opencv_image_to_pillow_image(frame))
        frames.append(frame)
        time += 1

    video.release()
    cv2.destroyAllWindows()

    return frames

# Sauce: https://stackoverflow.com/a/48602446/4752388
def opencv_image_to_pillow_image(opencv_image) -> Image:
    rgb_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(rgb_image)

    return pil_image
