surveys = File.new('inputs/6_test_surveys.txt', 'r')

is_inclusive = false
groups = []
result = surveys.reduce(0) do |total_of_yes_answers, survey|
    if survey == "\n"
        if is_inclusive
            # len(set(sum(group, [])))
            total_of_yes_answers += groups.flatten.uniq.count
        else
            total_of_yes_answers += groups.inject(:&).count
        end
        groups = []
    else
        groups.append(survey.strip.split(''))
    end
    total_of_yes_answers
end
puts(result)