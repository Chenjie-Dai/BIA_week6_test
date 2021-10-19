"""
pyEdge: a small utility to detect edges in images
"""

# Import libraries
import matplotlib.pyplot as plt
from skimage.io import imread, imsave
from skimage.feature import canny
from skimage.filters import sobel, prewitt

# TODO: these should be passed by the user
# if no output filename is passed, it should be generated automatically
input_filename = "test_images/nucleoli.png"
output_filename = "nucleoli_edges.png"

def plot_results(img, img_edges, cmap="gray"):
    """plots the results of edge detection

    Args:
        img(np.array): the original image
        img_edges(np.array):[description] the detected edges
        cmap(str,optional):[description]the colormap. Defaults to "gray".

    Returns: nothing
    """
    # Display
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10,5))
    ax[0].imshow(img, cmap=cmap)
    ax[1].imshow(img_edges, cmap=cmap)

    for a in ax:
        a.axis("off")

    plt.show()

def detect_edges(img, method="canny"):
    """Detect edges in an image
    
    Args: 
        img(np.array): the image
        method(str, optional): the edge-detecting algorithm. defaults to "canny". 
    
    Returns(np.array): the edges of the image
    """

    if method == "canny":
        return canny(img, sigma=7)
    elif method == "prewitt":
        return  prewitt(img)
    elif method == "sobel":
        return sobel (img)
    else:
        sys.exit(f"{method} is an unsupported edge-detecting method!!!")

# Read image
img = imread(input_filename)
# Detect edges
# TODO: user should choose edge detecting algorithm
# sigma 值约小，越灵敏
img_edges = detect_edges(img, "sobel")

# 使用不同cmap制图
plot_results(img, img_edges)
plot_results(img, img_edges, cmap="viridis")

# Save to file
imsave(fname=output_filename, arr=img_edges)
