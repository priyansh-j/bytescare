Problem Statement 12

Subject: Text Processing

Problem Statement: Given a text file, find if any URL is present in the text file or not, if present extract first occurrence.
Ans: code in link_from_text file
explanation:
step1: I import re(regular expression ) module.
step2: taking input for the location of text file from the user.
step3:open the file in read mode using "with open function" and read the content of the file.
step4: then i use regular expression to check if there is a url present in the given text file.
step5:then i use a list(url_matches) that store all url that are present in the text.
step6:if the length of list(url_matches) is greater than 0 it will print number of urls and first occurences of url else return 0;

-----------------------------------------------------------------------
problem statement 15
Subject: Image Processing

Problem Statement: Write a program to compare two images and find the difference between them.
Ans:
code in image_processing.py file.

explanation:
step 1: I use open cv liberary for the above problem.
step2 : taking input of image file in jpg/jpeg format from the using in img1_path and img2_path and created a (compare_images)function that showing the difference between the images using open cv library to read and process the image.
step2: In compare_image function first load both the images and resize both the image with the same shape and ensure both the images having same dimensions.Having same dimensions make easy to compare both images.
step3: In compare_image function i use cv2.cvtColor() function that use to convert both the images into grayscale because the grayscale image has only one channel, making it easier to compute the absolute difference between the images.
step4: In compare_image function The absolute difference between the grayscale images is computed using the cv2.absdiff() function. This creates an image where each pixel is the absolute difference between the corresponding pixels in the two input images.
step5: Finally, the percentage difference is calculated by summing up all the pixel values in the difference image and dividing by the total number of pixels in the image. This value is returned by the compare_images() function.


