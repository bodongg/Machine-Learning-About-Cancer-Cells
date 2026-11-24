# Cervical cell classification using machine learning

## Research question

How well can logistic regression and random forest distinguish five cervical cell morphologies in isolated Pap smear images when all crops from a parent cluster image stay together? The Python notebook compares them with a most-frequent-class baseline.

## Dataset and scope

SIPaKMeD is a publicly available research dataset from the University of Ioannina. Expert cytopathologists annotated isolated cervical cells that were manually cropped from microscope images of Pap smear specimens. The release contains 4,049 cell crops derived from 966 parent cluster images. The authors request that users cite their 2018 IEEE ICIP paper. [Official SIPaKMeD downloads](https://www.cs.uoi.gr/~marina/sipakmed.html) · [Original paper, Table 1](https://www.cse.uoi.gr/~cnikou/Publications/C072%20-%20Plissiti%20-%20icip%202018%20-%20Athens.pdf)

The counts below describe the Kaggle mirror used in the benchmark.

| Label | Category in the paper | Cell crops | Parent cluster images |
| --- | --- | ---: | ---: |
| Superficial/intermediate | Normal | 831 | 126 |
| Parabasal | Normal | 787 | 108 |
| Koilocytotic | Abnormal | 825 | 238 |
| Metaplastic | Benign | 793 | 271 |
| Dyskeratotic | Abnormal | 813 | 223 |
| **Total** | | **4,049** | **966** |

The two abnormal categories are nonmalignant. The label set describes cell appearance and contains no invasive cancer class. Each prediction in this study concerns an already cropped cell. [Original paper, sections 1 and 2](https://www.cse.uoi.gr/~cnikou/Publications/C072%20-%20Plissiti%20-%20icip%202018%20-%20Athens.pdf)

## Methods

1. Load the isolated cell images from the Kaggle mirror of the class archives. Use the class folders for labels and group crops by their parent cluster image within each class. Record counts by class and verify that no parent group crosses evaluation partitions. The release documents its cluster images and isolated crops separately. [Official archive description](https://www.cs.uoi.gr/~marina/SIPAKMED/Description_of_Features.pdf)
2. Use histogram of oriented gradients (HOG) features to summarize local edge directions and color statistics to describe pixel colors. Both feature sets are derived from the crops. Compare a most-frequent-class dummy classifier, a logistic regression pipeline, and a random forest. [scikit-image HOG documentation](https://scikit-image.org/docs/stable/api/skimage.feature.html#skimage.feature.hog) · [Dummy classifier](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html)
3. Reserve the first held-out fold from a five-fold stratified group split. Use four-fold stratified group cross-validation on the remaining samples. Rank models by mean validation macro F1, giving each of the five labels equal weight. Stratification aims for similar class proportions while respecting groups. [Stratified group split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html) · [F1 score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html)
4. Refit the selected model on the full training partition and evaluate it on the held-out clusters. Inspect per-class precision and recall alongside the confusion matrix to see which morphologies the model confuses. [Classification metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics)

## Results

The Colab run used Kaggle version 1, Python 3.13.18, and scikit-learn 1.6.1. The mirror contained 4,049 crops in 966 parent groups. It contained 831 superficial-intermediate crops, compared with 813 in the original paper’s class table. The other four class counts matched. No exact file duplicates were found. The split reserved 814 crops and used 3,235 for training and model selection.

| Model | Mean validation macro F1 | Fold SD | Mean validation balanced accuracy |
| --- | ---: | ---: | ---: |
| Random forest | 0.8188 | 0.0475 | 0.8209 |
| Logistic regression | 0.7508 | 0.0174 | 0.7529 |
| Majority baseline | 0.0601 | 0.0069 | 0.2000 |

Random forest scored **0.7993 macro F1** on 814 held-out crops, with **80.34% accuracy** and **80.31% balanced accuracy**. The most frequent error was labeling dyskeratotic cells as koilocytotic (23 crops). Koilocytotic cells had the lowest recall (67.92%).

| Actual ↓ / Predicted → | Dyskeratotic | Koilocytotic | Metaplastic | Parabasal | Superficial-intermediate |
| --- | ---: | ---: | ---: | ---: | ---: |
| Dyskeratotic | 180 | 23 | 1 | 0 | 0 |
| Koilocytotic | 16 | 108 | 11 | 12 | 12 |
| Metaplastic | 10 | 11 | 146 | 12 | 9 |
| Parabasal | 5 | 1 | 10 | 90 | 0 |
| Superficial-intermediate | 10 | 6 | 4 | 7 | 130 |

The matrix contains 654 correct predictions and 160 errors. The validation fold standard deviation describes variation across folds.

## Limitations

A parent cluster split controls overlap between crops from the same cluster. It does not establish patient or slide independence. The data come from a single published collection and the models see manually isolated cells, so the benchmark cannot estimate full-slide or patient-level screening performance. A study of invasive cervical cancer would require independently held-out, clinically verified invasive cancer labels and an evaluation design appropriate to that endpoint.

## Dataset citation

Plissiti, M. E., Dimitrakopoulos, P., Sfikas, G., Nikou, C., Krikoni, O., & Charchanti, A. (2018). SIPaKMeD: A new dataset for feature and image based classification of normal and pathological cervical cells in Pap smear images. IEEE International Conference on Image Processing, 3144–3148. [Paper](https://www.cse.uoi.gr/~cnikou/Publications/C072%20-%20Plissiti%20-%20icip%202018%20-%20Athens.pdf)
