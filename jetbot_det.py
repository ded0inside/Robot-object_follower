import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox, YOLO
import numpy as np

cam = cv2.VideoCapture(0)

mean = 255.0 * np.array([0.485, 0.456, 0.406])
stdev = 255.0 * np.array([0.229, 0.224, 0.225])

config_file = "yolov4-tiny.cfg"
weights_file = "yolov4-tiny.weights"
labels_file = "coco.names"

yolo = YOLO(weights_file, config_file, labels_file)

def detection_center(bbox):
    center_x = (bbox[0] + bbox[2]) / 2.0 - 0.5
    center_y = (bbox[1] + bbox[3]) / 2.0 - 0.5
    return (center_x, center_y)

def detect_object():
    while True:
        ret, frame = cap.read()
        bbox, label, conf = yolo.detect_objects(frame)
        # bbox, label, conf = cv.detect_common_objects(frame, model='yolov4-tiny')
        output_image = draw_bbox(frame, bbox, label, conf)
        #cv2.imshow('output', frame) maybe plt.show?
        try:
            if label[0] == 'person': # follows a person
		center = detection_center(bbox[0])
        	robot.set_motors(
            		float(speed_widget.value + turn_gain_widget.value * center[0]),
            		float(speed_widget.value - turn_gain_widget.value * center[0])
        		)
        except IndexError:
            print('No one there :(')

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def detection_center(bbox):
    center_x = (bbox[0] + bbox[2]) / 2.0 - 0.5
    center_y = (bbox[1] + bbox[3]) / 2.0 - 0.5
    return center_x, center_y

cam.release()
cv2.destroAllWindows()
