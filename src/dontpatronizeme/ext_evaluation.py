#!/usr/bin/env python
import pandas, numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, multilabel_confusion_matrix

pcl_categories = ['Unbalanced Power Relations', 'Shallow Solution', 'Presupposition', 'Authority Voice', 'Metaphor', 'Compassion', 'The poorer the merrier']
hl_categories = ['The saviour', 'The expert', 'The poet']

def evaluate(y_true, y_predicted, mode = 'll', verbose = True):
    # evaluate predictions per pcl category, based on level of taxonomy 
    if mode == 'll':    # lower level labels
        return evaluate_per_category(y_true, y_predicted, pcl_categories, verbose)
    elif mode == 'hl':  # higher level labels
        return evaluate_per_category(y_true, y_predicted, hl_categories, verbose)
    

def evaluate_per_category(y_true, y_predicted, categories, verbose = True):
    # if verbose is False, only compute F1 Average and return that, otherwise print full report
    if verbose:
        cm = multilabel_confusion_matrix(y_true, y_predicted)
    f1_scores = []
    for i in range(0, len(y_true[0])):
        true_for_category = [entry[i] for entry in y_true]
        pred_for_category = [entry[i] for entry in y_predicted]
        if verbose:
            print(categories[i])
            print('Accuracy:', accuracy_score(true_for_category, pred_for_category))
            print('Precision:', precision_score(true_for_category, pred_for_category))
            print('Recall:', recall_score(true_for_category, pred_for_category))
            print('F1 Score:', f1_score(true_for_category, pred_for_category))
        f1_scores.append(f1_score(true_for_category, pred_for_category))
        if verbose:
            print('Confusion Matrix: (tn, fp / fn, tp)' )
            print(cm[i])
            print('--------------------------------------------------')

    f1_avg = np.mean(f1_scores)
    if verbose:
        print('F1 Score Average:', f1_avg)
    else:
        return f1_avg
