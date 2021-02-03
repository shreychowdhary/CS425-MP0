package main

import (
	"bufio"
	"fmt"
	"log"
	"net"
	"os"
)

func main() {
	if len(os.Args) != 4 {
		log.Fatal("Format should be ./node nodename serverip serverport")
	}
	nodeName := os.Args[1]
	serverAddress := os.Args[2] + ":" + os.Args[3]

	connection, err := net.Dial("tcp", serverAddress)
	if err != nil {
		log.Println(serverAddress)
		log.Fatal("Unable to connect to server")
	}

	fmt.Fprintf(connection, "%s\n", nodeName)

	stdinReader := bufio.NewReader(os.Stdin)
	for {
		text, err := stdinReader.ReadString('\n')
		fmt.Fprintf(connection, text)
		if err != nil {
			log.Fatal(err)
		}
	}
}
