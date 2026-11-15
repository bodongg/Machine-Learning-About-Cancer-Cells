# Cervical cytology classification with machine learning

This project asks how well simple machine-learning models can classify **individual cervical cells in Pap smear images**. It compares logistic regression and random forest against a majority-class baseline. The model takes a cropped cell image and predicts one of five morphology labels.

## Run in Google Colab

1. Download [cervical-cytology-ml.ipynb](cervical-cytology-ml.ipynb).
2. Open [Google Colab](https://colab.research.google.com/), choose **File → Upload notebook**, and select the file.
3. Choose **Runtime → Run all**. A CPU runtime is sufficient. The notebook installs KaggleHub and downloads the public dataset. If Kaggle prompts for authentication, follow its instructions in Colab and keep credentials out of the notebook before sharing it.
4. Read the model comparison, then examine the held-out macro F1 and confusion matrix.

## Dataset

SIPaKMeD contains **4,049 isolated cell images** cropped from **966 parent cluster images**. The original authors permit experimental use and request citation of their ICIP 2018 paper. [Kaggle download](https://www.kaggle.com/datasets/prahladmehandiratta/cervical-cancer-largest-dataset-sipakmed) · [Original dataset and usage information](https://www.cs.uoi.gr/~marina/sipakmed.html) · [Original paper](https://www.cse.uoi.gr/~sfikas/sipakmed2018.pdf)

| Cell class | Crops |
| --- | ---: |
| Dyskeratotic | 813 |
| Koilocytotic | 825 |
| Metaplastic | 793 |
| Parabasal | 787 |
| Superficial-intermediate | 831 |

Dyskeratotic and koilocytotic are annotated as abnormal, nonmalignant cell types in the original paper. There is no confirmed invasive-cancer label. The project evaluates cell morphology for cervical cancer screening research. [Original paper](https://www.cse.uoi.gr/~sfikas/sipakmed2018.pdf)

## Experiment

The notebook extracts histogram of oriented gradients (HOG) features to describe local edges and RGB histograms to summarize color. It keeps crops from a shared parent cluster together in the held-out split and during training cross-validation. The model with the highest mean validation macro F1 is evaluated on the held-out clusters.

**Macro F1** gives each cell class equal weight. **Per-class recall** shows how often the model finds each class. The **confusion matrix** shows which classes are mistaken for one another. Cluster-level grouping does not establish that patients are separated across splits. See the [research report](research-report.md) for the evidence and limitations.

## Results

Random forest scored **0.7993 macro F1** on 814 held-out crops, with **80.34% accuracy** and **80.31% balanced accuracy**. The most frequent error was labeling dyskeratotic cells as koilocytotic (23 crops). Koilocytotic cells had the lowest recall (67.92%).

Mean validation macro F1 was 0.8188 for random forest, 0.7508 for logistic regression, and 0.0601 for the majority baseline. The experiment used Kaggle dataset version 1. See the [research report](research-report.md) for the full confusion matrix.

## 50 project contributions

### Scope and sources

1. Define the cervical cytology research question.
2. Frame the task as five-class morphology classification.
3. Identify cropped cells as the unit of prediction.
4. Identify parent clusters as the split unit.
5. Name all five cell labels.
6. Cite the original ICIP paper.
7. Link the original University of Ioannina dataset.
8. Use the public Kaggle mirror.
9. Report the expected image and cluster counts.
10. Explain the absence of a confirmed invasive-cancer class.

### Dataset checks

11. Download with KaggleHub.
12. Print the dataset cache path.
13. Record Python and scikit-learn versions.
14. Scan the cropped BMP directories.
15. Derive labels from the class directories.
16. Validate the crop filename format.
17. Derive parent cluster IDs from crop names.
18. Require matching parent image files.
19. Check the Kaggle class counts and report the parent group count.
20. Compute SHA-256 hashes for exact-duplicate checks.

### Exploration and features

21. Summarize crops and clusters by class.
22. Display one training crop per class.
23. Standardize image size to 64 × 64 pixels.
24. Convert input images to RGB.
25. Convert a separate copy to grayscale for HOG.
26. Extract normalized HOG edge descriptors.
27. Compute per-channel RGB histograms.
28. Normalize histogram counts by image size.
29. Concatenate edge and color descriptors.
30. Verify the feature matrix shape and finiteness.

### Model selection

31. Fix a seed for reproducible sampling.
32. Reserve a stratified group holdout.
33. Check group separation in the holdout.
34. Check for repeated file hashes across the holdout split.
35. Check class coverage in each partition.
36. Use four stratified group training folds.
37. Recheck group and hash separation in each training fold.
38. Build a majority-class baseline.
39. Compare scaled logistic regression and a random forest.
40. Select the model using mean validation macro F1.

### Evaluation and communication

41. Report validation macro F1 variability across folds.
42. Compare validation balanced accuracy.
43. Refit the selected model on all training data.
44. Report held-out accuracy, balanced accuracy, and macro F1.
45. Report class-level precision, recall, F1, and support.
46. Plot the held-out confusion matrix.
47. Show examples from the misclassification table.
48. Explain the limits of cluster-level splitting.
49. Propose external validation and a feature comparison.
50. Provide a Colab walkthrough and a research report.


