# libraries required
import os
import face_recognition
# need to pip install face_recognition,cmake first


# image database or corpus
images = os.listdir('images')

#load image that you want to recognize here
image_to_recognize = face_recognition.load_image_file('image_to_check.jpg')

# to change the image into a feature vector
encoded_image_to_recognize = face_recognition.face_encodings(image_to_recognize)[0]

for image in images:
    #load and encode the image
    current_image = face_recognition.load_image_file("images/" + image)
    encoded_current_image = face_recognition.face_encodings(current_image)[0]
    
    #use face_recognition to comapre
    comparison = face_recognition.compare_faces([encoded_image_to_recognize],encoded_current_image)
    
    if comparison[0] ==True:
        print("Matched: " + image)
            
    else:
        print("Not Matched: " + image)
    
    