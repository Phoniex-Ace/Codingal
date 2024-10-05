class pair_elemets:

    def twoSum(self, nums , target):
        lookup = {}

        for i, num in enumerate(nums):
            if target - num  in lookup:
                return (lookup[target - num ], i )
            lookup[num] = i

value = int(input("Enter Sum for which you want to make this search: "))
print("index1=%d,index2=%d" % pair_elemets().twoSum((10,20,30,40,50,60,70),value))