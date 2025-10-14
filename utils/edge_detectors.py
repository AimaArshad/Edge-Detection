import cv2
import numpy as np

class EdgeDetector:
    @staticmethod
    def sobel_edge_detection(image, kernel_size=3, direction='both'):
        """
        Apply Sobel edge detection
        """
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        else:
            gray = image.copy()
        
        if direction == 'x':
            sobel = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=kernel_size)
        elif direction == 'y':
            sobel = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=kernel_size)
        else:  # both
            sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=kernel_size)
            sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=kernel_size)
            sobel = cv2.magnitude(sobel_x, sobel_y)
        
        # Normalize to 0-255
        sobel = cv2.normalize(sobel, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
        return sobel
    
    @staticmethod
    def laplacian_edge_detection(image, kernel_size=3):
        """
        Apply Laplacian edge detection
        """
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        else:
            gray = image.copy()
        
        # Apply Gaussian blur to reduce noise
        blurred = cv2.GaussianBlur(gray, (3, 3), 0)
        laplacian = cv2.Laplacian(blurred, cv2.CV_64F, ksize=kernel_size)
        
        # Convert to absolute value and normalize
        laplacian_abs = cv2.convertScaleAbs(laplacian)
        return laplacian_abs
    
    @staticmethod
    def canny_edge_detection(image, low_threshold=50, high_threshold=150, kernel_size=3, sigma=1.0):
        """
        Apply Canny edge detection
        """
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        else:
            gray = image.copy()
        
        # Apply Gaussian blur
        blurred = cv2.GaussianBlur(gray, (kernel_size, kernel_size), sigma)
        
        # Apply Canny edge detection
        edges = cv2.Canny(blurred, low_threshold, high_threshold)
        return edges
    
    @staticmethod
    def resize_image(image, max_width=800):
        """
        Resize image while maintaining aspect ratio
        """
        if image.shape[1] > max_width:
            ratio = max_width / image.shape[1]
            new_height = int(image.shape[0] * ratio)
            image = cv2.resize(image, (max_width, new_height))
        return image