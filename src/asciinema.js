const STEP = 100; // 100ms, equivalent to 0.1 seconds
const BIO = `👋 Bio
 • Gnu Believer. Support it now.
 • Tux Cultist(We suck Windows).
 • Disciple of RTFM & STFW. Ps. ATFL(Ask The Fucking LLM)
`;

const CONTACT = `✉️ Contact me
 • Gmail - ■■■■■■■
   Please Sign the email with GPG.
 • Gvoice - ■■■■■■■
   Feel free to leave voice messages.
 • Telegram - ■■■■■■■
`;

function type(content) {
    return new Promise((resolve) => {
        let i = 0;
        function typeChar() {
            if (i < content.length) {
                process.stdout.write(content[i]);
                i++;
                setTimeout(typeChar, STEP);
            } else {
                resolve();
            }
        }
        typeChar();
    });
}

async function main() {
    await type(BIO);
    await type(CONTACT);
}

main();