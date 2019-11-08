package sorting

// BubbleSort sorts a slice using bubble sort algorithm.
func BubbleSort(items []int) []int {
	sortedPositions := 0
	cnt := 0

	for !(sortedPositions == len(items)) {
		for i := 0; i < len(items)-sortedPositions-1; i++ {
			if items[i] > items[i+1] {
				items[i], items[i+1] = items[i+1], items[i]
			}
			cnt++
		}
		// At this point the last item has to be sorted
		// either is was the biggest
		// or switched positions earlier
		sortedPositions++
	}
	return items
}
