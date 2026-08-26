class Solution:
    def intToRoman(self, num: int) -> str:
        romanNumerals = {
            1000: "M", 
            500: "D",
            100: "C",
            50: "L", 
            10: "X", 
            5: "V", 
            1: "I"
        }

        result = ""
        digit_places = [1000,100,10,1]   
        

        for index, place in enumerate(digit_places):
            digit = (num // place) % 10   #get the digits in regards with their places

            #Move by 5 or 10 depending on rule pattern based on the roman numerals layout
            if (digit == 9):
                result += romanNumerals[place] + romanNumerals[place * 10] 
            elif (digit == 4):
                result += romanNumerals[place] +romanNumerals[place *5]

            # rules for = and up by 5
            else:
                if(digit >= 5):
                    result += romanNumerals[place*5]
                    digit -= 5
                result += romanNumerals[place] * digit   #places for the digits repeats 

        return result
