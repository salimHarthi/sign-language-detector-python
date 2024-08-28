import cv2
import streamlit as st
import numpy as np



# Use this line to capture video from the webcam
cap = cv2.VideoCapture(0)


# Set the title for the Streamlit app
st.title("Video Capture with OpenCV")

frame_placeholder = st.empty()



while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        st.write("The video capture has ended.")
        break

    # You can process the frame here if needed
    # e.g., apply filters, transformations, or object detection

    # Convert the frame from BGR to RGB format
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Display the frame using Streamlit's st.image
    frame_placeholder.image(frame, channels="RGB")

    # Break the loop if the 'q' key is pressed or the user clicks the "Stop" button
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()