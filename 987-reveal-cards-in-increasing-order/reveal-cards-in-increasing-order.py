class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        res=[0]*len(deck)
        queue=deque()
        for i in range(len(deck)):
            queue.append(i)
        for num in deck:
            idx=queue.popleft()
            res[idx]=num
            if queue:
                queue.append(queue.popleft())


      

        return res
        