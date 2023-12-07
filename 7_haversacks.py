# {
#     "light_red": {"muted_yellow": 1, "bright_white": 2},
#     "dark_orange": {"bright_white": 3, "muted_yellow": 4}
#     "bright_white": {"shiny_gold": 1}
#     "muted_yellow": {"shiny_gold": 2, "faded_blue": 9}
#     "shiny_gold": {"dark_olive": 1, "vibrant_plum": 2}
#     "dark_olive": {"faded_blue": 3, "dotted_black": 4}
#     "vibrant_plum": {"faded_blue": 5, "dotted_black": 6}
# }

# Loop outer keys
# loop inner keys until no children or shiny gold

# light red keys = ['muted_yellow', 'bright_white']
# muted_yellow keys = ['shiny_gold']
# Add one!
# bright_white keys = ['shiny_gold']
# Add one!

# dark olive bags contain 3 faded blue bags, 4 dotted black bags, 2 shiny gold bags.
# ['light red ', 's
#  contain 1 bright white ', ', 2 muted yellow ', 's.']
# ['faded blue ', 's contain no other ', 's.']
golden_bag = 'shiny gold'


def set_bag_count_index(bag_rule):
    for index, char in enumerate(bag_rule):
        try:
            int(char)
            return index
        except ValueError:
            pass
    return None


def parse_children(children):
    contains_bags = {}
    for child in children:
        bag_count_index = set_bag_count_index(child)
        if bag_count_index:
            child_bag = child[bag_count_index:].strip()
            contains_bags[child_bag[2:]] = int(child_bag[0])
    return contains_bags


def parse_rule(rule):
    rule_set = rule.strip().split('bag')
    return rule_set[0].strip(), rule_set[1:]


def parse_rule_file(filename):
    all_bags = {}
    with open(filename, 'r') as rules:
        for rule in rules:
            bag, children = parse_rule(rule)
            all_bags[bag] = parse_children(children)
    return all_bags


def has_eligible_children(child_bags, eligible_bags):
    return any([child_bag for child_bag in child_bags if child_bag in eligible_bags])


def check_children_for_eligible_bags(bags, all_bags, eligible_bags=[]):
    for bag in bags:
        child_bags = all_bags[bag]
        print(f'Current Bag: {bag} Children: {child_bags}')
        if bag == golden_bag:
            print(f'Do nothing because current bag is {bag}')
        elif len(child_bags) == 0:
            print(f'Do nothing because {bag} holds nothing')
        elif bag in eligible_bags:
            print(f'Do nothing because {bag} is already in eligible bags')
        else:
            if golden_bag in child_bags:
                eligible_bags.append(bag)
                print(f'Added {bag} to eligible bags: {eligible_bags}')
            eligible_bags = check_children_for_eligible_bags(child_bags, all_bags, eligible_bags)
            if has_eligible_children(child_bags, eligible_bags) and bag not in eligible_bags:
                eligible_bags.append(bag)
                print(f'Added {bag} to eligible bags: {eligible_bags}')
    return eligible_bags


def search_for_eligible_number_of_shiny_bag_carriers():
    all_bags = parse_rule_file('inputs/7_bag_rules.txt')
    print(f'All Bags: {all_bags}')
    eligible_bags = check_children_for_eligible_bags(all_bags, all_bags)
    count = len(eligible_bags)
    print(f'There are {count} eligible bags for {golden_bag}')


search_for_eligible_number_of_shiny_bag_carriers()
