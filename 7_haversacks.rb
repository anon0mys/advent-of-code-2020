class Bag
  def initialize(name)
    @name = name
    @children = {}
  end

  def add_child(bag)
    @children[bag.name] = bag
  end

  def has_child(bag_name)
    p('stuff')
  end
end

class LuggageRules
  def initialize(filename)
    rules = File.readlines(filename, chomp: true)
    @bag_tree = create_bag_heirarchy(rules)
  end

  def create_bag_heirarchy(rules)
    rules.reduce do |parent_bag, rule|
      bag_name, child_bag_names = rule.split('contain')

    end
  end

  def find_bag(bag_name)
    if @bag_tree
      
  end
end

luggage = LuggageRules.new('inputs/7_test_rules.txt')
require 'pry'; binding.pry()
