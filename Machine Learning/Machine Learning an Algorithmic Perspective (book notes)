# 1. Introduction

## 1.4 Supervised Learning
There is a set of data (**the training data**) that consists of a set of input data that has **target** data, which is the answer that the algorithm should produce.<br>
<br>


### 1.4.1 Regression
Regression tries to give value for `y` based on the values of `x`, describind a curve that will pass as close as possible to all the datapoints, predicting `y` for `x's` that we do not exist.<br>
<br>


### 1.4.2 Classification
Classification consists in taking input vectors and deciding which of `N` classes they belong to, based on training from **exemplars** of each class. The different classes are separated by decision bondaries.<br>
The input vectors are the attributes that identifies the observation to a group. These attributes are numerics.<br>
It's not wise to use too many input vectors, otherwise the training of the classifier will take too long and the number of datapoints required will increase.


## 1.5 The machine learning process


##### Data collection and preparation
Considerations:
   * Does the data has significant **erros, missing values, or duplications**?
   * Needs **target** data
   * Is there enough data to apply machine learning algorithms?


##### Feature selection
Features are the variables we can collect and/or use to predict `y`.
It's wise to select features that can be collected without significant expense or time, and do not create noises or other corruptions in the data.


##### Algorithm choice
Decide which algorithm is the best option for the study.


##### Parameter and model selectionthe target 

##### Training
Build a model of the data in order to predict outputs. <br>


##### Evaluation
Test and evaluate for accuracy of the program. <br>



<br>
<br>


# 2. Preliminaries

