public class TypingSimulation {
    private static final long STEP = 100; // 100ms, equivalent to 0.1 seconds

    private static final String BIO = """
        👋 Bio
         • Gnu Believer. Support it now.
         • Tux Cultist(We suck Windows).
         • Disciple of RTFM & STFW. Ps. ATFL(Ask The Fucking LLM)
        """;

    private static final String CONTACT = """
        ✉️ Contact me
         • Gmail - ■■■■■■■
           Please Sign the email with GPG.
         • Gvoice - ■■■■■■■
           Feel free to leave voice messages.
         • Telegram - ■■■■■■■
        """;

    public static void typeContent(String content) throws InterruptedException {
        for (char c : content.toCharArray()) {
            System.out.print(c);
            System.out.flush();
            Thread.sleep(STEP);
        }
    }

    public static void main(String[] args) {
        try {
            typeContent(BIO);
            typeContent(CONTACT);
        } catch (InterruptedException e) {
            System.err.println("Typing was interrupted: " + e.getMessage());
        }
    }
}
