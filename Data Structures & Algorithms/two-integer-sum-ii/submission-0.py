class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mymap = {}
        inverted_list = [target - num for num in numbers]
        for index, number in enumerate(numbers):
            if number in mymap:
                return [mymap[number]+1,index+1]
            inverted_num = target-number
            mymap[inverted_num] = index