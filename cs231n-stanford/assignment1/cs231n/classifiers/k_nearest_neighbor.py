import numpy as np

class KNearestNeighbor:
  """ a kNN classifier with L2 distance """

  def __init__(self):
    pass

  def train(self, X, y):
    """
    Train the classifier. For k-nearest neighbors this is just
    memorizing the training data.

    Input:
    X - A num_train x dimension array where each row is a training point.
    y - A vector of length num_train, where y[i] is the label for X[i, :]
    """
    self.X_train = X
    self.y_train = y

  def predict(self, X, k=1, num_loops=0):
    """
    Predict labels for test data using this classifier.

    Input:
    X - A num_test x dimension array where each row is a test point.
    k - The number of nearest neighbors that vote for predicted label
    num_loops - Determines which method to use to compute distances
                between training points and test points.

    Output:
    y - A vector of length num_test, where y[i] is the predicted label for the
        test point X[i, :].
    """
    if num_loops == 0:
      dists = self.compute_distances_no_loops(X)
    elif num_loops == 1:
      dists = self.compute_distances_one_loop(X)
    elif num_loops == 2:
      dists = self.compute_distances_two_loops(X)
    else:
      raise ValueError('Invalid value %d for num_loops' % num_loops)

    return self.predict_labels(dists, k=k)

  def compute_distances_two_loops(self, X):
    """
    Compute the distance between each test point in X and each training point
    in self.X_train using a nested loop over both the training data and the
    test data.

    Input:
    X - An num_test x dimension array where each row is a test point.

    Output:
    dists - A num_test x num_train array where dists[i, j] is the distance
            between the ith test point and the jth training point.
    """
    num_test = X.shape[0]
    num_train = self.X_train.shape[0]
    dists = np.zeros((num_test, num_train))
    for i in xrange(num_test):
      for j in xrange(num_train):
        #####################################################################
        # TODO:                                                             #
        # Compute the l2 distance between the ith test point and the jth    #
        # training point, and store the result in dists[i, j]               #
        #####################################################################
        dists[i, j] = np.sqrt(np.sum(np.square(X[i, :] - self.X_train[j, :])))
        #####################################################################
        #                       END OF YOUR CODE                            #
        #####################################################################
    return dists

  def compute_distances_one_loop(self, X):
    """
    Compute the distance between each test point in X and each training point
    in self.X_train using a single loop over the test data.

    Input / Output: Same as compute_distances_two_loops
    """
    num_test = X.shape[0]
    num_train = self.X_train.shape[0]
    dists = np.zeros((num_test, num_train))
    for i in xrange(num_test):
      #######################################################################
      # TODO:                                                               #
      # Compute the l2 distance between the ith test point and all training #
      # points, and store the result in dists[i, :].                        #
      #######################################################################
      dists[i, :] = np.sqrt(np.square(X[i] - self.X_train).sum(axis=1))

      #######################################################################
      #                         END OF YOUR CODE                            #
      #######################################################################
    return dists

  def compute_distances_no_loops(self, X):
    """
    Compute the distance between each test point in X and each training point
    in self.X_train using no explicit loops.

    Input / Output: Same as compute_distances_two_loops
    """
    num_test = X.shape[0]
    num_train = self.X_train.shape[0]
    dists = np.zeros((num_test, num_train))
    #########################################################################
    # TODO:                                                                 #
    # Compute the l2 distance between all test points and all training      #
    # points without using any explicit loops, and store the result in      #
    # dists.                                                                #
    # HINT: Try to formulate the l2 distance using matrix multiplication    #
    #       and two broadcast sums.                                         #
    #########################################################################

    # I got stuck, so grabbed the following from
    # https://github.com/eliben/deep-learning-samples/blob/master/cs231n/k_nearest_neighbor.py
    # Well explained!
    # -----------
    #
    # The sum in L2 distance is:
    #
    #   distance[i,j] = sqrt(Sum_p (X_train[i,p] - X[j,p])^2
    #
    # where 'p' is running over the pixels/colors vector.
    #
    # The expression inside the sum can be rewritten as:
    #
    #   X_train[i,p]^2 - 2*X_train[i,p]*X[j,p] + X[j,p]^2
    #
    # Note that the first and last items only depend on one of i or j, not
    # both, so they can be broadcast over the result array. And the middle
    # item can be computed as matrix multiplication between X_train and X
    # (one of them transposed).
    X_train_T = self.X_train.T

    # First compute the "cross-correlation" item using matrix mul,
    # transposing X_train since we want tests in rows and train in columns.
    # The shape of this is (num_test,num_train), which is also the shape
    # of the result.
    cross = -2.0 * X.dot(X_train_T)

    # Now compute the first item: norm of X_train. Sum all columns together,
    # getting a row vector.
    X_train_norm = np.sum(self.X_train ** 2, axis=1)

    # Similarly for X, but this time the results go into a column vector so
    # it gets broadcast per column of the result.
    X_norm = np.sum(X ** 2, axis=1, keepdims=True)

    # Finally sum up the parts and compute their sqrt.
    dists = np.sqrt(X_norm + cross + X_train_norm)


    #dists = np.sum(np.sqrt(X - self.X_train.T))
    #########################################################################
    #                         END OF YOUR CODE                              #
    #########################################################################
    return dists

  def predict_labels(self, dists, k=1):
    """
    Given a matrix of distances between test points and training points,
    predict a label for each test point.

    Input:
    dists - A num_test x num_train array where dists[i, j] gives the distance
            between the ith test point and the jth training point.

    Output:
    y - A vector of length num_test where y[i] is the predicted label for the
        ith test point.
    """
    """Predict labels, given a distances matrix.
          dists - (num_test, num_train) array; dists[i, j] is the distance between
                  the ith test point and the jth trainin point.
          k - how many neighbors to use.
          Output: a vector of length num_test where each element is the predicted
                  label for the test point.
          """
    num_tests = dists.shape[0]
    y_pred = np.zeros(num_tests)
    for i in xrange(num_tests):
      # dists[i] has the ith test distance from each training example.
      # argsort will produce sorted indices of training examples, from
      # smallest distance (closes) to largest distance. We can use this
      # to index into y_train to find the labels that are closest.
      closest_y = self.y_train[np.argsort(dists[i])]
      k_closest_y = closest_y[:k]

      # k_closest_y is a list of k labels that were the closest among
      # the training samples. Find the most common label among these.
      values, counts = np.unique(k_closest_y, return_counts=True)
      y_pred[i] = values[np.argmax(counts)]

    return y_pred

