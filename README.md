# Edge Detection Explorer

An interactive web application for experimenting with different edge detection algorithms using Python, Streamlit, and OpenCV.
## Project Description

This project is an interactive web application built using Python, OpenCV, and Streamlit that demonstrates how different edge detection algorithms work.
Users can upload any image, select an algorithm, and adjust parameters to see how edges are detected in real time.
The original and processed images are shown side by side for easy comparison and better understanding.
The **Sobel algorithm** detects edges by calculating image gradients in horizontal and vertical directions.
The **Laplacian algorithm** highlights regions of rapid intensity change using second-order derivatives.
The **Canny edge algorithm** is more advanced and uses Gaussian smoothing and thresholding for cleaner and more accurate edges.

---

## Setup and Installation

### 1. Clone the repository
```bash
git clone https://github.com/AimaArsad/Edge-Detection.git
cd Edge-Detection
```
### 3. Install required dependencies
```bash
pip install -r requirements.txt
```

Once dependencies are installed, start the Streamlit app with:
```bash
streamlit run edge_detection_ui.py
```
Then open the local URL shown in the terminal.

## Features

- **Image Upload**: Support for JPG, PNG, and BMP formats
- **Real-time Updates**: Instant visual feedback when adjusting parameters
- **Parameter Control**: Algorithm-specific adjustable parameters
- **Download Results**: Save processed images
- **Edge Detection Algorithms:**
  - **Sobel** – adjustable kernel size and gradient direction (X, Y, or Both)
  - **Laplacian** – adjustable kernel size
  - **Canny** – adjustable thresholds, Gaussian kernel size, and sigma
- **Parameter Adjustment UI:** Uses sliders, dropdowns, and radio buttons for easy tuning.
- **Side-by-side Display:** Original and processed images are shown side by side.
- **Clean & Responsive UI:** Designed with Streamlit for an intuitive user experience.

## Screenshots

Below are the Screenshots  of each edge detection algorithm.
Each image shows the original input (left) and the edge-detected output (right) side by side.
# Sobel filter

## Kernel size=3 : gradient direction : both x and y

<img width="975" height="448" alt="image" src="https://github.com/user-attachments/assets/f29ccf42-eb41-4e5e-8472-6d240d4d61d5" />

## Kernel size=7 : gradient direction=both x and y
<img width="975" height="449" alt="image" src="https://github.com/user-attachments/assets/8e8c2c80-2a66-4b23-b76e-ab8cb863fd3e" />

## Kernel size=3    gradient direction: x
<img width="975" height="458" alt="image" src="https://github.com/user-attachments/assets/520857f9-c45a-41ab-9a4d-4d2057cad30e" />

## kernel size=1       Gradient direction=y   
<img width="975" height="385" alt="image" src="https://github.com/user-attachments/assets/dd916c69-38f6-4481-b241-770d3f47bc63" />


 <img width="975" height="365" alt="image" src="https://github.com/user-attachments/assets/9e412eb0-3804-43eb-94a8-15241422122a" />

# Laplacian   

## Kernel =3

<img width="975" height="389" alt="image" src="https://github.com/user-attachments/assets/7aaca1d2-a71d-4664-8f9f-d1818e27f12f" />

## Kernel=7
 
<img width="975" height="316" alt="image" src="https://github.com/user-attachments/assets/299db2cc-3a03-4b51-bdd8-4f334aff2c81" />



# Canny Edge Detector	

## Thresholds[50,150]   kernel=3  Sigma=1.0

<img width="975" height="417" alt="image" src="https://github.com/user-attachments/assets/d7aa6a95-1e50-477f-a48a-a71e971ff7c4" />

<img width="1013" height="371" alt="image" src="https://github.com/user-attachments/assets/e1a4fec2-be91-4715-96ba-8c37a7807e4e" />

## Threshold=[46,151]       Kernel size=5       Sigma=0.70

<img width="975" height="326" alt="image" src="https://github.com/user-attachments/assets/f8f9f730-b637-4d5a-9372-8736a8cc29e4" />

<img width="975" height="423" alt="image" src="https://github.com/user-attachments/assets/853829c6-39c0-4bda-9af5-1cfeee11a5bd" />

## Threshold=[0,107]    Kernel=3    Sigma= 2.40

