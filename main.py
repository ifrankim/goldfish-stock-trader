from src.tracking import fish_tracking, initialize_camera
from src.companies import select_action
import cv2

if __name__ == "__main__":
    cap = initialize_camera()  # Initializes the camera

    i = 0
    tank_sides = [0, 0]
    max_iterations = 150  # Use constants instead of magic numbers
    decision_iteration = max_iterations - 1

    while i < max_iterations:
        fish_position = fish_tracking(cap)
        tank_sides[fish_position == "right"] += 1

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

        if i == decision_iteration:
            action = "right" if tank_sides[0] > tank_sides[1] else "left"
            select_action(fish_position)
            i = 0
        else:
            i += 1

    cap.release()  # Releases camera resources
    cv2.destroyAllWindows()  # Closes all OpenCV windows
