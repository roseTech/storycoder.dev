# Johann's Harp solution in Ruby
# Rubberduck.tech + human-edited
# 2023-02-14

# Factorzation function
# start = starting number; factor; iterate = loop count
def factorize(start, factor, iterate)
  result = start
  iterate.times do
    result *= factor
  end
  return result
end

# Round the result to 6 decimal places
puts format("%.6f", factorize(1.0, 2.0 ** (1.0 / 12.0), 12))
