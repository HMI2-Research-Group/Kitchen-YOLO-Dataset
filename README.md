# Kitchen YOLO Datset
This datset contains the Label Studio Rectangular labels for the following object classes inside respective container types:

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
- Green beans 
- Tomato Sauce 
- Corn

To train the dataset using your favorite deep neural Network/Frameworks, you can use Label Studio and export the rectangular bounding boxes in a wide variety of formats.

# Dataset Statistics
# TODO Fix these
| Class Name | Number of Images out of 211 containing the Object|
|------------|--------------------------------------------------|
| Bell Pepper | 100  
| Pasta | 100  
| Chilli | 100  
| Garlic | 100  
| Cheese | 100  
| Butter | 100  
| Mushrooms | 100  
| Peas and Carrots | 100  
| Green beans | 100  
| Tomato Sauce | 100  
| Corn | 100  


# Install and Launch Label Studio
To install label studio to work with this dataset, install label-studio in an Poetry virtual environment:

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
