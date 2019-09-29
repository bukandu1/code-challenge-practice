class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        #listify string
        #loop and replace all '.' with [.]

        """
        str_list = list(address)
        
        for i in range(len(str_list)):
            if str_list[i] == '.':
                str_list[i] = '[.]'
        print(str_list)
        
        return ''.join(str_list)
        """

    # Alternative
        return address.replace('.', '[.]')

    # Runtime: 36 ms, faster than 64.89% of Python3 online submissions for Defanging an IP Address.
    # Memory Usage: 13.9 MB, less than 100.00 % of Python3 online submissions for Defanging an IP Address.
