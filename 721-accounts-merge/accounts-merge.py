class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n=len(accounts)
        m= len(accounts[0])
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])

            return parent[x]

        def union(x,y):
            p1=find(x)
            p2=find(y)
            if p1==p2:
                return 
            parent[p2]=p1

        parent={}
        name_mail={}
        
        for acc in accounts:
            name=acc[0]
            for mail in acc[1:]:
                parent[mail]=mail
                name_mail[mail]=name

        for acc in accounts:
            first_mail=acc[1]
            for i in acc[2:]:
                union(first_mail,i)
        merged=defaultdict(list)
        for email in parent:
            root=find(email)
            merged[root].append(email)
        result=[]
        for root in merged:
            name=name_mail[root]
            result.append([name]+sorted(merged[root]))

        return result


        
        
        

                
    
         