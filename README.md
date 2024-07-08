# Kitchen YOLO Dataset
This dataset contains the Label Studio Rectangular labels for the following object classes inside respective container types:

Translucent Containers:
- Bell Pepper  
- Pasta 
- Chilli 
- Garlic 
- Cheese 
- Butter 

Opaque container: 
- Mushrooms  
- Peas and Carrots 
- Green Beans 
- Tomato Sauce 
- Corn

To train the dataset using your favorite deep neural Network/Frameworks, you can use Label Studio and export the rectangular bounding boxes in a wide variety of formats.

# Dataset Statistics
|       Class      | Image Count by Class |
|:----------------:|:--------------------:|
|      Cheese      |          18          |
| Peas and Carrots |          25          |
|      Butter      |          32          |
|    Green Beans   |          34          |
|       Corn       |          48          |
|     Mushrooms    |          52          |
|      Garlic      |          56          |
|    Bell Pepper   |          57          |
|   Tomato Sauce   |          58          |
|      Chilli      |          60          |
|       Pasta      |          62          |


# Install and Launch Label Studio
To install label studio to work with this dataset, install label-studio in a Poetry virtual environment:

```bash
poetry install
```
Then subsequently activate the virtual environment.
```bash
cd DIRECTORY_OF_THIS_REPOSITORY
source .venv/bin/activate
```

```bash
export LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED=true
export LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT=$PWD
export DATA_UPLOAD_MAX_NUMBER_FILES=10000000 
export LABEL_STUDIO_DISABLE_SIGNUP_WITHOUT_LINK=true
echo $LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED
echo $LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT
label-studio start --username hmi2@gmail.com --password test123 
```

After running the label Studio server, import the images from the `my_images` folder and the annotations from `final_export` file into the label studio server. After importing the data, you can export it to whichever format you want.
