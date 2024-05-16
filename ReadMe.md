Pizza detection model by Mridul Sanghavi
Made for Graymatics interview

Model result- really good accuracy in making Bounding boxes around clear pizzas. struggles a bit when faced with many instances placed together at a distance and gives false positives when brightness is low


Creating video file to display output
As you can see its detecting really obscure pizzas in bright lights but is taking a lot of time per frame. I will skip the video a bit to demonstrate different points in the video

No False positives in brightly lit scenarios.

High accuracy even through bars and grills

Dataset changes - The "pepperoni Pizza" class with a high imbalace towards the class was causing issues in recognizing pizzas as in the current video there are no pepperoni pizzas. Removimg the class instantly fixed this issue and made the model work perfectly


Model used - YoloV8 trained with a custom Dataset. 


Dataset conversion and augmentation done via Roboflow.com
link to final dataset - https://universe.roboflow.com/mridul-sanghavi/pizza-detection-oaqie/dataset/4

Model training done on Google colab - 
ipymb file present in this directory under "Training File" - "TrainYOLOV8.ipymb"
link - https://colab.research.google.com/drive/1Nh5bGPppucvwcMWtesP9I1uYSMPO5rZi?usp=sharing


Video used for testing - Final Test Video/pizza test.mp4
(a minute of pizza footage extracted from ["Frozen Pizza MEGA FACTORY: How Automation Produces TONS of Pizzas Daily"](https://www.youtube.com/watch?v=5lKsyMu6pAk&ab_channel=TheSmartFarm)) Time - 8:00 - 9:00

Problems Faced - due to some unknown issue with my nvidea drivers, Tensor isnt able to utilize GPU hence really slow frame times (700-800ms per frame)

**END OF FILE**
