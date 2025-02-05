class Solution:
    def maskPII(self, s: str) -> str:
        # if s is a string
        if "@" in s:
            
            name,domain=s.lower().split("@")
            # print(name[0])
            # for ch in name[0]:
            masked_name=""
            
            masked_name=name[0]+"*****"+name[-1]
            masked_email=masked_name+"@"+domain
                
            return masked_email
        
        masked_pno=[ch for ch in s if ch.isdigit() ]
        masked_pno="".join(masked_pno)
        last_four=masked_pno[-4:]
        masked=""
        if len(masked_pno)==10:
            return "***-***-"+last_four

        elif len(masked_pno)==11:
            return "+*-***-***-"+last_four

        elif len(masked_pno)==12:
            return "+**-***-***-"+last_four
        elif len(masked_pno)==13:
            return "+***-***-***-"+last_four
            
        # if s.isdigit():
        #     separation_chars=['+', '-', '(', ')', ' ']
        #     masked_pno=[]
        #     for ch in s:
        #         if ch not in separation_chars:
        #             masked_pno.append(ch)
          
        #     masked=""    
        #     if len(masked_pno)==10:
        #         masked+= "***-***-"+masked_pno[10-4:]

        #     if len(masked_pno)==11:
        #         masked+= "+" + "*-***-***-"+masked_pno[11-4:]

        #     if len(masked_pno)==12:
        #         masked+="+" + "**-***-***-"+masked_pno[12-4:]
        #     if len(masked_pno)==13:
        #         masked+="+" "***-***-***-"+masked_pno[13-4:]
        #     return masked


            

            
            








                