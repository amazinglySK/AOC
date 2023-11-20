package conns

import (
	"day-09/helpers/permut"
	"day-09/helpers/slices"
	"strconv"
	"strings"
)

type Connection struct {
	locations []string
	weight    int
}

func ParseConnections(routes []string) []Connection {
	connList := []Connection{}
	for _, route := range routes {
		routeSplit := strings.Split(route, " ")
		cities := []string{routeSplit[0], routeSplit[2]}
		score, _ := strconv.Atoi(routeSplit[len(routeSplit)-1])
		newConn := Connection{
			cities,
			score,
		}
		connList = append(connList, newConn)
	}
	return connList
}

func IsValidConn(conn []string, conns []Connection) (bool, *Connection) {
	for _, con := range conns {
		if slices.EqualSlice(conn, con.locations) {
			return true, &con
		}
	}
	return false, &Connection{}
}

func GetAllValidRoutes(conns []Connection, cities []string) [][]*Connection {
	routes := [][]*Connection{}
	for perm := range permut.GetPerms(cities) {
		path := []*Connection{}
		isPath := true
		for idx := range perm {
			if idx < 1 {
				continue
			}
			valid, connect := IsValidConn(perm[idx-1:idx+1], conns)
			if !valid {
				isPath = false
				continue
			} else {
				path = append(path, connect)
			}
		}
		if isPath {
			routes = append(routes, path)
		}
	}

	return routes

}

func GetMinPath(paths [][]*Connection) int {
	min := 0
	for i, path := range paths {
		sum := 0
		for _, conn := range path {

			sum += conn.weight
		}

		if i == 0 || sum < min {
			min = sum
		}
	}
	return min
}

func GetMaxPath(paths [][]*Connection) int {
	max := 0
	for i, path := range paths {
		sum := 0
		for _, conn := range path {

			sum += conn.weight
		}

		if i == 0 || sum > max {
			max = sum
		}
	}
	return max
}
