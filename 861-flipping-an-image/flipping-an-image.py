class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        output=[]
        for img in image:
            img.reverse()
        size=len(image)
        for i in range(size):
            for j in range(size):
                if image[i][j]==0:
                    image[i][j]=1
                else:
                    image[i][j]=0
            
        return image



                
            #     if i==0:
            #         i=1
            #     i=0
            #   print(img)
            
        #     for r in img:
        #         if r==0:
        #             r=1
        #         else:
        #             r=0
                
        #     output.append(img)
        # return output
                
            
    
        