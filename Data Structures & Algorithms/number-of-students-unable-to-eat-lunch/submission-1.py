class Solution:
    # optimal solution
    # Time - O(N), Space - O(1)
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        # counts [0] = students who prefer 0
        # counts [1] = students who prefer 1
        counts = [0,0]

        # count each prefernce
        for student in students:
            counts[student] += 1

        # process sandwiches in order
        for sandwich in sandwiches:

            # nobody remaining wants this sandwich
            if counts[sandwich] == 0:
                return counts[0] + counts[1]

            # 1 student takes this sandwich
            counts[sandwich] -= 1
        
        # every student recieved a sandwich
        return 0 