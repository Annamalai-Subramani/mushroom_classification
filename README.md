# Mushroom Classification

# Flask Web App

https://github.com/Annamalai-Subramani/mushroom_classification/assets/131845401/630353b4-2869-4bb0-a59e-0148b089bf53

![Screenshot 2024-01-27 115156](https://github.com/Annamalai-Subramani/mushroom_classification/assets/131845401/356b1d21-861d-4d42-ab44-e7e75a97c8ff)

![Screenshot 2024-01-27 120345](https://github.com/Annamalai-Subramani/mushroom_classification/assets/131845401/62d24087-f99a-4142-9033-cadb1e808b25)

## Description about Mushrooms

**Attribute Information**: (classes: edible=e, poisonous=p)

**cap-shape**: bell=b,conical=c,convex=x,flat=f, knobbed=k,sunken=s

**cap-surface**: fibrous=f,grooves=g,scaly=y,smooth=s

**cap-color**: brown=n,buff=b,cinnamon=c,gray=g,green=r,pink=p,purple=u,red=e,white=w,yellow=y

**bruises**: bruises=t,no=f

**odor**: almond=a,anise=l,creosote=c,fishy=y,foul=f,musty=m,none=n,pungent=p,spicy=s

**gill-attachment**: attached=a,descending=d,free=f,notched=n

**gill-spacing**: close=c,crowded=w,distant=d

**gill-size**: broad=b,narrow=n

**gill-color**: black=k,brown=n,buff=b,chocolate=h,gray=g, green=r,orange=o,pink=p,purple=u,red=e,white=w,yellow=y

**stalk-shape**: enlarging=e,tapering=t

**stalk-root**: bulbous=b,club=c,cup=u,equal=e,rhizomorphs=z,rooted=r,missing=?

**stalk-surface-above-ring**: fibrous=f,scaly=y,silky=k,smooth=s

**stalk-surface-below-ring**: fibrous=f,scaly=y,silky=k,smooth=s

**stalk-color-above-ring**: brown=n,buff=b,cinnamon=c,gray=g,orange=o,pink=p,red=e,white=w,yellow=y

**stalk-color-below-ring**: brown=n,buff=b,cinnamon=c,gray=g,orange=o,pink=p,red=e,white=w,yellow=y

**veil-type**: partial=p,universal=u

**veil-color**: brown=n,orange=o,white=w,yellow=y

**ring-number**: none=n,one=o,two=t

**ring-type**: cobwebby=c,evanescent=e,flaring=f,large=l,none=n,pendant=p,sheathing=s,zone=z

**spore-print-color**: black=k,brown=n,buff=b,chocolate=h,green=r,orange=o,purple=u,white=w,yellow=y

**population**: abundant=a,clustered=c,numerous=n,scattered=s,several=v,solitary=y

**habitat**: grasses=g,leaves=l,meadows=m,paths=p,urban=u,waste=w,woods=d

# Mushroom Classification Project

## Overview

This project focuses on the classification of mushrooms based on various features. The dataset used for training and evaluation contains information about different mushroom species, including physical characteristics and edibility.

## Dataset

The dataset used for this project is sourced from [Mushroom Data](https://www.kaggle.com/uciml/mushroom-classification) on Kaggle. It includes features such as cap shape, cap color, gill size, and more.

## Requirements

- Python 3.x
- Jupyter Notebook (optional)
- Libraries: NumPy, Pandas, Scikit-learn, Matplotlib, Seaborn

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Annamalai-Subramani/mushroom-classification.git
   cd mushroom-classification

## Install dependencies:

   pip install -r requirements.txt

## Model Training
The notebook mushroom_classification.ipynb contains the code for data preprocessing, model training, and evaluation. The project uses a Random Forest classifier for mushroom classification.

## Evaluation
The model's performance is evaluated using metrics such as accuracy, precision, recall, and F1 score. The results are presented in the notebook along with visualizations to better understand the model's behavior.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

# AWS-CICD-Deployment-with-Github-Actions
## 1. Login to AWS console.
## 2. Create IAM user for deployment
#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess

## 3. Create ECR repo to store/save docker image
- Save the URI: 852566064072.dkr.ecr.ap-south-1.amazonaws.com/project

## 4. Create EC2 machine (Ubuntu)
## 5. Open EC2 and Install docker in EC2 Machine:
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

## 6. Configure EC2 as self-hosted runner:
setting>actions>runner>new self hosted runner> choose os> then run command one by one
## 7. Setup github secrets:
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = simple-app
