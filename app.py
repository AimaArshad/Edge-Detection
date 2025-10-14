import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io
from utils.edge_detectors import EdgeDetector

# Page configuration
st.set_page_config(
    page_title="Edge Detection Explorer",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #ff7f0e;
        margin-bottom: 1rem;
    }
    .image-container {
        border: 2px solid #ddd;
        border-radius: 10px;
        padding: 10px;
        background-color: #f9f9f9;
    }
    .stButton button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 5px;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown('<h1 class="main-header">🔍 Edge Detection Explorer</h1>', unsafe_allow_html=True)
    
    # Sidebar for controls
    with st.sidebar:
        st.markdown('<h2 class="sub-header">Controls</h2>', unsafe_allow_html=True)
        
        # File uploader
        uploaded_file = st.file_uploader(
            "📁 Upload an Image",
            type=['jpg', 'jpeg', 'png', 'bmp'],
            help="Upload an image in JPG, PNG, or BMP format"
        )
        
        # Algorithm selection
        st.markdown("### 🎯 Edge Detection Algorithm")
        algorithm = st.selectbox(
            "Select Algorithm",
            ["Sobel", "Laplacian", "Canny"],
            index=0,
            help="Choose the edge detection algorithm to apply"
        )
        
        # Real-time update toggle
        real_time = st.toggle("🔄 Real-time Updates", value=True, 
                            help="Update results automatically when parameters change")
        
        # Apply button (only show if real-time is disabled)
        apply_button = None
        if not real_time:
            apply_button = st.button("🚀 Apply Changes", type="primary")
        
        # Algorithm-specific parameters
        st.markdown("### ⚙️ Parameters")
        
        if algorithm == "Sobel":
            kernel_size = st.slider(
                "Kernel Size", 
                min_value=1, 
                max_value=7, 
                value=3, 
                step=2,
                help="Size of the Sobel kernel (must be odd)"
            )
            direction = st.radio(
                "Gradient Direction",
                ["both", "x", "y"],
                index=0,
                help="Direction of gradient to compute"
            )
            
        elif algorithm == "Laplacian":
            kernel_size = st.slider(
                "Kernel Size", 
                min_value=1, 
                max_value=7, 
                value=3, 
                step=2,
                help="Size of the Laplacian kernel (must be odd)"
            )
            
        elif algorithm == "Canny":
            col1, col2 = st.columns(2)
            with col1:
                low_threshold = st.slider(
                    "Low Threshold", 
                    min_value=0, 
                    max_value=255, 
                    value=50,
                    help="Lower threshold for hysteresis procedure"
                )
            with col2:
                high_threshold = st.slider(
                    "High Threshold", 
                    min_value=0, 
                    max_value=255, 
                    value=150,
                    help="Upper threshold for hysteresis procedure"
                )
            
            kernel_size = st.slider(
                "Gaussian Kernel Size", 
                min_value=1, 
                max_value=7, 
                value=3, 
                step=2,
                help="Size of Gaussian blur kernel (must be odd)"
            )
            
            sigma = st.slider(
                "Sigma (σ)", 
                min_value=0.1, 
                max_value=5.0, 
                value=1.0, 
                step=0.1,
                help="Standard deviation for Gaussian blur"
            )
    
    # Main content area
    if uploaded_file is not None:
        # Load and process image
        try:
            # Convert uploaded file to OpenCV format
            image = Image.open(uploaded_file)
            image_array = np.array(image)
            
            # Convert RGBA to RGB if necessary
            if image_array.shape[-1] == 4:
                image_array = cv2.cvtColor(image_array, cv2.COLOR_RGBA2RGB)
            elif len(image_array.shape) == 2:
                image_array = cv2.cvtColor(image_array, cv2.COLOR_GRAY2RGB)
            
            # Resize image for display
            original_image = EdgeDetector.resize_image(image_array)
            
            # Create two columns for input and output
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown('<h3 class="sub-header">📥 Input Image</h3>', unsafe_allow_html=True)
                st.image(original_image, use_column_width=True, 
                        caption=f"Original Image - {original_image.shape[1]}×{original_image.shape[0]}")
            
            with col2:
                st.markdown('<h3 class="sub-header">📤 Output Result</h3>', unsafe_allow_html=True)
                
                # Check if we should process the image
                process_image = real_time or apply_button
                
                if process_image:
                    try:
                        # Apply selected edge detection algorithm
                        if algorithm == "Sobel":
                            result = EdgeDetector.sobel_edge_detection(
                                original_image, kernel_size, direction
                            )
                            caption = f"Sobel Edges - Kernel: {kernel_size}, Direction: {direction}"
                            
                        elif algorithm == "Laplacian":
                            result = EdgeDetector.laplacian_edge_detection(
                                original_image, kernel_size
                            )
                            caption = f"Laplacian Edges - Kernel: {kernel_size}"
                            
                        elif algorithm == "Canny":
                            result = EdgeDetector.canny_edge_detection(
                                original_image, low_threshold, high_threshold, kernel_size, sigma
                            )
                            caption = f"Canny Edges - Thresholds: [{low_threshold}, {high_threshold}], Kernel: {kernel_size}, σ: {sigma}"
                        
                        # Display result
                        st.image(result, use_column_width=True, caption=caption)
                        
                        # Download button for processed image
                        result_pil = Image.fromarray(result)
                        buf = io.BytesIO()
                        result_pil.save(buf, format='PNG')
                        st.download_button(
                            label="💾 Download Processed Image",
                            data=buf.getvalue(),
                            file_name=f"{algorithm.lower()}_edges.png",
                            mime="image/png"
                        )
                        
                    except Exception as e:
                        st.error(f"Error processing image: {str(e)}")
                else:
                    st.info("👆 Adjust parameters and click 'Apply Changes' or enable real-time updates to see results.")
        
        except Exception as e:
            st.error(f"Error loading image: {str(e)}")
    
    else:
        # Welcome message and instructions when no image is uploaded
        st.markdown("""
        <div style='text-align: center; padding: 4rem;'>
            <h2>🎯 Welcome to Edge Detection Explorer!</h2>
            <p style='font-size: 1.2rem;'>
                Upload an image using the sidebar controls to start exploring different edge detection algorithms.
            </p>
            <div style='margin-top: 3rem;'>
                <h3>📚 Available Algorithms:</h3>
                <ul style='text-align: left; display: inline-block;'>
                    <li><strong>Sobel:</strong> Computes gradient approximations</li>
                    <li><strong>Laplacian:</strong> Uses second derivatives</li>
                    <li><strong>Canny:</strong> Multi-stage algorithm with noise reduction</li>
                </ul>
            </div>
            <div style='margin-top: 2rem;'>
                <h3>💡 Tips:</h3>
                <ul style='text-align: left; display: inline-block;'>
                    <li>Enable real-time updates for instant feedback</li>
                    <li>Experiment with different parameter values</li>
                    <li>Compare results between algorithms</li>
                    <li>Download your favorite results</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Sample images section
        st.markdown("---")
        st.markdown('<h3 class="sub-header">🖼️ Try These Sample Images</h3>', unsafe_allow_html=True)
        st.info("For best results, try images with clear contrasts and well-defined edges.")

if __name__ == "__main__":
    main()