# Import the libraries
import math
import cv2
import cvzone
from cvzone.ColorModule import ColorFinder
import numpy as np

# -------------------------------------------------------------------------
# Project: Basketball Shot Detection & Prediction
# Description:
#   This script detects a basketball in a video, tracks its trajectory,
#   and predicts whether the ball will land inside the basket or not.
#   It uses OpenCV for video processing, cvzone for contour detection,
#   and polynomial regression (NumPy) to model the trajectory.
# -------------------------------------------------------------------------

# Initialize the Video
cap = cv2.VideoCapture(r"D:\Self Study\BasketBallProject\venv\Files\Videos\vid (6).mp4")

# Create the color Finder object
myColorFinder = ColorFinder(False)

# HSV values for detecting the basketball color
hsvVals = {'hmin': 8, 'smin': 96, 'vmin': 115,
           'hmax': 14, 'smax': 255, 'vmax': 255}

# Variables for storing ball positions and prediction flag
posListX, posListY = [], []
xList = [item for item in range(0, 1300)]
prediction = False

# -------------------------------------------------------------------------
# Main Processing Loop
# -------------------------------------------------------------------------
while True:
    # Grab the current frame from the video
    success, img = cap.read()

    #  Check if the frame is valid before slicing (important fix)
    if not success or img is None:
        print(" No frame received from video. Exiting...")
        break

    # Crop the frame height (take top 900 pixels)
    img = img[0:900, :]

    # ---------------------------------------------------------------------
    # Step 1: Detect the basketball color in the frame
    # ---------------------------------------------------------------------
    imgColor, mask = myColorFinder.update(img, hsvVals)

    # Step 2: Find the ball location using contours
    imgContours, contours = cvzone.findContours(img, mask, minArea=500)

    if contours:
        # Save the ball's center positions
        posListX.append(contours[0]['center'][0])
        posListY.append(contours[0]['center'][1])

    if posListX:
        # -----------------------------------------------------------------
        # Step 3: Polynomial Regression
        # y = Ax^2 + Bx + C
        # Fit curve to the tracked points
        # -----------------------------------------------------------------
        A, B, C = np.polyfit(posListX, posListY, 2)

        # Draw the detected trajectory path
        for i, (posX, posY) in enumerate(zip(posListX, posListY)):
            pos = (posX, posY)
            cv2.circle(imgContours, pos, 10, (0, 255, 0), cv2.FILLED)
            if i == 0:
                cv2.line(imgContours, pos, pos, (0, 255, 0), 5)
            else:
                cv2.line(imgContours, pos, (posListX[i - 1], posListY[i - 1]), (0, 255, 0), 5)

        # Draw predicted curve across full range of x values
        for x in xList:
            y = int(A * x ** 2 + B * x + C)
            cv2.circle(imgContours, (x, y), 2, (255, 0, 255), cv2.FILLED)

        # -----------------------------------------------------------------
        # Step 4: Prediction
        # If trajectory intersects basket area (x between 330–430, y=590)
        # -----------------------------------------------------------------
        if len(posListX) < 10:  # Use first few points only
            a, b, c = A, B, C - 590
            x = int((-b - math.sqrt(b ** 2 - (4 * a * c))) / (2 * a))
            prediction = 330 < x < 430

        # Display result on screen
        if prediction:
            cvzone.putTextRect(imgContours, "Basket", (50, 150),
                               scale=5, thickness=5, colorR=(0, 200, 0), offset=20)
        else:
            cvzone.putTextRect(imgContours, "No Basket", (50, 150),
                               scale=5, thickness=5, colorR=(0, 0, 200), offset=20)

    # ---------------------------------------------------------------------
    # Display results
    # ---------------------------------------------------------------------
    imgContours = cv2.resize(imgContours, (0, 0), None, 0.7, 0.7)
    cv2.imshow("ImageColor", imgContours)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

