import torch
import torch.nn as nn
import torchvision.models as models


# ============================================================
# Custom CNN Model (Chip / Menopause Model)
# ============================================================

class CancerDetectionCNN(nn.Module):

    def __init__(self, pix_sz=500):
        super(CancerDetectionCNN, self).__init__()

        self.pix_sz = pix_sz

        self.conv_layers = nn.Sequential(

            nn.Conv2d(3, 32, kernel_size=3, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(128, 256, kernel_size=3, padding=1),
            nn.BatchNorm2d(256),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )

        self.fc_layers = nn.Sequential(
            nn.Flatten(),
            nn.Linear(256 * (pix_sz // 16) * (pix_sz // 16), 512),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(512, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        x = self.conv_layers(x)
        x = self.fc_layers(x)
        return x


# ============================================================
# Loader Helper Functions
# ============================================================

def load_custom_model(model_path, device="cpu"):
    model = CancerDetectionCNN()
    model.load_state_dict(torch.load(model_path, map_location=device, weights_only=False))
    model.eval()
    return model


def load_resnet_model(model_path, device="cpu"):

    model = models.resnet18(pretrained=False)
    model.fc = nn.Linear(model.fc.in_features, 2)

    model.load_state_dict(
        torch.load(model_path, map_location=device, weights_only=False)
    )

    model.eval()
    return model

