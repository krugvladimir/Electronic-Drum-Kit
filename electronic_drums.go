// electronic_drums.go — Go версия

package main

import (
	"bufio"
	"fmt"
	"os"
	"os/exec"
	"runtime"
	"strings"
	"time"
)

type Drum struct {
	name string
	freq int
}

var drums = map[string]Drum{
	"1": {"Бас", 80},
	"2": {"Снэр", 200},
	"3": {"Хай-хэт", 1000},
	"4": {"Том 1", 150},
	"5": {"Том 2", 120},
	"6": {"Райд", 800},
	"7": {"Крэш", 600},
	"8": {"Перкуссия", 400},
}

func playSound(freq, duration int) {
	switch runtime.GOOS {
	case "windows":
		cmd := exec.Command("powershell", "-Command", fmt.Sprintf("[System.Console]::Beep(%d, %d)", freq, duration))
		cmd.Run()
	default:
		cmd := exec.Command("beep", "-f", fmt.Sprintf("%d", freq), "-l", fmt.Sprintf("%d", duration))
		cmd.Run()
	}
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Println("\x1b[36m🥁 Electronic Drum Kit (Go)\x1b[0m")
	fmt.Println("Клавиши для игры:")
	fmt.Println("  [1] Бас   [2] Снэр   [3] Хай-хэт")
	fmt.Println("  [4] Том1  [5] Том2   [6] Райд")
	fmt.Println("  [7] Крэш  [8] Перк")
	fmt.Println("Нажмите q для выхода")

	for {
		fmt.Print("\x1b[33m> \x1b[0m")
		input, _ := reader.ReadString('\n')
		input = strings.TrimSpace(strings.ToLower(input))
		if input == "q" {
			break
		}
		if drum, ok := drums[input]; ok {
			fmt.Printf("Играем %s\n", drum.name)
			// Имитация реверберации
			for i := 0; i < 3; i++ {
				playSound(drum.freq+int(float64(drum.freq)*0.02*float64(i)), 30)
				time.Sleep(10 * time.Millisecond)
			}
		} else {
			fmt.Println("Неизвестная команда.")
		}
	}
}
