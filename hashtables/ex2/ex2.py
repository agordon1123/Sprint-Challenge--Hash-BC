#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    # add tickets to hashtable
    for i in range(length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)

    # find first
    iterfirst = hash_table_retrieve(hashtable, "NONE")
    
    for j in range(length):
        route[j] = iterfirst
        # find where key is destination
        target = hash_table_retrieve(hashtable, iterfirst)
        iterfirst = target

    return route
