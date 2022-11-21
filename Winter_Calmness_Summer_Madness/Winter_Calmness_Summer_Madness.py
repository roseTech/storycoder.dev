def main():
    import math

    TIME_END = 360

    def buses():
        """Count of passengers passing by in buses"""
        people_count_bus = 0
        increment_people = 2
        for minute in range(0, TIME_END + 1, 3):
            if minute > 0 and minute % 15 == 0:
                increment_people += 12
            people_count_bus += increment_people
        return people_count_bus

    def cars():
        """Count of people passing by in cars"""
        people_count_car = 0
        for minute in range(TIME_END + 1):
            if minute % 6 == 0:
                people_count_car += 5
            else:
                people_count_car += 1
        return people_count_car
        
    def walkers():
        """Count of walkers passing by"""
        people_count_walker = 0   
        for interval_number in range(math.ceil(TIME_END / 11)):
            if interval_number == math.floor(TIME_END / 11):
                for minute in range(1, (TIME_END % 11) + 1):
                    people_count_walker += minute
            else:     
                for minute in range(1, 12):
                    people_count_walker += minute
        return people_count_walker
    
    def people_passing_by():
        """Total count of people passing by"""
        #print(buses())
        #print(cars())
        #print(walkers())
        return buses() + cars() + walkers()

    print(people_passing_by())

main()