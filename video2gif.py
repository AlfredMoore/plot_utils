import cv2
import numpy as np
import imageio
from pathlib import Path
from tqdm import tqdm


filepath = "/home/xmo/socialnav_xmo/SimpleScreenRecorder/skeleton_node.mp4"
outpath = "/home/xmo/socialnav_xmo/SimpleScreenRecorder/skeleton_node.gif"

def main():
    video_cap = cv2.VideoCapture(filepath)
    image_list = []

    video_fps = video_cap.get(cv2.CAP_PROP_FPS)
    video_frames = video_cap.get(cv2.CAP_PROP_FRAME_COUNT)
    print(f"Frames: {video_frames}, FPS: {video_fps}")
    # input()
    with imageio.get_writer(outpath, mode="I", fps=10, loop=0) as writer:
        for _ in tqdm(range(0,int(video_frames),5),
                    ncols=80,
                    colour="red",
                    ):
            ret, frame = video_cap.read()
            if not ret:
                break
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            writer.append_data(frame_rgb)

            cv2.imshow('video to gif', frame)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break

    video_cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()


