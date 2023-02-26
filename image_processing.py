import cv2

def compare_images(img1_path, img2_path):
    # Load the images
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)
    
    img1 = cv2.resize(img1, (img2.shape[1], img2.shape[0]))
    # Convert the images to grayscale
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Compute the absolute difference between the images
    diff = cv2.absdiff(gray1, gray2)

    # Calculate the percentage difference
    diff_percent = (diff.sum() / (gray1.shape[0] * gray1.shape[1]))

    return diff_percent


  #taking input from the user
img1_path = input("Enter path of first image: ")
img2_path = input("Enter path of second image: ")

diff_percent = compare_images(img1_path, img2_path)
print(f'Percentage difference between img1_path and img2_path: {diff_percent:.2f}%')
