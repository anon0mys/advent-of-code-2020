groups = {}
total_of_yes_answers = 0
is_inclusive = False


def get_unique_set(group, is_inclusive):
    if is_inclusive:
        sum_of = sum(group, [])
        unique_set = set(sum_of)
    else:
        unique_set = set(group[0]).intersection(*group)
    return unique_set


surveys = open('inputs/6_surveys.txt', 'r')
group_id = 1
for survey in surveys:
    if survey == '\n':
        group = groups[group_id]
        unique_set = get_unique_set(group, is_inclusive)
        len_of_unique_set = len(unique_set)
        group_id += 1
        total_of_yes_answers += len_of_unique_set
    else:
        line = list(survey.strip())
        groups.setdefault(group_id, []).append(line)
print(total_of_yes_answers)
