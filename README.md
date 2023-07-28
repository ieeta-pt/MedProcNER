# BIT.UA at MedProcNer: Discovering Medical Procedures in Spanish Using Transformer Models with MCRF and Augmentation

![Main Image](figures/NER_main.jpg)

## Overview
This repository hosts the work detailed in our paper, [BIT.UA at MedProcNer: Discovering Medical Procedures in Spanish Using Transformer Models with MCRF and Augmentation](https://www.dei.unipd.it/~faggioli/temp/CLEF2023-proceedings/paper-05.pdf).

## Contributors
- [Tiago Almeida](https://t-almeida.github.io/online-cv/) - tiagomeloalmeida@ua.pt - ORCID: 0000-0002-4258-3350
- Richard A. A. Jonker - richard.jonker@ua.pt - ORCID: 0000-0002-3806-6940
- Roshan Poudel - proshan@ua.pt - ORCID: 0000-0001-6450-023X
- [Jorge M. Silva](https://jorgeMFS.com/) - jorge.miguel.ferreira.silva@ua.pt - ORCID: 0000-0002-6331-6091
- Sérgio Matos - aleixomatos@ua.pt - ORCID: 0000-0003-1941-3983

## Dataset
We use the MedProcNER corpus in our study. The MedProcNER corpus is a collection of 1,000 clinical case reports in Spanish annotated with clinical procedure mentions and normalized to SNOMED CT. You can access the dataset [here](https://temu.bsc.es/medprocner/corpus-description/).

- [Gold Standard data (includes train and test set, as well as gazetteers)](https://doi.org/10.5281/zenodo.7817745)
- [Annotation Guidelines (Spanish)](https://doi.org/10.5281/zenodo.7817666)

## Repository Organization
- **HF_CACHE** : cache directory for downloading models from Hugging Face
- **dataset** : folder for MedProcNER dataset
- **medprocner-submission** : folder containing submission for all subtasks (results)
- **subtask-1** : code for subtask 1 NER 
- **subtask-2** : code for subtask 2, entity linking to concepts
- **subtask-3** : code for subtask 3, indexing the concepts
- **trained_models** : folder containing trained models

## How to Run the Code
Prerequisites: Python version 3.9 (minimum); We used Python version 3.10

```bash
git clone https://github.com/ieeta-pt/MedProcNER.git
chmod +x setup.sh 
bash setup.sh # installs environments and requirement dependencies
```

## Replicating Submissions

The `make_runs.sh` scripts are available in the respective subtask directories. They're shell scripts which execute a series of commands for replicating the results we obtained in our study. Here's how to use them and what they do:

### Subtask-1
To replicate the results of Subtask-1, navigate to the `subtask-1` directory and run `make_runs.sh`:

```bash
cd subtask-1
./make_runs.sh
```

This script performs the following steps:
1. Downloads the models used for this subtask.
2. Runs the downloaded models on the provided dataset.
3. Combines the results of different model runs to form an ensemble.
4. Converts the results to the MedProcNER format for submission.

### Subtask-2
To replicate the results of Subtask-2, navigate to the `subtask-2` directory and run `make_runs.sh`:

```bash
cd ../subtask-2
./make_runs.sh
```

This script performs the following steps:
1. Downloads the models used for this subtask.
2. Creates a semantic index for the SNOMED CT medical terminology system.
3. Performs a semantic search on the indexed terms using the results from the model runs.
4. Converts the results to the MedProcNER format for submission.

### Subtask-3
To replicate the results of Subtask-3, navigate to the `subtask-3` directory and run `make_runs.sh`:

```bash
cd ../subtask-3
./make_runs.sh
```

This script performs the following steps:
1. Converts the identified medical concepts from Subtask-2 into an index list.
2. The resulting index list represents the results for Subtask-3 and is ready for submission.

By running these scripts, you can replicate our submissions for each subtask.

## Training
Check the README in the `subtask-1` folder to learn how to train the NER models.

## Results

Comparison of System Performances on Subtasks with Best Competition Results:

| **System** | **Models Used** | **Aug.** | **Data** | **Subtask-1 F1** | **Subtask-2 F1** | **Subtask-3 F1** |
| --- | --- | --- | --- | --- | --- | --- |
| system-0 | 5 x lcampillos-dense | UNK | no val | 79.46 | 31.53 | 35.67 |
| system-1 | 5 x lcampillos-dense | UNK | full | 79.24 | 31.32 | 35.42 |
| system-2 | 30 x lcampillos-bilstm | mixed | mixed | 78.81 | 31.10 | 35.37 |
| system-3 | 20 x plantl-mixed | mixed | no val | 79.23 | 31.66 | 35.98 |
| system-4 | All plantl and lcampilos (91) | mixed | mixed | **79.85** | 31.68 | 35.85 |
| **Best** | - | - | - | **79.85** | **57.07** | **62.42** |

## Issues
For any issue you encounter with the repository or code, please report it to the [Issues section](https://github.com/ieeta-pt/MedProcNER/issues).

## Citation
If you find this helpful work and use it in your own research, please cite our paper as follows:

```bibtex
@inproceedings{bituaMedprocner,
title={ {BIT.UA} at {M}ed{P}roc{N}er: Discovering Medical Procedures in Spanish Using Transformer Models with {MCRF} and Augmentation},
author={Almeida, Tiago and Jonker, Richard A. A. and Poudel, Roshan and Silva, Jorge M. and Matos, Sérgio},
booktitle={Working Notes of CLEF 2023 - Conference and Labs of the Evaluation Forum},
year={2023}
}
```
