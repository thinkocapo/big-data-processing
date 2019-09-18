package main

import "fmt"
import "flag"
import "strconv"

var ip = flag.Int("flagname", 1234, "help message for flagname")

func main() {
	fmt.Printf("hello, world\n")
	ipstring := strconv.Itoa(*ip) // ip is int pointer

	fmt.Printf(ipstring)
}
