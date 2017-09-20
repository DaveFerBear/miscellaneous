def quicksort(myList, start, end):
  if start < end:
    # partition the list
    pivot = partition(myList, start, end)
    # sort both halves
    quicksort(myList, start, pivot-1)
    quicksort(myList, pivot+1, end)
  return myList

def partition(myList, start, end):
  pivot = myList[start][0]
  left = start+1
  right = end
  done = False
  while not done:
    while left <= right and myList[left][0] <= pivot:
      left = left + 1
    while myList[right][0] >= pivot and right >=left:
      right = right -1
    if right < left:
      done = True
    else:
      # swap places
      temp=myList[left]
      myList[left]=myList[right]
      myList[right]=temp
  # swap start with myList[right]
  temp=myList[start]
  myList[start]=myList[right]
  myList[right]=temp
  return right

def merge_meetings(meetings):
	sorted_meetings = quicksort(meetings, 0 , len(a)-1)
	new_meetings = [sorted_meetings[0]]

	for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
		
		last_meeting_start, last_meeting_end = new_meetings[-1]

		if last_meeting_end >= current_meeting_start:
			new_meetings[-1] = (last_meeting_start, max(last_meeting_end, current_meeting_end))
		else:
			new_meetings.append((current_meeting_start,current_meeting_end))

	return new_meetings			

a = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
print merge_meetings(a)