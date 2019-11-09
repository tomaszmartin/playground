package main

import (
	"fmt"
	"sorting"
)

func main() {
	unsorted := []int{30, 1, 9, 7, 5, 2, 8, 6, 4, -10, 20, -100, 15}
	fmt.Println("Unsorted: ", unsorted)
	fmt.Println("Sorted: ", sorting.InsertionSort(unsorted))
}
