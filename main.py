import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox, YOLO
import progressbar
import sys
import os
import numpy as np

config_file = "yolov4-tiny.cfg"
weights_file = "yolov4-tiny.weights"
labels_file = "coco.names"

yolo = YOLO(weights_file, config_file, labels_file)

cap = cv2.VideoCapture(0)


def detect_object():
    while True:
        ret, frame = cap.read()
        bbox, label, conf = yolo.detect_objects(frame)
        # bbox, label, conf = cv.detect_common_objects(frame, model='yolov4-tiny')
        output_image = draw_bbox(frame, bbox, label, conf)
        #cv2.imshow('output', frame)
        try:
            if label[0] == 'person':
                print(detection_center(bbox[0])[0])
        except IndexError:
            print('No one there :(')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


# detect where the object is in the image to turn properly.
def detection_center(bbox):
    center_x = (bbox[0] + bbox[2]) / 2.0 - 0.5
    center_y = (bbox[1] + bbox[3]) / 2.0 - 0.5
    return center_x, center_y


detect_object()

cap.release()
cv2.destroyAllWindows()
