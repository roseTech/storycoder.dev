n_explorers = 8
fish_limit = 117
Fish = Struct.new(:big, :medium, :small)
explorers = Array.new(n_explorers) { Fish.new(0, 0, 0) }
fishes = {big: 19, medium: 11, small: 5}
sizes = [:big, :medium, :small]

fish = 0
expl_i = 0
while explorers.any? { |expl| expl.big < fish_limit || expl.medium < fish_limit || expl.small < fish_limit }
  size = sizes[fish % 3]
  fish_pieces = fishes[size]
  fish_pieces.times do
    explorers[expl_i][size] += 1
    expl_i = (expl_i + 1) % n_explorers
  end
  fish += 1
end

# fish fishes were needed
puts "big fishes: #{(fish + 2) / 3}", "medium fishes: #{(fish + 1) / 3}", "small fishes: #{fish / 3}"
