package sorting

// BubbleSort sorts a slice of integers
// using bubble sort algorithm O(n^2).
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

// InsertionSort sorts a slice of integers
// using insertion sort algorithm O(n^2).
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

// SelectionSort sorts a slice of integers
// using selection sort algorithm O(n^2).
func SelectionSort(items []int) []int {
	for i := 0; i < len(items); i++ {
		min := i
		for j := i; j < len(items); j++ {
			if items[j] < items[min] {
				min = j
			}
		}
		items[i], items[min] = items[min], items[i]
	}
	return items
}

// TestSort sorts a slice of integers.
func TestSort(items []int) []int {
	if len(items) < 2 {
		return items
	}

	middleIx := len(items) / 2
	middleVal := items[middleIx]
	var less []int
	var greater []int
	var middle []int
	for i := 0; i < len(items); i++ {
		curr := items[i]
		if items[i] < middleVal {
			less = append(less, curr)
		} else if items[i] > middleVal {
			greater = append(greater, curr)
		} else {
			middle = append(middle, curr)
		}

	}

	less = TestSort(less)
	greater = TestSort(greater)
	less = append(less, middle...)
	items = append(less, greater...)
	return items
}
