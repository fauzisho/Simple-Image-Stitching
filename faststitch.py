from panorama import Panaroma
import imutils
import cv2


no_of_images = 5
filename = ["card/image1.jpeg","card/image2.jpeg","card/image3.jpeg","card/image4.jpeg","card/image5.jpeg"]

images = []

for i in range(no_of_images):
    images.append(cv2.imread(filename[i]))

for i in range(no_of_images):
    images[i] = imutils.resize(images[i], width=400)

for i in range(no_of_images):
    images[i] = imutils.resize(images[i], height=400)

panaroma = Panaroma()

if no_of_images==2:
    (result, matched_points) = panaroma.image_stitch([images[0], images[1]], match_status=True)
else:
    (result, matched_points) = panaroma.image_stitch([images[no_of_images-2], images[no_of_images-1]], match_status=True)
    for i in range(no_of_images - 2):
        (result, matched_points) = panaroma.image_stitch([images[no_of_images-i-3],result], match_status=True)


crop_x_min = 300
crop_x_max = 900
crop_y_min = 30
crop_y_max = 390

crop_img = result[crop_y_min:crop_y_max,crop_x_min:crop_x_max]

cv2.imshow("Fast Keypoint Matches", matched_points)
cv2.imshow("Fast Result", result)
cv2.imshow("Crop Result", crop_img)

cv2.imwrite("Fast_Matched_points.jpg",matched_points)
cv2.imwrite("fastresult.jpg",result)
cv2.imwrite("cropresult.jpg",crop_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
