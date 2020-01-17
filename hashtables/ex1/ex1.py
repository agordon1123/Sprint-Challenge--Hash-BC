#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    hashtable = HashTable(length)

    # add weights to hashtable
    # :<key>: weight
    # :<val: index in weights
    for i in range(len(weights)):
        print(weights[i])
        
        hash_table_insert(hashtable, weights[i], i)

    for j in range(len(weights)):
        remainder = limit - weights[j]

        target = hash_table_retrieve(hashtable, remainder)
        
        if target is not None:
            if weights[j] > remainder:
                return (j, target)
            else:
                return (target, j)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
