# MNIST Handwritten Digit Generator

## Project Description
This project is a simple web application that generates images of handwritten digits (0–9) similar to the MNIST dataset.  
The app allows users to select a digit, then generates **5 different images** of that digit using a **Generative Adversarial Network (GAN)** trained from scratch on the MNIST dataset.

The model is implemented in **PyTorch** and trained on Google Colab with a T4 GPU. The web app is built with **Streamlit** and publicly deployable on Streamlit Cloud or other similar platforms.

---

## Features
- Train a GAN generator model from scratch on MNIST digits (28x28 grayscale images).
- Generate multiple (5) unique images for any digit (0–9) selected by the user.
- Simple and interactive web UI with Streamlit.
- Fully reproducible training and deployment scripts.

---

## Files
- `train_mnist_gan.py` or `.ipynb`: PyTorch training script for the GAN model.
- `mnist_generator.pth`: Trained generator model weights.
- `app.py`: Streamlit app script to run the web app.
- `requirements.txt`: Python dependencies.

---

## How to Run

### Training (Optional)
Train the GAN model on MNIST dataset using:

```bash
python train_mnist_gan.py
````

This will save the trained model as `mnist_generator.pth`.

### Running the Web App Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run app.py
```

### Deployment

The app can be deployed easily on [Streamlit Cloud](https://streamlit.io/cloud) by linking your GitHub repository.

---

## Technologies Used

* Python 3.8+
* PyTorch
* Streamlit
* Matplotlib
* Google Colab (for training)

---

## License

This project is released under the MIT License.
