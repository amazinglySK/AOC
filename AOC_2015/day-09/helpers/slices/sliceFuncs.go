package slices

func Includes(arr []string, el string) bool {
	for _, i := range arr {
		if i == el {
			return true
		}
	}
	return false
}

func EqualSlice(a, b []string) bool {
	if len(a) != len(b) {
		return false
	}
	for _, i := range b {
		// fmt.Println(i, b)
		if !Includes(a, i) {
			return false
		}
	}

	return true
}
