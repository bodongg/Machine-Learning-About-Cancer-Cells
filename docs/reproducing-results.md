# Record a notebook run

Use the [Colab setup instructions](../README.md#run-in-google-colab) and start from a fresh CPU runtime. Run all cells in order so the reported results describe one execution.

## Record alongside the scores

| Stage | What to save |
| --- | --- |
| Input | Kaggle dataset handle and version, software versions, and any local changes to the notebook |
| Index | Class and parent-cluster counts, plus the reported number of repeated file hashes |
| Split and features | Sample counts for train and holdout, group separation checks, and feature matrix shape |
| Model selection | Mean and fold variation in training cross-validation, baseline score, and selected model |
| Holdout | Macro F1, balanced accuracy, per-class support, and the confusion matrix |

The run in the [research report](../research-report.md) used Kaggle version 1 and reports 4,049 crops, of which 814 were held out. If a rerun differs, compare the dataset version and partition counts before comparing scores. Keep new results with their own run details.

Use the scores to describe this cropped-cell benchmark. Parent-cluster separation leaves patient-level independence unverified. Share aggregate results and keep credentials and local data out of the run record.
