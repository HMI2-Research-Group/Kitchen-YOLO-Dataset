# Launch Label Studio
```bash
cd DIRECTORY_OF_THIS_REPOSITORY
export LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED=true
export LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT=/home/student/PycharmProjects/data_collection_scripts
give_me_conda
conda activate label_studio
label-studio start
```

## Rules
- Make sure the bounding boxes are tight around the object of interest.
- If the object of interest is not visible in the image, do not label it.