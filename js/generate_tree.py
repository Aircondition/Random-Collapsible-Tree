import random
import numpy as np

random.seed()

probability_distribution = [0.25, 0.50, 0.125, 0.125, 0]
num_Chidren_max = len(probability_distribution)
def add_children (node, n):
    if (n != 0):
        for i in range(0, n):
            node['children'].append({'name': random.choice(names_list) + ' ' + random.choice(surenames_list), 'children': [], 'value': 10, 'type': 'black', 'level': 'red'})
def extend_tree (node, probability_distribution):
    if not node['children']:
        add_children (node, np.random.choice(num_Chidren_max, 1, probability_distribution)[0])
    else:
        for kids in node['children']:
            extend_tree(kids, probability_distribution)
# Ideja je da napravim prbability density za broj eksplodiranog offspringa

# a little bit of data
names_list = ['William','James','Harper','Mason','Evelyn','Ella','Jackson','Avery']
surenames_list = ['Smith','Jones','Taylor','Brown','Williams','Wilson','Johnson','Davies']

#lines je glavni output u .tex fajl
root = {'name': random.choice(names_list) + ' ' + random.choice(surenames_list), 'children': [], 'value': 10, 'type': 'black', 'level': 'red'}
extend_tree(root, probability_distribution)
extend_tree(root, probability_distribution)
extend_tree(root, probability_distribution)
extend_tree(root, probability_distribution)
extend_tree(root, probability_distribution)
extend_tree(root, probability_distribution)

a_file = open("script.js", "r")
list_of_lines = a_file.readlines()
list_of_lines[0] = "var treeData = [" + str(root) + "]\n"

a_file = open("script.js", "w")
a_file.writelines(list_of_lines)
a_file.close()