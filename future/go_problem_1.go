package main

import "fmt"
import "flag"
import "strconv"


var flagvar int

func main() {
	fmt.Printf("hello, world\n")
	
	// 1
	// var ip = flag.Int("flagname", 1234, "help message for flagname") // integer pointer
	flag.IntVar(&flagvar, "flagname", 1234, "help message for flagname") // &flagvar

	// 2
	flag.Parse()

	// 3
	// flagString := strconv.Itoa(*ip)
	flagString := strconv.Itoa(flagvar)
	fmt.Printf(flagString)
}
