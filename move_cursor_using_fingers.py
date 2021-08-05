import math

import cv2
import pyautogui
from mediapipe.python.solutions import hands as mediapipe_hands

# That's the things you wanna change VVVVV

MINIMUM_DISTANCE_BETWEEN_FINGERS = 0.05
CURSOR_MOVEMENT_MULTIPLIER = 1

# ----------------------------------------


screen_width, screen_height = pyautogui.size()

pyautogui.FAILSAFE = False


def get_distance_between_two_points(first_point, second_point):
    return math.sqrt(
        (first_point.x - second_point.x) ** 2
        +
        (first_point.y - second_point.y) ** 2
    )


def check_distance(first_finger, second_finger):
    return (
        get_distance_between_two_points(first_finger, second_finger)
        < MINIMUM_DISTANCE_BETWEEN_FINGERS
    )


old_finger_coords = None
last_event_was_mouse_down = True

video_capture = cv2.VideoCapture(0)
with mediapipe_hands.Hands(max_num_hands=1) as hands_recognition_object:
    while video_capture.isOpened():
        frame_capturing_was_successful, frame = video_capture.read()
        if not frame_capturing_was_successful:
            continue
        frame.flags.writeable = False
        # noinspection PyUnresolvedReferences
        # for .multi_hand_landmarks
        fingers_info = (
            hands_recognition_object.process(frame).multi_hand_landmarks
        )
        if fingers_info:
            fingers_info = fingers_info[0].landmark  # First and only hand
            thumb_tip, index_finger_tip, middle_finger_tip = (
                fingers_info[4], fingers_info[8], fingers_info[12]
            )
            if check_distance(thumb_tip, index_finger_tip):
                if not old_finger_coords:
                    old_finger_coords = thumb_tip
                coords_to_move = (
                    int(
                        screen_width * (old_finger_coords.x - thumb_tip.x)
                        * CURSOR_MOVEMENT_MULTIPLIER
                    ),
                    int(
                        screen_height * (thumb_tip.y - old_finger_coords.y)
                        * CURSOR_MOVEMENT_MULTIPLIER
                    )
                )
                old_finger_coords = thumb_tip
                pyautogui.move(coords_to_move)
            else:
                old_finger_coords = None
            if check_distance(thumb_tip, middle_finger_tip):
                last_event_was_mouse_down = True
                pyautogui.mouseDown()
            elif last_event_was_mouse_down:
                last_event_was_mouse_down = False
                pyautogui.mouseUp()
