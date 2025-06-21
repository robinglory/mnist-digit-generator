import streamlit as st
import torch
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import torch.nn as nn

# Generator model (same as training)
class Generator(nn.Module):
    def __init__(self, z_dim=100, num_classes=10):
        super().__init__()
        self.label_embedding = nn.Embedding(num_classes, z_dim)
        self.model = nn.Sequential(
            nn.Linear(z_dim, 128),
            nn.ReLU(True),
            nn.Linear(128, 784),
            nn.Tanh()
        )

    def forward(self, noise, labels):
        x = noise * self.label_embedding(labels)
        return self.model(x).view(-1, 1, 28, 28)

# Load model
device = torch.device("cpu")
G = Generator()
G.load_state_dict(torch.load("mnist_generator.pth", map_location=device))
G.eval()

# Streamlit UI
st.title("Handwritten Digit Generator (0–9)")

digit = st.selectbox("Choose a digit to generate", list(range(10)))

if st.button("Generate Images"):
    z_dim = 100
    noise = torch.randn(5, z_dim)
    labels = torch.tensor([digit] * 5)
    with torch.no_grad():
        imgs = G(noise, labels).squeeze(1)

    # Plot
    fig, axs = plt.subplots(1, 5, figsize=(10, 2))
    for i in range(5):
        axs[i].imshow(imgs[i].numpy(), cmap='gray')
        axs[i].axis("off")
    st.pyplot(fig)
