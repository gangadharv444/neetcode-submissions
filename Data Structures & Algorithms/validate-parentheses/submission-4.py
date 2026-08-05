class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        
        st = []

        for i in range(n):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                st.append(s[i])
            else:
                
                if not st:
                    return False
                
                top = st[-1]
                op = s[i]
                if op == ')' and top != '(':
                    return False
                elif op == '}' and top != '{':
                    return False
                elif op == ']' and top != '[':
                    return False
                else:
                    st.pop()
                
        
        if not st:
            return True
        return False
