package sorting

import (
	"math/rand"
	"testing"
	"time"
)

func randomInt(min, max int) int {
	return min + rand.Intn(max-min)
}

func benchmarkBubbleSort(b *testing.B, n int) {
	items := make([]int, n)
	rand.Seed(time.Now().UnixNano())
	for i := 0; i <= n-1; i++ {
		items[i] = randomInt(-100, 100)
	}
	BubbleSort(items)
}

func BenchmarkBubbleSort10_000(b *testing.B) {
	benchmarkBubbleSort(b, 10_000)
}

func BenchmarkBubbleSort1_000(b *testing.B) {
	benchmarkBubbleSort(b, 1_000)
}