<img width="975" height="332" alt="image" src="https://github.com/user-attachments/assets/12053878-ef4b-401e-9f90-ac380d12bcc6" />
<img width="975" height="403" alt="image" src="https://github.com/user-attachments/assets/23c224ea-968f-4417-93c4-27ee90883228" />


### The Canny edge detector  has three main parameters.

The Three Key Parameters & How to Adjust Them
# 1. Thresholds (Low & High)
The Canny algorithm uses two thresholds to identify "strong" and "weak" edges.
- **High Threshold:** Used to find strong, definite edges. Any gradient value above this is considered a strong edge.
- **Low Threshold:** Used to find potential edges. Any gradient value below this is discarded. Values between the low and high thresholds are only considered edges if they are connected to a strong edge.

**How to find the best values:**
Start with the Default (50, 150): This is a good starting point for a 2:1 or 3:1 ratio.
If you see too many broken edges (edges are dotted lines):
The High Threshold is too high. Lower it (e.g., from 150 to 100) to be more sensitive and include more strong edges.
If you see too much noise (lots of irrelevant edges and "fuzz"):
The Low Threshold is too low. Increase it (e.g., from 50 to 80) to be more selective and ignore minor gradients.
Alternatively, the High Threshold might be too low. Increase it to be more strict about what constitutes a "strong" edge.
--**General Rule of Thumb:** A good starting ratio is often 1:2 or 1:3 (Low:High). So if you set Low to 50, High should be around 100-150.

# 2. Gaussian Kernel Size
This controls the amount of blur applied to the image before edge detection. Blurring reduces noise and details, which can result in cleaner edges.
**Small Kernel (e.g., 3):** Applies less blur. Preserves more detail but is more sensitive to noise. Use this for very clean images or when you need fine details.
**Large Kernel (e.g., 5, 7):** Applies more blur. Smoothes out noise and finer textures, resulting in thicker, more prominent edges. Use this for noisy images or when you only care about the main, large edges.

**How to find the best value:**
If your edges look too "noisy" or jagged, increase the Kernel Size (e.g., from 3 to 5).
If your edges are too thick and you are losing important details, decrease the Kernel Size (e.g., from 5 to 3).

# Recommended Step-by-Step Workflow
Follow these steps to dial in the perfect settings for your specific image:
Set Gaussian Kernel Size First: Start with a medium value like 5. This gives a good balance of noise reduction and detail.
Adjust the High Threshold: Move the High Threshold slider up and down until the main, most obvious edges in your image are clear and continuous. Ignore noise for now.
Adjust the Low Threshold: Now, adjust the Low Threshold. Set it to about 1/2 or 1/3 of the High Threshold value. Fine-tune it until the weaker, but still important, edges connect to the strong ones without introducing too much noise from the background.
Fine-tune the Kernel: Go back and check if a slightly larger or smaller kernel improves the result.

# The Relationship Between Kernel Size and Sigma
In your interface, sigma is automatically calculated based on the kernel size you choose. The general formula is:
σ ≈ (kernel_size - 1) / 6

So for my available kernel sizes:
Kernel Size 3 → σ ≈ 0.33 (minimal blur, preserves fine details)
Kernel Size 5 → σ ≈ 0.67 (moderate blur, good balance)
Kernel Size 7 → σ ≈ 1.0 (significant blur, strong smoothing)

# Recommended Sigma Values for  Scenery Image
**1. For Maximum Detail Preservation (fine edges, leaves, textures)**
Kernel Size: 3 (σ ≈ 0.33)
Low Threshold: 40-60
High Threshold: 120-150
Best for: When you want to see all the fine details in vegetation, textures
**2. For Balanced Results**
Kernel Size: 5 (σ ≈ 0.67)
Low Threshold: 50-70
High Threshold: 150-180
Best for: General scenery with good edge clarity and noise reduction
**3. For Strong, Clean Outlines (major shapes only)**
Kernel Size: 7 (σ ≈ 1.0)
Low Threshold: 70-90
High Threshold: 180-210
Best for: When you only want the main contours (mountains, horizons, large objects)

**Pro Tip: Sigma's Effect on Edge Thickness**
Low σ (0.33): Thin, precise edges
Medium σ (0.67): Balanced edge thickness
High σ (1.0): Thicker, smoother edges


### Author

- **Name:** Aima Arshad 
- **Course:** Computer Vision  
- **Project:** Edge Detection Algorithms Visualization  
- **GitHub Repo:** [Interactive Edge Detection UI](https://github.com/AimaArshad/Edge-Detection)





