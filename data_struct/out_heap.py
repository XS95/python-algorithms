class OurHeap:
  def __init__(self, items):
    self.heap = [None] # index 0 会被替换
    self.rank= {}
    for x in items:
      self.push(x)
    
  def __len__(self):
    return len(self.heap) - 1
  
  def push(self, x):
    assert x not in self.rank
    i = len(self.heap)
    self.heap.append(x) # 添加一个叶子节点
    self.rank[x] = i
    self.up(i)          # 插入节点上升(保持堆排序)

  def pop(self):
    root = self.heap[1]
    del self.rank[root]
    x = self.heap.pop() # 移除最后一个叶子结点
    if self:            # 堆非空
      self.heap[1] = x  # 最后一个节点变为跟节点
      self.rank[x] = 1
      self.down(1)      # 跟节点下降(保持排序)
    return root
  
  def up(self, i):
    x = self.heap[i]
    while i > 1 and x < self.heap[i//2]:
      self.heap[i] = self.heap[i//2]
      self.rank[self.heap[i//2]] = i
      i //= 2
    self.heap[i] = x # 找到了插入点
    self.rank[x] = i

  def down(self, i):
    x = self.heap[i]
    n = len(self.heap)
    while True:
      left = 2 * i  # 在二叉树中下降
      right = left + 1
      if right < n and self.heap[right] < x and self.heap[right] < self.heap[left]:
        self.heap[i] = self.heap[right]
        self.rank[self.heap[right]] = i # 提升右侧子节点
        i = right
      elif left < n and self.heap[left] < x:
        self.heap[i] = self.heap[left]
        self.rank[self.heap[left]] = i # 提升左侧子节点
        i = left
      else:
        self.heap[i] = x # 找到了插入点
        self.rank[x] = i
        break

  def update(self, old, new):
    i = self.rank[old] # 交换下标为 i 的元素
    del self.rank[old]
    self.heap[i] = new
    self.rank[new] = i
    if old < new:     # 保持堆排序
      self.down(i)
    else:
      self.up(i)
        
    