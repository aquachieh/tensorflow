

tf-faster-rcnn
[https://github.com/endernewton/tf-faster-rcnn/blob/master/README.md]


## 1.Clone the repository
git clone https://github.com/endernewton/tf-faster-rcnn.git

## 2.Update your -arch in setup script to match your GPU
cd tf-faster-rcnn/lib
# Change the GPU architecture (-arch) if necessary   (我沒改
vim setup.py

## 3.Build the Cython modules
# pip install Cython,easydict,opencv-python
make clean
make
cd ..


## 4.Install the Python COCO API. The code requires the API to access COCO dataset.
cd data
git clone https://github.com/pdollar/coco.git
cd coco/PythonAPI
make
cd ../../..

### ----- setup data ----- ###
## 1.Download pre-trained model
# Resnet101 for voc pre-trained on 07+12 set
./data/scripts/fetch_faster_rcnn_models.sh

## 2.Create a folder and a softlink to use the pre-trained model
NET=res101
TRAIN_IMDB=voc_2007_trainval+voc_2012_trainval
mkdir -p output/${NET}/${TRAIN_IMDB}
cd output/${NET}/${TRAIN_IMDB}
ln -s ../../../data/voc_2007_trainval+voc_2012_trainval ./default
cd ../../..

## 3.Demo for testing on custom images
# at reposistory root
#pip install matplotlib,image
GPU_ID=0
CUDA_VISIBLE_DEVICES=${GPU_ID} ./tools/demo.py




