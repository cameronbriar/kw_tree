import json

# Our keyword tree basically a dictionary
kw_tree = dict()

# Let's define an add module
def add_kw(keyword, tree):
    
    if keyword.strip() == "":
        print 'Must be at least 1 character long'
        return
    
    for letter in keyword:
        if not tree.get(letter):
            tree[letter] = {}
        tree = tree[letter]
            
    return tree


# Let's define a get module
def get_kw(keyword, tree):
    
    if keyword.strip() == "":
        print 'Must be at least 1 character long'
        return
    
    # Starting point
    head = tree
    
    for letter in keyword:
        if head.get(letter) != None:
            head = head[letter]
        else:
            return False
    return True

# Let's define a remove module
def del_kw(keyword, tree):
    
    if keyword.strip() == "":
        print 'Must be at least 1 character long'
        return
    
    # Starting point
    head = tree
    
    # This list stores the path to the last letter of the keyword
    # (helps you delete and take a step backward)
    prev_pos = []
    
    for letter in keyword[:-1]:
        if head.get(letter) != None:
            prev_pos.append(head)
            head = head[letter]
        else:
            print 'Word not found'
            return False
        
    curr = len(keyword) - 1
    for letter in keyword[::-1]:
        if head.get(letter) == {}:
            del(head[letter])
            head = prev_pos.pop()
        else:
            print 'Keyword removed'
    
    del(prev_pos)
    return True
    
# TEST

print "KW: Add 'test' --", add_kw("test", kw_tree)
print "KW: Add 'true' --", add_kw("true", kw_tree)
print "KW: Add 'alpha' --", add_kw("alpha", kw_tree)

print json.dumps(kw_tree, indent=1)

print "KW: Has 'tire' -- ", get_kw("tire", kw_tree) # should be False
print "KW: Has 'true' -- ", get_kw("true", kw_tree) # should be True

print "KW: Del 'fox' --", del_kw("fox", kw_tree) # should return 'Word not found'
print "KW: Del 'true' --", del_kw("true", kw_tree) # should return 'Keyword removed'

print "KW: Has 'true' --", get_kw("true", kw_tree) # should be False
