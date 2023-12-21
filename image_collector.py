"""
All the angle and coordinate axes are WRTO to the base_link of the ridgeback robot, as it can 
be visualized easily in RViz
"""
from pyrealsense2 import pyrealsense2
import numpy as np
import threading
import cv2
import glob
import os


class RealsenseQR:
    def __init__(self, device_id: str) -> None:
        self.device_id = device_id
        self.pipeline = pyrealsense2.pipeline()
        # Create a config and configure the pipeline to stream
        # different resolutions of color and depth streams
        config = pyrealsense2.config()
        config.enable_device(device_id)
        config.enable_stream(pyrealsense2.stream.depth, 640, 480, pyrealsense2.format.z16, 30)
        config.enable_stream(pyrealsense2.stream.color, 640, 480, pyrealsense2.format.bgr8, 30)
        # Align color and depth streams
        align_to = pyrealsense2.stream.color
        self.align = pyrealsense2.align(align_to)
        self.pipeline.start(config)
        # Initialize some class variables
        self.aligned_depth_image = None
        self.color_image = None
        self.depth_intrin = None
        # Run self.cam in a seperate thread
        self.cam_thread = threading.Thread(target=self.cam)
        self.cam_thread.start()

    def cam(self) -> None:
        try:
            while 1:
                # Get frameset of color and depth
                frames = self.pipeline.wait_for_frames()
                # Align the depth frame to color frame
                aligned_frames = self.align.process(frames)
                # Get aligned frames
                aligned_depth_frame = aligned_frames.get_depth_frame()  # aligned_depth_frame is a 640x480 depth image
                color_frame = aligned_frames.get_color_frame()
                # get intrinsics
                depth_intrin = aligned_depth_frame.profile.as_video_stream_profile().intrinsics
                # Assign to class variables
                self.aligned_depth_image = aligned_depth_frame
                self.color_image = np.asanyarray(color_frame.get_data())
                self.depth_intrin = depth_intrin
        except Exception as e:
            pass


def count_png_images(folder_path):
    png_files = glob.glob(os.path.join(folder_path, "*.png"))
    return len(png_files)


def main():
    # Start the camera
    realsense = RealsenseQR("128422272486")
    # find number of images in the my_images folder
    num_images = count_png_images("my_images")
    while 1:
        # Get frames
        color_frame = realsense.color_image
        if color_frame is None:
            continue
        # Show the image
        cv2.imshow("RealSense", color_frame)
        # Save the image whenever the user presses 's'
        key = cv2.waitKey(1)
        if key == ord("s"):
            cv2.imwrite(f"my_images/{num_images}.png", color_frame)
            num_images += 1


if __name__ == "__main__":
    main()
