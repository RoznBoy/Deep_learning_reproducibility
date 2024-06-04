# Deep_learning_reproducibility
Deep_Learning_reproducibility&amp;Generalization

# Weight Predictor Network with Feature Selection for Small Sample Tabular Biomedical Data

## Introduction
This repository contains the implementation of the Weight Predictor Network with Feature Selection (WPFS) for handling high-dimensional and small sample tabular biomedical data. The primary focus of this work is to address the challenges posed by the high dimensionality and limited number of samples in biomedical datasets, which often lead to overfitting and include many potentially irrelevant features.

## Problem Statement
Biomedical data typically have the following issues:
- **High-dimensional data**: A large number of features make the analysis complex.
- **Small sample size**: The limited number of samples increases the risk of overfitting.
- **Potentially irrelevant features**: Many features might not significantly impact the prediction outcome.

## Contributions
To tackle these challenges, we propose the Weight Predictor Network with Feature Selection (WPFS), which incorporates the following key innovations:
- **WPFS model proposal**: A novel model for training neural networks on high-dimensional and small sample data.
- **Feature selection and weight prediction**: WPFS reduces the number of learnable parameters while simultaneously performing feature selection.
- **Auxiliary networks**: Two small auxiliary networks are designed to output the weights of the first layer of the classification model.

## Results
- **Performance evaluation**: WPFS was evaluated on nine real-world biomedical datasets, demonstrating superior performance compared to standard and recent methods typically applied to tabular data.
- **Effectiveness of feature selection mechanism**: The proposed feature selection mechanism improved performance and provided useful insights into the learning task.

## Conclusion
The WPFS model effectively handles high-dimensional, small sample biomedical data by reducing the risk of overfitting and selecting relevant features. This approach has been validated across multiple datasets, showing its potential to significantly enhance biomedical data analysis.

This README file provides instructions on how to run the reproducibility experiment code for Weight Predictor Networks with Sparse Feature Selection for Small Size Tabular Biomedical Data (WPFS).

## Running Experiments

This README file provides instructions on how to run the reproducibility experiment code for Weight Predictor Networks with Sparse Feature Selection for Small Size Tabular Biomedical Data (WPFS).

**Note:** The code for the paper is available at [https://github.com/Dirkster99/MRULib](https://github.com/Dirkster99/MRULib). The runtime environment suggested by this GitHub repository should be used for running the experiments.

**Running Experiments with Auxiliary Network Removal**

This experiment utilizes files from the `remove network` folder.

1. Replace the `model.py` file in the above GitHub repository with the `remove network/model.py` file.
2. Add the `play.py` file from the `remove network` folder in the `src` folder of the above GitHub repository.
3. Run the experiment with the command `python play.py`.
4. Replace the `main.py` file in the above GitHub repository with the `remove network` folder's `main.py` file to view the experiment results in a CSV file.

**Running Experiments with All Data**

This experiment utilizes files from the `Params_test` folder.

1. Move the `params_test_main` file from the `Params_test` folder of the cloned paper code to the `WPFS/src` folder.
2. The `run_all_data_experiments` file can be used to obtain the results of running all datasets for 25 times for various models by changing the `model`. The `model` value should be changed in the code as follows:

```python
# Change model
model = "WPFS" # Default model
# model = "fsnet" # fsnet model
# model = "cae" # cae model

# ... rest of the code ...
```

3. The `run_params_test` file is a folder for experimenting with various parameters for the WPFS model. It can be used to obtain the average of 25 runs with different parameters for each dataset in a CSV file.



**Feature Selection and Feature Extraction Experiment** 

This experiment utilizes files from the `MLP_variant` folder.

This experiment can be verified through the `embedding_test.ipynb` file in the `MLP_variant` folder.
Experiment Code for Each Cell: vanila MLP ,MLP+SVD(feature 50 ), MLP+SVD(feature 100), MLP+NME, MLP+Dot histogram 
