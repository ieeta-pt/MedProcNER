# MEDPROCNER CORPUS README

## What is MEDPROCNER

MedProcNER stands for MEDical PROCedure Named Entity Recognition. It is a shared task and set of resources focused on the detection, normalization and indexing of clinical procedures in medical documents in Spanish. MedProcNER is complementary to the DisTEMIST corpus (https://temu.bsc.es/distemist) as they both use the same document collection, which is why it's also called ProcTEMIST.

This repository includes the Train Set of the task, which includes a total of 750 documents. The unannotated test text files are also included so that predictions can be created for them. Finally, we include a gazetteer of possible SNOMED CT codes for the normalization and indexing tasks.

MedProcNER was developed by the Barcelona Supercomputing Center's NLP for Biomedical Information Analysis and used as part of BioASQ @ CLEF 2023. For more information on the corpus, annotation scheme and task in general, please visit: https://temu.bsc.es/medprocner.

## Folder Structure

This repository includes:

- `medprocner_train/`: Training section of the corpus.
- `medprocner_test/`: Test section of the corpus (currently only includes text files).
- `medprocner_gazetteer/`: Lexical resources to be used for the task.

## Files Format

The MedProcNER corpus is offered in two different formats, each separated in a different folder:

- `medprocner_train/brat/`

Original documents resulting from the annotation process using the brat tool. Includes the brat .ann files together with the .txt files. For more information on brat's format please visit: https://brat.nlplab.org/standoff.html. Only the annotations for subtask 1 (NER) are included in this format.

- `medprocner_train/tsv/`

This folder includes tab-separated files (tsv) where each line represents an annotation. Three different files are included, one for each subtask:

  - `medprocner_train/tsv/medprocner_tsv_train_subtask1.tsv` includes the data for Subtask 1 (Named Entity Recognition).
  It has the following columns: "filename", "ann_id" (annotation identifier, not really needed for the task but kept for traceability), "label", "start_span", "end_span" and "text".

  - `medprocner_train/tsv/medprocner_tsv_train_subtask2.tsv` includes the data for Subtask 2 (Entity Linking/Normalization).
  It has the following columns: "filename", "label", "start_span", "end_span", "text", "code" (might be 'NO_CODE' if no code could be assigned), "sem_rel" (semantic relation between the assigned code and the entity, can be 'EXACT', 'NARROW' or 'NO_CODE'), "is_abbrev" (whether the mention is or includes an abbreviation), "is_composite" (whether the mention was normalized to more than one code; multiple codes are joint using a '+' sign) and "need_context" (whether the annotator needed to see the text to disambiguate the mention and assign a code).

  - `medprocner_train/tsv/medprocner_tsv_train_subtask3.tsv` includes the data for Subtask 3 (Indexing).
  It has the following columns: "filename", "codes" (list of SNOMED CT codes associated with the text).

## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

## Contact

If you have any questions or suggestions, please contact us at:

- Salvador Lima-López (<salvador [dot] limalopez [at] gmail [dot] com>)
- Martin Krallinger (<krallinger [dot] martin [at] gmail [dot] com>)
