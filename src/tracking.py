import cv2
import numpy as np


def __verify_position__(x, aquarium_width):
    if x < aquarium_width / 2:
        return "left"
    else:
        return "right"


def __add_circle_and_line__(frame, center_x, center_y):
    # Draw a circle around the contour
    image_with_circle = cv2.circle(
        frame, (center_x, center_y), 40, (0, 0, 255), thickness=2
    )

    x1, y1 = 640, 0
    x2, y2 = 640, 720
    return cv2.line(
        image_with_circle,
        (x1, y1),
        (x2, y2),
        (0, 255, 0),
        thickness=2,
    )


def initialize_camera():
    frameWidth = 640
    frameHeight = 480
    video_path = "assets/fish.mp4"
    cap = cv2.VideoCapture(video_path)
    # cap = cv2.VideoCapture(0)
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)
    cap.set(10, 150)
    return cap


def fish_tracking(cap):
    fish_position = "right"

    ret, frame = cap.read()

    # Convert the frame to the HSV color scale
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Set orange color range
    lower_orange = (10, 187, 120)
    upper_orange = (20, 255, 255)

    # Create a mask for orange pixels
    mask = cv2.inRange(hsv, lower_orange, upper_orange)

    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations=1)

    # Find contours in the mask
    contours, _ = cv2.findContours(erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Check if there are contours
    if contours:
        # Find the largest contour (assuming it is the fish)
        largest_contour = max(contours, key=cv2.contourArea)

        # Find the center of the contour
        moments = cv2.moments(largest_contour)
        if moments["m00"] != 0:
            center_x = int(moments["m10"] / moments["m00"])
            center_y = int(moments["m01"] / moments["m00"])

            # Check the fish position
            fish_position = __verify_position__(center_x, 1280)

            # Display the fish position in the frame
            cv2.putText(
                frame,
                f"Fish: {fish_position}",
                (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 255),
                2,
            )

            image = __add_circle_and_line__(frame, center_x, center_y)

            # Display the frame
            cv2.imshow("Aquarium", image)

    return fish_position
