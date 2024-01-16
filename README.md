# Kitchen YOLO Datset
This datset contains the Label Studio Rectangular labels for the following object classes

- Tomato Sauce


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
echo $LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED
echo $LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT
export LABEL_STUDIO_DISABLE_SIGNUP_WITHOUT_LINK=true
label-studio start --username hmi2@gmail.com --password test123 
```
