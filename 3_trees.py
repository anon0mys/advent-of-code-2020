
slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

tree_map = open('inputs/3_trees.txt').read().split('\n')


def count_trees_on_slope(slope, tree_map):
    row_length = len(tree_map[0])
    trees = 0
    toboggan_coords = (0, 0)
    while toboggan_coords[1] < len(tree_map) - 1:
        toboggan_coords = move_toboggan(toboggan_coords, slope, row_length)
        if tree_at_coords(toboggan_coords, tree_map):
            trees += 1
    return trees


def tree_at_coords(toboggan_coords, tree_map):
    x, y = toboggan_coords
    return tree_map[y][x] == '#'


def move_toboggan(toboggan_coords, slope, row_length):
    x = toboggan_coords[0] + slope[0]
    y = toboggan_coords[1] + slope[1]
    if x >= row_length:
        x = x - row_length
    return (x, y)


def product_of_trees(trees_list):
    product = 1
    for trees in trees_list:
        product = product * trees
    return product


all_trees = []
for slope in slopes:
    trees = count_trees_on_slope(slope, tree_map)
    all_trees.append(trees)
    print(f'Slope: {slope} Trees: {trees} AllTrees: {all_trees}')

print(f'Trees: {product_of_trees(all_trees)}')
