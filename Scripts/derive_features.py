import mediapipe as mp
import cv2
import os
import glob

def roc(curr, prev): #rate of change a.k.a first derivitave/ acceleration
    if prev is None or prev == 0:
        return 0.0
    return ((curr - prev) / prev) * 100.0


def compute_features(xy, prev_xy, delta_time):
    if xy is None:
        return [""] * 6, prev_xy #no = no of colums so need to figure out what the new value is with the pared down dataset used for training

    x, y = xy

    if prev_xy is None:
        roc_x = roc_y = 0.0
        movement_mag = movement_mag_sec = 0.0
    else:
        roc_x = roc(x, prev_xy[0])
        roc_y = roc(y, prev_xy[1])

        dx = x - prev_xy[0]
        dy = y - prev_xy[1]

        movement_mag = math.sqrt(dx*dx + dy*dy)
        movement_mag_sec = movement_mag / delta_time

##the features graveyard - went with roc & movement magnitude
    # roc_sum = roc_x + roc_y

    # roc_sum_abs = abs(roc_sum)

    # roc_x_abs = abs(roc_x)
    # roc_y_abs = abs(roc_y)

    # roc_abs_sum = roc_x_abs + roc_y_abs 

    roc_x_sec = roc_x / delta_time
    roc_y_sec = roc_y / delta_time

    # roc_sec_sum = roc_x_sec + roc_y_sec
    
    values = [
        roc_x_sec,
        roc_y_sec,
        movement_mag_sec
    ]

    return values, (x, y)
