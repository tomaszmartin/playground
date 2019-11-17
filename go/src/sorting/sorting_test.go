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

func testSort(t *testing.T, fn algorithm) {
	items := []int{1, 0, 0, 4, 90, 5, 13, 17, 2, -10, 100}
	sorted := []int{-10, 0, 0, 1, 2, 4, 5, 13, 17, 90, 100}
	got := fn(items)
	for i, v := range sorted {
		if v != got[i] {
			t.Errorf("Should get %d, but got %d", sorted, got)
		}
	}
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

func TestBubbleSort(t *testing.T) {
	testSort(t, BubbleSort)
}

func BenchmarkSelectionSort(b *testing.B) {
	benchmarkSort(b, nItems, SelectionSort)
}

func TestSelectionSort(t *testing.T) {
	testSort(t, BubbleSort)
}

func BenchmarkInsertSort(b *testing.B) {
	benchmarkSort(b, nItems, InsertionSort)
}

func TestInsertSort(t *testing.T) {
	testSort(t, BubbleSort)
}

func BenchmarkTestSort(b *testing.B) {
	benchmarkSort(b, nItems, TestSort)
}

func TestTestSort(t *testing.T) {
	testSort(t, BubbleSort)
}
