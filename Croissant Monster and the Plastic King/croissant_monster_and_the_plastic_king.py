# some flags determining the exact rules
allow_picking_already_picked_roll = false
must_pick_another_roll = true
# strategy
try_minimizing_number_of_picked_rolls = false

found_counts = []

# count how often the right roll is picked
# after a given number of tries
# (the values will only be approximations of the probabilities)
n_reps = 10000
n_reps.times do
  # prepare the rolls
  rolls = Array.new(17, false)
  good_index = rand(rolls.length)
  rolls[good_index] = true

  all_rolls = (0...rolls.length).to_a
  removed_rolls = []
  picked_rolls = []
  last_picked_roll = -1
  n = 0
  while(n < rolls.length)
    # the rolls that are allowed to be picked
    available_rolls = all_rolls - removed_rolls
    unless allow_picking_already_picked_roll
      available_rolls -= picked_rolls
    end
    available_for_removal = available_rolls

    if must_pick_another_roll
      available_rolls -= [last_picked_roll]
    end
    break if available_rolls.empty?

    # pick a roll at random
    picked_roll = available_rolls.sample(1).first
    # if desired, pick a preferred roll instead
    if try_minimizing_number_of_picked_rolls
      interesting_rolls = available_rolls & picked_rolls
      unless interesting_rolls.empty?
        picked_roll = interesting_rolls.sample(1).first
      end
    end

    # check the result
    if rolls[picked_roll]
      found_counts[n] = 0 unless found_counts[n]
      found_counts[n] += 1
      break unless allow_picking_already_picked_roll
    end

    available_for_removal -= [picked_roll, good_index]
    picked_rolls << picked_roll
    last_picked_roll = picked_roll

    # remove a roll
    removed_roll = available_for_removal.sample(1).first
    removed_rolls << removed_roll

    n += 1
  end
end

puts "found after following number of tries:"
found_counts.each_with_index do |n, i|
  puts "#{i + 1}: #{(n.to_f * 100 / n_reps).round}%"
end
i50 = found_counts.find_index { |n| n.to_f >= n_reps / 2.0 }
puts "50% first reached at round #{i50 ? i50 + 1 : '-'}"
