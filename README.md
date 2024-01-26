# Mushroom Classification

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