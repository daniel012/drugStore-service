from cv2 import ( 
    VideoCapture, 
    imshow, 
    imwrite, 
    waitKey, 
    destroyWindow, 
    COLOR_BGR2GRAY, 
    cvtColor, 
    threshold, 
    THRESH_OTSU, 
    THRESH_BINARY_INV,
    getStructuringElement,
    MORPH_RECT,
    dilate,
    findContours,
    RETR_EXTERNAL,
    CHAIN_APPROX_NONE,
    boundingRect,
    rectangle,
    imread
)

from pytesseract import ( 
    pytesseract, 
    image_to_string 
)
  
# cam_port = 0
# cam = VideoCapture(cam_port)

# result, image = cam.read()
image = imread('/Users/fredpulido/Downloads/test.jpeg')
  

# if result:
  
    # set configurations
config = ('-l eng --oem 1 --psm 3')
    # Convert the image to gray scale 
gray = cvtColor(image, COLOR_BGR2GRAY) 
    
    # OTSU threshold performing
ret, threshimg = threshold(gray, 0, 255, THRESH_OTSU | THRESH_BINARY_INV) 

    # Specifying kernel size and structure shape.  
rect_kernel = getStructuringElement(MORPH_RECT, (18, 18)) 
    
    # Appplying dilation on the threshold image 
dilation = dilate(threshimg, rect_kernel, iterations = 1) 
    
    # getting contours 
img_contours, hierarchy = findContours(dilation, RETR_EXTERNAL,  
                                                    CHAIN_APPROX_NONE) 

pytesseract.tesseract_cmd = '/usr/local/Cellar/tesseract/5.3.0_1/bin/tesseract'

text = image_to_string(image , config=config )

cd  = text.split('\n')
print(text)

    # for cnt in img_contours: 
    #     x, y, w, h = boundingRect(cnt) 
        
    #     # Drawing a rectangle
    #     rect = rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2) 
        
    #     # Cropping the text block  
    #     cropped_img = image[y:y + h, x:x + w] 
        
    #     text = image_to_string(image)

    # text = text.split('\n')
    # print(text)

    # imshow("imageTest", image)
    # imwrite("imageTest.png", image)
    # waitKey(0)
    # destroyWindow("imageTest")

# else:
#     print("No image detected. Please! try again")