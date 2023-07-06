class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAlt = 0
        altgain = 0
        for i in gain:
            altgain += i
            maxAlt = max(maxAlt , altgain)
        return maxAlt
