

tf-faster-rcnn
[https://github.com/endernewton/tf-faster-rcnn/blob/master/README.md]


1.Clone the repository
```
git clone https://github.com/endernewton/tf-faster-rcnn.git
```

2.Update your -arch in setup script to match your GPU
```
cd tf-faster-rcnn/lib
# Change the GPU architecture (-arch) if necessary   (我沒改
vim setup.py
```

3.Build the Cython modules
```
# pip install Cython,easydict,opencv-python
make clean
make
cd ..
```

4.Install the Python COCO API. The code requires the API to access COCO dataset.
```
cd data
git clone https://github.com/pdollar/coco.git
cd coco/PythonAPI
make
cd ../../..
```

### ----- setup data ----- ###
1.Download pre-trained model
```
# Resnet101 for voc pre-trained on 07+12 set
./data/scripts/fetch_faster_rcnn_models.sh
```

2.Create a folder and a softlink to use the pre-trained model
```
NET=res101   #vgg16
TRAIN_IMDB=voc_2007_trainval+voc_2012_trainval
mkdir -p output/${NET}/${TRAIN_IMDB}
cd output/${NET}/${TRAIN_IMDB}
ln -s ../../../data/voc_2007_trainval+voc_2012_trainval ./default
cd ../../..
```

3.Demo for testing on custom images
```
# at reposistory root
#pip install matplotlib,image
~/tf-faster-rcnn$
GPU_ID=0
CUDA_VISIBLE_DEVICES=${GPU_ID} ./tools/demo.py
#CUDA_VISIBLE_DEVICES=${GPU_ID} ./tools/demo_for_person.py --net res101
```

4. for vgg16
```
~/tf-faster-rcnn$
GPU_ID=1
CUDA_VISIBLE_DEVICES=${GPU_ID} ./tools/demo_for_person.py --net vgg16
```
- demo_for_person.py will output a bbox.txt [filename,label,xmin,ymin,xmax,ymax]


### ----- other ----- ###
the netseting such as image size are set in ```lib/model/config.py```
```
# Scale to use during testing (can NOT list multiple scales)
# The scale is the pixel size of an image's shortest side
__C.TEST.SCALES = (1080,)  #(600,)

# Max pixel size of the longest side of a scaled input image
__C.TEST.MAX_SIZE = 1920  #1000

# Number of top scoring boxes to keep after applying NMS to RPN proposals
__C.TEST.RPN_POST_NMS_TOP_N = 600   #300

```
