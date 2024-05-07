# ViT for Pneumonia Detection
This project investigates the use of Vision Transformers (ViTs) for detecting pneumonia from chest X-ray images as an alternative to traditional Convolutional Neural Networks (CNNs). By leveraging the transformer architecture, ViTs can model long-range pixel dependencies more effectively, potentially enhancing classification performance. The goal is to improve diagnostic accuracy in pneumonia detection, especially in areas with limited medical resources.

## Code Files
### Code Files

- **`Distributing_Data.py`**
  - **Description**: This script handles the distribution of chest X-ray images into training, testing, and validation datasets. It ensures that the data is evenly split according to specified proportions and prepares the data for the modeling process.
  - **Usage**:
    ```bash
    python Distributing_Data.py
    ```

- **`Data_Analysis.ipynb`**
  - **Description**: A Jupyter notebook used for initial data analysis and preprocessing. It includes visualizing data distributions, applying transformations for data normalization, and performing augmentations to increase the robustness of the models against overfitting.
  - **Usage**:
    ```bash
    jupyter notebook Data_Analysis.ipynb
    ```

- **`Reproduction_CNN_model.ipynb`**
  - **Description**: This notebook contains the implementation of a traditional CNN model as a baseline for performance comparison. It involves the training, validation, and testing of the CNN model using the preprocessed data.
  - **Usage**:
    ```bash
    jupyter notebook Reproduction_CNN_model.ipynb
    ```

- **`ViT_Conventional_Model.ipynb`**
  - **Description**: A notebook that implements the Vision Transformer model for image classification. This includes setting up the transformer architecture, training the model on chest X-ray images, and evaluating its performance against the CNN baseline.
  - **Usage**:
    ```bash
    jupyter notebook ViT_Conventional_Model.ipynb
    ```

- **`ViT_with_Filters.ipynb`**
  - **Description**: This notebook explores enhancements to the Vision Transformer model by integrating thresholding techniques. It examines how different preprocessing methods can improve the model's ability to detect pneumonia from X-ray images, comparing these results with the conventional ViT model.
  - **Usage**:
    ```bash
    jupyter notebook ViT_with_Filters.ipynb
    ```
