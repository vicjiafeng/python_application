# python排序
___
### 1. 快速排序

```python
      def quick_sort(lst):     
          length = len(lst)
          great=[]
          small=[]
          if len(lst) <= 1:
              return lst
          else:
              pivot=lst[0]
              for element in lst[1:]:
                  if element < pivot:
                      small.append(element)
                  else:
                      great.append(element)
              #great=[element for element in lst[1:] if element > pivot]
              #small=[element for element in lst[1:] if element <= pivot]
              return quick_sort(small)+[pivot]+quick_sort(great)
```

### 2. 归并排序

```python
      def merge_sort(lst):
          def merge(left,right):
              result = []
              while left and right:
                  result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
              return result + left + right
          if len(lst) <= 1:
              return lst
          mid = len(lst) // 2
          return merge(merge_sort(lst[:mid]), merge_sort(lst[mid:]))
```

### 3. 冒泡排序

```python
      def bubble_sort(lst):
          for i in range(len(lst)-1):
              for j in range(len(lst)-1-i):
                  if lst[j] > lst[j+1]:
                      lst[j], lst[j+1] = lst[j+1], lst[j]
          return lst
```

### 4. 插入排序

```python
      def insert_sort(lst):
          for i in range(1,len(lst)):
              while i > 0 and lst[i-1] > lst[i]:
                  lst[i],lst[i-1]=lst[i-1],lst[i]
                  i -= 1
          return lst
```

### 5. 选择排序

```python
      def select_sort(lst):
          for i in range(len(lst)-1):
              k = i
              for j in range(i,len(lst)):
                  if lst[j] < lst[k]:
                      k = j
              lst[k], lst[i] = lst[i], lst[k]
          return lst
```

### 6. 猴子排序

```python
      def bogo_sort(lst):
          def bogo(lst):
              if len(lst)<2:
                  return True
              for  i in range(len(lst)-1):
                  if lst[i] > lst[i+1]:
                      return False
              return True
      while not bogo(lst):
          random.shuffle(lst)
      return lst
```
              
              
          
                      
