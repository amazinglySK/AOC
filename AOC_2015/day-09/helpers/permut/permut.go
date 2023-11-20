package permut

func swap(arr []string, i, j int) {
	arr[i], arr[j] = arr[j], arr[i]
}

func GetPerms(arr []string) <-chan []string {
	c := make(chan []string)
	go func(c chan []string) {
		defer close(c)

		perms(c, len(arr), arr)
	}(c)
	return c
}

func perms(c chan []string, k int, arr []string) {
	if k == 1 {
		c <- arr
	} else {
		perms(c, k-1, arr)

		for i := 0; i < k-1; i++ {
			if k%2 == 0 {
				swap(arr, i, k-1)
			} else {
				swap(arr, 0, k-1)
			}
			perms(c, k-1, arr)
		}
	}
}
