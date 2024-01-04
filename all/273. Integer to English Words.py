# 273. Integer to English Words

# Convert a non-negative integer num to its English words representation.

class Solution:
    def numberToWords(self, num: int) -> str:
        levels = [
            '',
            'Thousand',
            'Million',
            'Billion'
        ]

        numbers = [
            '',
            'One',
            'Two',
            'Three',
            'Four',
            'Five',
            'Six',
            'Seven',
            'Eight',
            'Nine',
            'Ten',
            'Eleven',
            'Twelve',
            'Thirteen',
            'Fourteen',
            'Fifteen',
            'Sixteen',
            'Seventeen',
            'Eighteen',
            'Nineteen'
        ]

        tens = [
            'Twenty',
            'Thirty',
            'Forty',
            'Fifty',
            'Sixty',
            'Seventy',
            'Eighty',
            'Ninety'
        ]

        def process(st, i):
            sub_result = ''
            lower_two = st % 100
            if lower_two < 20:
                sub_result = numbers[lower_two]
            else:
                tens_num = lower_two // 10
                ones_num = lower_two % 10
                sub_result = tens[tens_num - 2] + ' ' + numbers[ones_num] if numbers[ones_num] else tens[tens_num - 2]
            
            hundreds_num = st // 100
            if hundreds_num > 0:
                sub_result = numbers[hundreds_num] + ' Hundred ' + sub_result if sub_result else numbers[hundreds_num] + ' Hundred'
            
            return sub_result

        if num == 0:
            return 'Zero'
        
        i = 0
        result = ''
        while num:
            cur = num % 1000
            substr = process(cur, i)
            if substr:
                if i == 0:
                    result = substr
                else:
                    result = substr + ' ' + levels[i] + ' ' + result if result else substr + ' ' + levels[i]
            num = num // 1000
            i += 1
        
        return result
        