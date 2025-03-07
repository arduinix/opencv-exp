from picamera2 import Picamera2
import cv2
import os
from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
start_time = datetime.now()


images_to_capture = 10

# make the image dir if it is not there
script_dir = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(script_dir, 'images')
os.makedirs(image_dir, exist_ok=True)


# Initialize camera
picam2 = Picamera2()

# Configure still capture
config = picam2.create_still_configuration()
picam2.configure(config)

# Start camera
picam2.start()

# loop to capture n images
for x in range(0,images_to_capture):
    filename = f"image_{x}_{timestamp}.jpg"
    filepath = os.path.join(image_dir, filename)

    # Capture image to a NumPy array (directly compatible with OpenCV)
    frame = picam2.capture_array()

    # Convert RGB to BGR for OpenCV
    frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Example processing - convert to grayscale
    gray = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2GRAY)

    # Save processed image
    cv2.imwrite(filepath, gray)

    print(f"Image {filename} captured and processed.")

# Stop camera
picam2.stop()

end_time = datetime.now()
runtime = end_time - start_time

print(f"Total runtime: {runtime}")
print(f"Total images: {images_to_capture}")



# from picamzero import Camera
# import os

# home_dir = os.environ['HOME'] #set the location of your home directory
# cam = Camera()

# cam.start_preview()
# cam.take_photo(f"{home_dir}/Desktop/new_image.jpg") #save the image to your desktop
# cam.stop_preview()