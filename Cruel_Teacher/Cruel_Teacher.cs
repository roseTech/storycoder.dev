Console.WriteLine("Solution with complexity O(n), n being the amount of students");
{
    var totalLateStudents = 10;
    var penaltyPerMinute = 7;

    var totalPenalty = 0;
    for(var i = 0 ; i < totalLateStudents ; i++)
    {
        totalPenalty += (i + 1) * penaltyPerMinute;
    }

    Console.WriteLine($"Total money earned: ${totalPenalty}");
}

Console.WriteLine("Solution with a complexity of O(1)");
{
    int totalTimeLate = totalLateStudents * (totalLateStudents + 1) / 2; // Sum of consecutive numbers formula
    totalPenalty = totalTimeLate * penaltyPerMinute;

    Console.WriteLine($"Total money earned: ${totalPenalty}");
}