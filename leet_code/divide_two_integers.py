class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        dividend_list = list(str(dividend))
        print(dividend_list)
        
        answer = ""
        
        current_index = 0
        counter = 0
        current_dividend_string = dividend_list[current_index]
        
        while current_index < len(dividend_list) - 1:
            #review first digit in divident list
            current_dividend_int =  int(current_dividend_string)
            
            if current_dividend_int < divisor: 
                if counter > 1: 
                    answer += "0"
                    counter += 1
                    current_index += 1
                current_dividend_string += dividend_list[current_index + 1]
    
                print("string", current_dividend_string)
                
            else:
                print("subtract here")
                counter = 0
                while current_dividend_int >= divisor:
                    current_dividend_int -= divisor
                    counter +=1
                    print("counter equals", counter)
                      
                answer += str(counter)
                print("subtracted answer so far", answer, "current_div", current_dividend_int)
                current_dividend_string = str(current_dividend_int)
                current_index += 1
            
            
            counter = 0
            print("index now:",current_index, "answer", answer,"\n")
    

        return int(answer)
        