fun main() {

    val numbOfLily = 1.0
    val daysUntilFullMoon = 29
    var totalNumOfLily = numbOfLily

    for (i in 1..daysUntilFullMoon) {
        println("Day ${i}, There are ${totalNumOfLily} Lilies")
        totalNumOfLily = totalNumOfLily * 2
    }

    var lilyNum = 1
    var daysNum = 1

    while (daysNum <= 29) {
        println("On day ${daysNum}, there should be ${lilyNum} Lilies in the pond.")
        lilyNum = lilyNum * 2
        daysNum++
    }
}
