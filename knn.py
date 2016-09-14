import euclid as e
from math import floor

def knn(learn_data, learn_labels, test_data, k):
    """
    knn(learn_data, learn_labels, test_data, k) -> test_labels
    
    Find the labels for a list of data using k-narest-neighbor, 
    with labels being 1 and -1
    """
    if k<1:
        raise ValueError('k must be possitive, k = '+str(k))
    if k%2==0:
        raise ValueError('k must be odd, k = '+str(k))
    test_labels = []
    learn_data = list(enumerate(learn_data))
    for point in test_data:
        test_labels.append(find_label(learn_data, learn_labels, point, k))
    return test_labels
    
def find_label(learn_data, learn_labels, point, k):
    """
    find the label of a given point using k-nearest-neighbor
    """
    distances = []
    for data in learn_data:
        distances.append((e.dist(data[1],point),data[0]))
    distances.sort()
    
    if [learn_labels[i] for (d,i) in distances[:k]].count(1) > floor(k/2):
        label = 1
    else:
        label = -1
    return label
    

