import cv2
from utils.speech import Speak

def ObjectDetection():
    Speak("Starting object detection...")
    # Load pre-trained model (replace with actual model path)
    net = cv2.dnn.readNet("path_to_weights", "path_to_cfg")
    classes = []
    with open("path_to_classes", "r") as f:
        classes = f.read().strip().split("\n")
    
    # Open a video stream
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Perform object detection (simplified for example)
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(net.getUnconnectedOutLayersNames())

        # Display the resulting frame
        cv2.imshow("Object Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    Speak("Object detection stopped.")
