def create_an_empty_list():
    return []


def create_a_list():
    newList = ["de", "mid","off","streets"]
    return newList

def add_element_to_end_of_list (New_List, element = "cat"):
    New_List = ["dog","eat","dog"]
    New_List.append(element)
    return New_List

def add_element_to_start_of_list(lof,element ="a"):
    lof = ["cpo","nigg","hm"]
    lof.insert(0,element)
    return lof

def remove_element_from_end_of_list(op):
    op = ["ngn","jig",3,"jih"]
    op.pop()
    return op

def remove_element_from_start_of_list(gi):
    gi = [1,2,3,4]
    del gi[0]
    return gi

def retrieve_first_element_from_list(ol):
    ol = [1,"do","top","car"]
    return ol[0]

def retrieve_element_from_index(ki, index):
   
    return ki[index]

def retrieve_last_element_from_list(lo):
    lo = [1,2,3,4]

    return lo[3]
