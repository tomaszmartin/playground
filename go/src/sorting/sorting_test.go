package sorting

import (
	"math/rand"
	"testing"
	"time"
)

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

func BenchmarkBubbleSort(b *testing.B) {
	benchmarkSort(b, 5000, BubbleSort)
}

func BenchmarkSelectionSort(b *testing.B) {
	benchmarkSort(b, 5000, SelectionSort)
}

func BenchmarkInsertSort(b *testing.B) {
	benchmarkSort(b, 5000, InsertionSort)
}

func BenchmarkTestSort(b *testing.B) {
	benchmarkSort(b, 5000, TestSort)
}
