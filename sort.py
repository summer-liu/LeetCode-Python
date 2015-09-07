#Bubble Sort
def bubbleSort(items):
	for i in range(len(items)):
		for j in range(len(items) - i - 1):
			if items[j] > items[j+1]:
				items[j], items[j+1] = items[j+1], items[j]

#Insertion Sort
def insertionSort(items):
	for i in range(1, len(items)):
		j = i
		while j > 0 and items[j-1] > items[j]:
			items[j], items[j-1] = items[j-1], items[j]
			j -= 1
#Selection Sort
def selectionSort(items):
	for i in range(len(items)):
		minimum = i
		for j in range(i+1, len(items)):
			if items[j] < items[minimum]:
				minimum = j
		items[minimum], items[i] = items[i], items[minimum]


#Merge Sort
# def merge(left, right):
# 	result = [0] * (len(left) + len(right))
# 	l = r = 0
# 	for i in range(len(result)):
# 		lval = left[l] if l < len(left) else None
# 		rval = right[r] if r < len(right) else None
# 		if (lval and rval and lval < rval) or rval is None:
# 			result[i] = lval
# 			l += 1
# 		elif (lval and rval and lval >= rval) or lval is None:
# 			result[i] = rval
# 			r += 1
# 	return result

# def mergeSort(items):
# 	if len(items) < 2:
# 		return items
# 	mid = len(items) // 2
# 	return merge(mergeSort(items[:mid]), mergeSort(items[mid:]))
def mergesort( aList ):
  _mergesort( aList, 0, len( aList ) - 1 )
 
 
def _mergesort( aList, first, last ):
  # break problem into smaller structurally identical pieces
  mid = ( first + last ) // 2
  if first < last:
    _mergesort( aList, first, mid )
    _mergesort( aList, mid + 1, last )
 
  # merge solved pieces to get solution to original problem
  a, f, l = 0, first, mid + 1
  tmp = [None] * ( last - first + 1 )
 
  while f <= mid and l <= last:
    if aList[f] < aList[l] :
      tmp[a] = aList[f]
      f += 1
    else:
      tmp[a] = aList[l]
      l += 1
    a += 1
 
  if f <= mid :
    tmp[a:] = aList[f:mid + 1]
 
  if l <= last:
    tmp[a:] = aList[l:last + 1]
 
  a = 0
  while first <= last:
    aList[first] = tmp[a]
    first += 1
    a += 1



# #Quicksort
# def quicksort(items):
# 	if len(items) <= 1:
# 		return items
# 	left = []
# 	right = []
# 	pivotList = []
# 	pivot = items[len(items)//2]
# 	for i in items:
# 		if i < pivot:
# 			left.append(i)
# 		elif i > pivot:
# 			right.append(i)
# 		else:
# 			pivotList.append(i)
# 	left = quicksort(left)
# 	right = quicksort(right)
# 	return left + pivotList + right

def quicksort(items):
	quicksortHelper(items, 0, len(items) - 1 )
def quicksortHelper(array, start, end):
	if(start < end):
		split = partition(array, start, end)
		quicksortHelper(array, start, split - 1)
		quicksortHelper(array, split + 1, end)
def partition( aList, first, last ) :
	for i in range(first, last):
		if aList[i] <= aList[last]:
			swap(aList, i, first)
			first += 1
	swap(aList, first, last)
	return first

def swap( A, x, y ):
  	A[x],A[y]=A[y],A[x]

items = [43, 2,2,4 , 54, 23, 12, 4, 56, 44, 21, 7]
mergesort(items)
print(items)

