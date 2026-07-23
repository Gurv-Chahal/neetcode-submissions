class HistoryNode:

    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = HistoryNode(homepage)

    def visit(self, url: str) -> None:
        newPage = HistoryNode(url)

        # new page points backward to the current page
        newPage.prev = self.current

        # current page points forward to the new page
        self.current.next = newPage

        # move current to the newly visited page
        self.current = newPage

    def back(self, steps: int) -> str:

        for i in range (steps):

          # cannot move further back
          if self.current.prev is None:
            break
          
          # move back
          self.current = self.current.prev

        return self.current.url


    def forward(self, steps: int) -> str:
        
        for i in range(steps):
          
          # cannot move further forward
          if self.current.next is None:
            break

          # move forward
          self.current = self.current.next

        return self.current.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)