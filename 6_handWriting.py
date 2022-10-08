import pywhatkit as kit
import cv2 

text = input("Write a sentence: ")
kit.text_to_handwriting(text, save_to="handWriting_python.png")
img = cv2.imread("handWriting_python.png")
cv2.imshow("hand writing", img)
cv2.waitKey(0)
cv2.destroyAllWindows()