# Ova-sense

Ova-sense is a simulated chip-based cancer detection model designed to identify biomarkers from medical images using a Convolutional Neural Network (CNN).

## **Model Overview**
- **Input:** Synthetic chip images (6 radial biomarker petals, 500x500px) and real ovarian ultrasound images (224x224px).
- **Architecture:** Custom CNN for chip-based biomarker detection + ResNet18 for ultrasound classification, combined via multimodal ensemble.
- **Output:** Probability score for cancer presence from each modality, averaged into a final diagnosis.

## **Setup**
Clone the repository:  
```bash
git clone https://github.com/SoumilB7/Ova-sense.git
```

## **Roles**
- Data preparation (Chip) : `dataprep_chip.ipynb`
- Model training (Chip) : `train_chip.ipynb`
- Model training (Ultrasound) : `train_us.ipynb`
- Multimodal ensemble : `ensemble.ipynb`
- Shared model definitions : `models.py`
- [Chip Dataset](https://huggingface.co/datasets/SoumilB7/Ova-sense) :
    - `dataset/CustomChip/pre` : Pre menopause biomarker levels chip reading
    - `dataset/CustomChip/post` : Post menopause biomarker levels chip reading
- [Ultrasound Dataset](https://www.kaggle.com/datasets/orvile/mmotu-ovarian-ultrasound-images-dataset) :
    - `dataset/KaggleUltrasound/images` : 1,469 real ovarian ultrasound images (MMOTU)
    - See `dataset/KaggleUltrasound/__REFERENCE__.txt` for full citation

## **Visualization**
- Use `visualization_chip.ipynb` to visualize biomarker activity and custom CNN feature maps.
- Use `visualization_us.ipynb` to visualize ResNet18 residual learning on ultrasound images.

##### **Peek into the chip v1**:
<p align="center">
  <img src="ver1/image_v1.png" alt="Overview 1" width="210"/>
  <img src="ver1/chip_v1.png" alt="Overview 2" width="170"/>
</p>

##### **Peek into the chip v2**:
<p align="center">
  <img src="example/chip_image_v2.png" alt="Overview 1" width="210"/>
  <img src="chip_v2.png" alt="Overview 2" width="210"/>
</p>


## Model
- `model_archives/CustomChip/` has both pre and post menopause chip CNN models
- `model_archives/KaggleUltrasound/` has the continual-trained ResNet18 ultrasound model
- additionally stored at : [HuggingFace](https://huggingface.co/SoumilB7/Ova-sense)

## **License**
This project is licensed under the terms written in the `LICENSE.txt` file.
