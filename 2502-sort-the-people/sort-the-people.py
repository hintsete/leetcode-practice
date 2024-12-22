class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        max_number=max(heights)
        count=[0]*(max_number+1)
        height_to_names={}
        # populating the count array and the height_to_names dctionary
        for height,name in zip(heights,names):
            count[height]+=1
            if height not in height_to_names:
                height_to_names[height]=[]

            height_to_names[height].append(name)
        # Rearragneging

        sorted_array=[]
        for height in range(max_number,-1,-1):
            if count[height]>0:
                sorted_array.extend(height_to_names[height])

            
        return sorted_array

        
        