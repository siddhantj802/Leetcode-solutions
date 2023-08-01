class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0
        lenC = len(chars)

        while read < lenC:
            char = chars[read]
            count = 1

            while read+1 < lenC and chars[read + 1] == char:
                count += 1
                read += 1

            chars[write] = char
            write += 1


            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1 
            read += 1

        return write
