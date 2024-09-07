package main

import (
	"fmt"
	"time"
)

const (
	STEP = 100 * time.Millisecond // 100ms, equivalent to 0.1 seconds
)

var (
	BIO = `👋 Bio
 • Gnu Believer. Support it now.
 • Tux Cultist(We suck Windows).
 • Disciple of RTFM & STFW. Ps. ATFL(Ask The Fucking LLM)
`

	CONTACT = `✉️ Contact me
 • Gmail - ■■■■■■■
   Please Sign the email with GPG.
 • Gvoice - ■■■■■■■
   Feel free to leave voice messages.
 • Telegram - ■■■■■■■
`
)

func typeContent(content string) {
	for _, char := range content {
		fmt.Print(string(char))
		time.Sleep(STEP)
	}
}

func main() {
	typeContent(BIO)
	typeContent(CONTACT)
}
