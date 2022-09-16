class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        output = 0
        for substr in operations:
            if "+" in substr:
                output = output+1
            else:
                output = output - 1
        return output
        
