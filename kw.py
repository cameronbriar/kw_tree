#!/usr/bin/env python
import json

# Our keyword tree basically a dictionary
kw_tree = dict()

# What is a keyword
def is_good_keyword(keyword):
    # It must:
    # not be empty or contain whitespace
    if keyword.strip() == "" or " " in keyword:
        return False

    return True

# What is a kw tree?
def is_good_tree(tree):
    return isinstance(tree, dict)

def validate_kw_tree(kw, tree):
    return is_good_keyword(kw) and is_good_tree(tree)
 
def add_kw(keyword, tree):
    print 'adding', keyword
    for letter in keyword:
        if tree.get(letter) == None:
            tree[letter] = {}
        tree = tree[letter]
    print keyword, 'was added'
    return

def has_kw(keyword, tree):
    print 'checking for', keyword
    for letter in keyword:
        if tree.get(letter) == None:
            print keyword, 'not in tree'
            return False
        tree = tree[letter]
    print keyword, 'found'
    return True

# ...
def del_kw(keyword, tree):
    print 'deleting', keyword

    prev_pos = []
    for letter in keyword[:-1]:
        if tree.get(letter) != None:
            prev_pos.append(tree)
            tree = tree[letter]
        else:
            print keyword, 'was not found to delete'
            return False
        
    for letter in keyword[::-1]:
        if tree.get(letter) == {}:
            del(tree[letter])
            tree = prev_pos.pop()
    
    print keyword, 'removed'
    return True

def ptree(tree):
    print json.dumps(tree, indent=1)
    
# TEST
tree = kw_tree
good_kw0 = "test"
good_kw1 = "true"
good_kw2 = "temp"
bad_kw0  = "bad"

add_kw(good_kw0, tree)
add_kw(good_kw1, tree)
add_kw(good_kw2, tree)

print has_kw(good_kw0, tree)
print has_kw(good_kw1, tree)

print has_kw(bad_kw0, tree) 
del_kw(bad_kw0, tree)       

del_kw(good_kw0, tree)      
print has_kw(good_kw0, tree)

ptree(tree)
