package main

import "fmt"

// Sort makes a copy of the slice and sorts it using bubble sort.
func Sort(items []int) []int {
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

func main() {
	unsorted := []int{1, 9, 7, 5, 2, 8, 6, 4, -10, -100}
	fmt.Println("Unsorted: ", unsorted)
	fmt.Println("Sorted: ", Sort(unsorted))
}
