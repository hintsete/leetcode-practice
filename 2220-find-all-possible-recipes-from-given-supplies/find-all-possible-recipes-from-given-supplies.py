class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # supplies = set(supplies)
        
        queue = deque(supplies)
        graph = defaultdict(list)
        incoming = defaultdict(int)
        for idx, recipe in enumerate(recipes):
            incoming[recipe] = len(ingredients[idx])
            for ingred in ingredients[idx]:
                graph[ingred].append(recipe)
        ans = []
        # queue.append(supplies)
        while queue:
            node = queue.popleft()
            if node in graph:
                for neigh in graph[node]:
                    incoming[neigh] -= 1
                    if incoming[neigh] == 0:
                        ans.append(neigh)
                        queue.append(neigh)
        return ans
        