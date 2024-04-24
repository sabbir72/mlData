# ML Datasets
ML Datasets is a repository containing links to Annotated and RAW datasets and tools for ML model training

[The Ultimate Guide to Object Detection](https://www.v7labs.com/blog/object-detection-guide)

### Datasets
- [Person_Dataset_v4.2.zip](https://drive.google.com/file/d/1SyJZcsII928SnZU4oOcWu95SFCsJtk3C/view?usp=drive_link) | [Total Data: 38.6k Full Images]
- [Activity_Dataset_v12.1.zip](https://drive.google.com/drive/folders/1d0WEYZ2YP3wKAsqh-LoRWwwofdw6ys_y?usp=drive_link) | [Total Data: 131k+ 16k = 147k Cropped Images]

# Documentation 

- [Data Annotation Guideline](https://docs.google.com/document/d/1YShg8UJSNGmzG6vygHFxAICRtil1o8GWOwUQEO_JBVc/edit)
- [Yolov5 Custom Data Training Recommendations](https://docs.google.com/document/d/1NCYRT1lvbFQ0NRyVTYcUvhZOAj-oljgfHUZbro8xDAo/edit)
- [YOLO Data Annotation Format](https://docs.google.com/document/d/13oo3pTWHUhBW-A-s7msjHWyK5S08urEEut9z8Izx4CI/edit#heading=h.jt74ufvp489v)
- [ML (YOLO) Object Detection Metrics](https://docs.google.com/document/d/1Eqyin0os9SHHEQUq__F8t81DVQiRhG3qWqe9HUSyN0I/edit?usp=sharing)
- [Data Annotation Daily Count (Nadia)](https://docs.google.com/spreadsheets/d/17AflyuI49OzVG3oQHfrGUl9vBc7VkUAAM4kqwd1Jt9k)
- [Data organization Structure.(Junior Sabbir)](https://docs.google.com/document/d/1AOfXHZ1UI7O0jad0AkbzK5C0CtT7EJ4kfffznIVvZlY/edit#heading=h.97qbiihxq8my)
- [Activity Annotation Data variation](https://docs.google.com/document/d/1BE9kGAYIoH00yMS56qMMaaOb_Q_-Dto9xBN4_Dzix2I/edit)

### Data Annotation Tool
- [Label-studio](https://github.com/HumanSignal/label-studio/)
- [Roboflow](https://github.com/roboflow/supervision)

### Training Dataset Structure
- training-data/
  - images/ *.jpg
  - labels/ *.txt
  - 
### Dataset Annotation Structure (Activity Data)
- Date/
  - FloorID_LineID_Camera_ID_PersonID/
    - images/
      - image1.jpg
      - image2.jpg
      - ...
    - labels/
      - label1.txt
      - label2.txt
      - ...
### Dataset Annotation Structure (Person Data)
- Date/
  - FloorID_LineID_Camera_ID/
    - images/
      - image1.jpg
      - image2.jpg
      - ...
    - labels/
      - label1.txt
      - label2.txt
      - ...

# Steps of Collecting Data 
- Raw video data
- Extracted image folders
- Annotated images and label data
- Dataset archives

```nohup sh -c " docker compose up -d && label-studio" >/dev/null 2>&1 &```
# mlData