## 2.1 Some termiology
   * **Inputs** data given as one input to the algorithm. Written as `x`, with elements ![xi](http://latex.codecogs.com/gif.latex?x_%7Bi%7D), where`i` runs from 1 to the number of input dimensions, `m`.
   * **Weights** `w_ij`, are the weighted connections between nodes `i` and `j`, aranged in a matrix `W`.
   * **Uoutputs** is `y` with elements `yj`, where `j` runs from 1 to the number of output dimensions, `n`.
   * **Targets** the target vector `ti` is the correct answer that the algorithms are running about.
   * **Activation function** `g(*)`is a mathematical function.
   * **Error** `E` is a function that computres the innacuracy of the network as a function of the outputs `y` and targets `t`.
   
   
### 2.1.1 Weight Space
![Not understood](http://latex.codecogs.com/gif.latex?%5Ccolor%7Bred%7D%3F%3F%3F%3F%3F%3F%3F%3F%3F%3F%3F%3F%3F%3F%3F%3F%3F)

Euclidean distance:
![Euclidean distance](http://latex.codecogs.com/gif.latex?d%20%3D%20%5Csqrt%7B%28x_1-x_2%29%5E2%20&plus;%20%28y_1-y_2%29%5E2%7D)


### 2.1.2 The Curse of Dimensionality
As the number of dimensaions grow and space grow, the algorithm may get issues.


## 2.2 Knowing what you know: testing machine learning algorithms

### 2.2.1 Overlifting
If we train the algorithm too much, it will **overfit**, learning (memorizing) about the **noise** and **inaccuracies** in the data, instead of only the actual function.
When an overlifted algorithm is plotted, the line is not smooth, getting lost in its prediction.
The solution to avoid overlifting the algorithms, is to validate the algorithm with another data. We cannot use the training data because it wouldn't detect overlifting, and we cannot use the test data because it will be used only at the end. We need a third option, which is called **validation set**, because we are usin to **validate the learning** so far. This is known as **cross-validation** in statistics, part of **model selection**: choosing the right parameters for the model so that it generalises as well as possible.


### 2.2.2 Training, testing, and validation sets

##### Proportions of data of training to testing to validation
There is no specific proportions, but usually it's done (training, testing, validation) `50:25:25` if you have plenty of data, and `60:20:20` if you don't.


### 2.2.3 The confusion matrix
A matrix where the dagonal from top left to bottom right contains the correct predictions.


### 2.2.4 Accuracy metrics
A chart containing **true positives**, **false positives**, **false negatives**, and **true negatives**, and the diagonal from top left to bottom right is true positive and true negative, the correct predictions.
**Accuracy** is then defined as the `sum of the number of true positives and true negatives divided by the total number of examples`, as follows (`#` means `number of`, and `TP` stands for True Positive, etc):
![Accuracy metrics](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5C%23TP%20&plus;%20%5C%23TN%7D%7B%5C%23TP%20&plus;%20%5C%23FP%20&plus;%20%5C%23TN%20&plus;%20%5C%23FN%7D)

Accuracy is not the only peace to measure the results, since it turns 4 numbers into just one. To better interpret the performance of a classifier, we have two complementary pairs of measurements:
   * **Sensitivity** and **Specificity**
      + Sensitivity (true positive rate)
          + Is the number of correct positive examples to the number classified as positive
          + ![Sensitivity](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5C%23TP%7D%7B%5C%23TP%20&plus;%20%5C%23FN%7D)
      + Specificity (true negative rate)
          + Is the number of correct negative examples to the number of classified negative
          + ![Specificity](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5C%23TN%7D%7B%5C%23TN%20&plus;%20%5C%23FP%7D)
   * **Precision** and **Recall**
      + Precision
          + Is the ratio of correct positive examples to the number of actual positive examples
          + ![Precision](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5C%23TP%7D%7B%5C%23TP%20&plus;%20%5C%23FP%7D)
      + Recall
          + Is the ratio of the number of correct positive examples out of those that were classified as positive, which is the same as sensitivity
          + ![Recall](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5C%23TP%7D%7B%5C%23TP%20&plus;%20%5C%23FN%7D)
               
Together, these pairs give more information then `accuracy` alone.<br>
![F1](http://latex.codecogs.com/gif.latex?F_1%20%3D%202%20%5Cfrac%7Bprecision%20X%20recall%7D%7Bprecision%20&plus;%20recall%7D)<br>
or
<br>
![F1.2](http://latex.codecogs.com/gif.latex?F_1%20%3D%20%5Cfrac%7B%5C%23TP%7D%7B%5C%23TP%20&plus;%20%28%5C%23FN%20&plus;%20%5C%23FP%29%20/%202%7D)


### 2.2.5 The receiver operator characteristic (ROC) curve
The ROC is a way to compare classifiers in a plot with true positives in the y-axis and false positives in the x-axis.


### 2.2.6 Unbalanced datasets
**Balanced dataset** is dataset with the same number of positive and negative examples.
For datasets not balanced, we can use the **balanced accuracy**, that is the `sum of sensitivity and specificity divided by 2`.
But a better way is the **Mattew's Correlation Coefficient**, which is:
![MCC](http://latex.codecogs.com/gif.latex?MCC%20%3D%20%5Cfrac%7B%5C%23TP%20X%20%5C%23TN%20-%20%5C%23FP%20X%20%5C%23FN%7D%7B%5Csqrt%7B%28%5C%23TP%20&plus;%20%5C%23FP%29%28%5C%23TP%20&plus;%20%5C%23FN%29%28%5C%23TN%20&plus;%20%5C%23FP%29%28%5C%23TN%20&plus;%20%5C%23FP%29%28%5C%23TN%20&plus;%20%5C%23FN%29%7D%7D)
If any of the denominators is `0`, the whole set of denominators is set to `1`, providing a balanced accuracy computation.



### 2.2.7 Measurement precision
**Precision** is a way to measure the variability of a algorithm, telling how repeatable the predictions are, when we feed in a set of similar inputs (resulting in similar outputs also).
**Trueness** is the average distance between the correct output and the prediction. It's useful when there is some concept of certain classes being similar to each other.





## 7.2 Nearest Neighbour methods
Nearest neighbour algorithms are based on distance between inputs. It's very computionally expensive.


### 7.2.1 Nearest neighbour smoothing
Nearest neighbour van also be used for regression. 


### 7.2.2 Efficient distance computations: the KD-Tree
Computing distances is very expensivy computionally. **KD-Trees** is an solution for find the neares neighbors.
The idea behind **KD-Trees** is very simple. You create a binary tree by choosing one dimension at a time to split into two, and placing the line through the median of the point coordinates of that dimension. The points themselves end up as leaves of the tree. Making the tree is simple as follows, we identify a place to split into two choices, left and right, and then carry on down the tree. This makes it natural to write the algorithm **recursively**.

(Exemple of code and detailed explanation in pg. 162)


### 7.2.3 Distance Measures
**Euclidean distance:**
![Euclidean distance](http://latex.codecogs.com/gif.latex?d%20%3D%20%5Csqrt%7B%28x_1-x_2%29%5E2%20&plus;%20%28y_1-y_2%29%5E2%7D)

**City-block** or **Manhattan** distance:
![City-block distance](http://latex.codecogs.com/gif.latex?d_c%20%3D%20%7Cx_1-x_2%7C&plus;%7Cy_1-y_2%7C)











#######################################################################


# Supervised Learning

There is a set of data (**the training data**) that consists of a set of input data that has **target** data, which is the answer that the algorithm should produce.<br>
<br>


## Regression

Regression tries to give value for `y` based on the values of `x`, describind a curve that will pass as close as possible to all the datapoints, predicting `y` for `x's` that we do not exist.<br>
<br>


## Classification

Classification consists in taking input vectors and deciding which of `N` classes they belong to, based on training from **exemplars** of each class. The different classes are separated by decision bondaries.<br>
The input vectors are the attributes that identifies the observation to a group. These attributes are numerics.<br>
It's not wise to use too many input vectors, otherwise the training of the classifier will take too long and the number of datapoints required will increase. 









# Bayen Naive

Probability of **HIGH** `profit` given `type` = Drama, `Plot` = Drama, `Star Actor` = Yes:
![Probability of High](http://latex.codecogs.com/gif.latex?P%28high%29*P%28drama%7Chigh%29*P%28shallow%7Chigh%29*P%28starts%7Chigh%29)

Probability of **LOW** `profit` given `type` = Drama, `Plot` = Drama, `Star Actor` = Yes:
![Probability of Low](http://latex.codecogs.com/gif.latex?P%28low%29*P%28drama%7Clow%29*P%28shallow%7Clow%29*P%28starts%7Clow%29)






# Probabilities

## Turning data into probabilities
**Probability** is the number of times of 'C1' divided by the total number of examples ('n_c1/n()'). <br><br>

**Condiftional probability** is the probability that the class is 'C1' when 'x' is 'X' (**P(C1|X**). <br>
The first thing that we need to do to get these values is to **quantise** the measurement 'x' , which just means
that we put it into one of a discrete set of values { 'X' } , such as the bins in a histogram. Now, if we have
lots of examples of the two classes, and the histogram bins that their measurements fall into, we can compute 'P(Ci,Xj)',
which is the **joint probability**, and tells us how often a measurement of 'Ci' fell into histogram bin 'Xj'.
We do this by looking in histogram bin 'Xj', counting the number of examples of class 'Ci' that are in it, and dividing by
the total number of examples (of any class).<br><br>

We can also define 'P(Xj|Ci)', which is a different conditional probability, and tells us how often (in the training set)
there is a measurement of 'Xj' given that the example is a member of class 'Ci'. Again, we can just get this information
from the histogram by counting the number of examples of class 'Ci' in histogram bin 'Xj' and dividing by the number of
examples of that class there are (in any bin). <br><br>

### Bayes' rule
P(C_{i},X_{j}) = P(X_{j}|C_{i})P(C_{i}









