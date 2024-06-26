# This is a sample Python script.
import cv2
import os
MAX_CONTROL = 0
MIN_CONTROL = 1

def mouse_event(event, x, y, flags, param):
    global maxVal
    global minVal
    global mode

    if event == cv2.EVENT_FLAG_LBUTTON:
        if mode == MAX_CONTROL:
            mode = MIN_CONTROL
            print("mode : MIN_CONTROL")
        else:
            mode = MAX_CONTROL
            print("mode : MAX_CONTROL")
    elif event == cv2.EVENT_MOUSEWHEEL:
        if mode == MAX_CONTROL:
            maxVal += 1 if flags > 0 else -1
        else:
            minVal += 1 if flags > 0 else -1

        print("maxVal : ", maxVal)
        print("minVal : ", minVal)
        edge = cv2.Canny(param, maxVal, minVal)
        cv2.imshow("Canny", edge)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    maxVal = 0
    minVal = 0
    img = cv2.imread('imgs/img.jpg', cv2.IMREAD_COLOR)
    edge = cv2.Canny(img, maxVal, minVal)
    cv2.imshow("Canny", edge)
    cv2.setMouseCallback("Canny", mouse_event, img)
    mode = MAX_CONTROL
    cv2.waitKey(0)
    cv2.destroyAllWindows()