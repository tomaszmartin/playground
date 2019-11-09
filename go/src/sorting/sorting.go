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

// InsertionSort sorts a slice of integers using insertion sort algorithm.
func InsertionSort(items []int) []int {
	// We consider first item sorted since there
	// is nothing to the left to compere it with.
	// That's why we start at 1 position.
	for i := 1; i < len(items); i++ {
		// Make a backward pass
		for j := i; j > 0; j-- {
			if items[j-1] > items[j] {
				// If previous item is bigger than current one than
				// swap places and keep checking them
				items[j-1], items[j] = items[j], items[j-1]
			} else {
				// When previous item is smaller than You know
				// that the rest must also be sorted
				// and can break the loop
				break
			}
		}
	}
	return items
}
