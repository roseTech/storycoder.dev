import Text.Printf

main = do
  let tempSeidon = 11.475 + 14.0
  let tempCelsius = tempSeidon / 1.37
  printf "%.2f\n" (tempCelsius :: Float)
