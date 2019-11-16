package sorting

import (
	"math/rand"
	"sort"
	"testing"
	"time"
)

var nItems int = 7500

type algorithm func([]int) []int

func benchmarkSort(b *testing.B, n int, fn algorithm) {
	items := random(n)
	fn(items)
}

func reversed(n int) []int {
	items := make([]int, n)
	for i := 0; i < n; i++ {
		items[i] = n - i
	}
	return items
}

func random(n int) []int {
	items := make([]int, n)
	rand.Seed(time.Now().UnixNano())
	for i := 0; i <= n-1; i++ {
		items[i] = -100 + rand.Intn(200)
	}
	return items
}

func defaultSort(items []int) []int {
	sort.Ints(items)
	return items
}

func BenchmarkDefaultSort(b *testing.B) {
	benchmarkSort(b, nItems, defaultSort)
}

func BenchmarkBubbleSort(b *testing.B) {
	benchmarkSort(b, nItems, BubbleSort)
}

func BenchmarkSelectionSort(b *testing.B) {
	benchmarkSort(b, nItems, SelectionSort)
}

func BenchmarkInsertSort(b *testing.B) {
	benchmarkSort(b, nItems, InsertionSort)
}

func BenchmarkTestSort(b *testing.B) {
	benchmarkSort(b, nItems, TestSort)
}
