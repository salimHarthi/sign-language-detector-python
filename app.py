import cv2
import streamlit as st
import pickle5 as pickle
from util import get_hand_reading

model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']
filp = True
labels_dict = {}
with open('classes.txt', 'r') as file:
    for i,line in enumerate(file):
        labels_dict[i] = line.strip()
    file.close()

# Use this line to capture video from the webcam
cap = cv2.VideoCapture(0)

# Set the title for the Streamlit app
st.title("Video Capture with OpenCV")

frame_placeholder = st.empty()
# creating a placeholder for the fixed sized textbox
logtxtbox = st.empty()
old_pred = ''
full_text = ''
while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        st.write("The video capture has ended.")
        break
    if filp:
        frame = cv2.flip(frame,1)

    # You can process the frame here if needed
    # e.g., apply filters, transformations, or object detection
    prediction,x1, y1 = get_hand_reading(frame,model)  

    # Convert the frame from BGR to RGB format
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  
    if prediction!=-1:
        predicted_character = labels_dict[int(prediction)]
        cv2.putText(frame, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
                        cv2.LINE_AA)
        if old_pred != predicted_character:
            full_text+=f" {predicted_character}"
            logtxtbox.write(full_text)
            old_pred = predicted_character

    # Display the frame using Streamlit's st.image
    frame_placeholder.image(frame, channels="RGB")
    
    # Break the loop if the 'q' key is pressed or the user clicks the "Stop" button
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()