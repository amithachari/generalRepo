import cv2
import numpy as np


def gaussianblur(img):
	gaussian = cv2.cv2.GaussianBlur(img, (5,5), 0)
	return gaussian

def medianblur(img):
	median = cv2.medianBlur(img, 5)
	return median

def main():
	img = cv2.imread("gauusiannoise.jpg")
	img = cv2.resize(img, (0,0), img, 0.6, 0.6)
	median = medianblur(img)
	gaussian = gaussianblur(img)

	while True:
		#cv2.imshow("Original img", img)
		# cv2.imshow("Sobel img", sobel_img)
		# cv2.imshow("Laplace img", laplace_img)
		# cv2.imshow("Gradient on Sobel img", gradient_img)
		#cv2.imshow("Gradient on Original img", gradient_img_o)
		# cv2.imshow("Threshold on Original", threshold_img)
		cv2.imshow("Median Blur", median)
		cv2.imshow("Gaussian Blur", gaussian)

		if cv2.waitKey(1) & 0xFF == 27:
			break
	cv2.destroyAllWindows()


if __name__ == '__main__':
	main()