package main

import "fmt"
import "sorting"

func main() {
	unsorted := []int{1, 9, 7, 5, 2, 8, 6, 4, -10, -100}
	fmt.Println("Unsorted: ", unsorted)
	fmt.Println("Sorted: ", sorting.BubbleSort(unsorted))
}