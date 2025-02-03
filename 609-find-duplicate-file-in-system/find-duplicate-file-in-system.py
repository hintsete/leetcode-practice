from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
    #    so first i want to separate the content which are within the round braces and store each one of them as an individual string in a list. then i want to create an empty set to track the uniquness of each content(the one inside a round braces). so if char not in unique_set:
    # unique_ser.add(char) else i want to map it to its own root directoryit belongs to and return a list containing  all similar content with their respective directory within the same list 
        content_map=defaultdict(list)
        for path in paths:
            part=path.split() 
            directory=part[0]
            for file in part[1:]:  
                file_name,content=file.split("(")
                content=content[:-1] 
                
                content_map[content].append(f"{directory}/{file_name}")
        return [group for group in content_map.values() if len(group)>1]


        