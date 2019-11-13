package sorting

import (
	"math/rand"
	"testing"
	"time"
)

type algorithm func([]int) []int

func benchmarkSort(b *testing.B, n int, fn algorithm) {
	items := make([]int, n)
	rand.Seed(time.Now().UnixNano())
	for i := 0; i <= n-1; i++ {
		items[i] = -100 + rand.Intn(200)
	}
	fn(items)
}

func BenchmarkBubbleSort(b *testing.B) {
	benchmarkSort(b, 1000, BubbleSort)
}

func BenchmarkInsertSort(b *testing.B) {
	benchmarkSort(b, 1000, InsertionSort)
}

func BenchmarkSelectionSort(b *testing.B) {
	benchmarkSort(b, 1000, SelectionSort)
}
