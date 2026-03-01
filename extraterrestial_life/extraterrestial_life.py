
# The parental gene sequences are stored here
one_ancestor = int(input())
other_ancestor = int(input())

# Calculate the identity of a new alien here
new_alien = (id(one_ancestor) + id(other_ancestor)) / 2
new_alien = int(new_alien)
