private val numberOfRounds = 3
private val expectedInput =
"""Princess Salad
Lady Purple
Madame Pumpkin
Mister Onion
Knight Tomato
Count Leek
Mister Carrot
Sir Potato"""

private val actualInput = listOf<String>(
"""Princess Salad
Lady Purple
Madame Pumpkin
Mister Onion
Knight Tomato
Count Leek
Mister Carrot
Sir Potato""",
"""Knight Tomato
Sir Potato
Lady Purple
Princess Salad
Count Leek
Madame Pumpkin
Mister Carrot
Mister Onion""",
"""Count Leek
Mister Onion
Knight Tomato
Mister Carrot
Lady Purple
Sir Potato
Madame Pumpkin
Princess Salad"""
)

fun main(args: Array<String>) {
    printExpectedCount(expectedInput)

    printActualCount(actualInput)
}

private fun printExpectedCount(input: String) {
    val veggies = input.split("\n")
    val veggiesToCount = mutableMapOf<String, Int>()
    for (round in 1..numberOfRounds) {
        for (veggie in veggies) {
            veggiesToCount.set(veggie, veggiesToCount.getOrDefault(veggie, 0) + 1)
        }
    }

    println("Expected veggies count:")
    println(veggiesToCount)
}

private fun printActualCount(input: List<String>) {
    val veggiesToCount = mutableMapOf<String, Int>()
    for (roundInput in input) {
        val veggies = roundInput.split("\n")
        var veggiesEntering = 1
        for (veggie in veggies) {
            veggiesToCount.set(veggie, veggiesToCount.getOrDefault(veggie, 0) + veggiesEntering)
            veggiesEntering++
        }
    }

    val sortedVeggiesToCount = veggiesToCount.toList().sortedBy { (_, v) -> v }.toMap()

    println("Actual veggies count:")
    println(sortedVeggiesToCount)
}