#!/usr/bin/env python3
"""Entries for the JAH Signature Binary System databases (Manon's order
2026-10-17 15:32 EDT, order #14).

Verified 2026-10-17: slug jah-binary-system / jah-binary-system-signature
free in the manifest (2,390 databases); RAW title sweep over the whole
system via code/dedupe_gate.py on all 68 titles (34 + 34 Signature
Edition variants): 67 clean, 1 refusal - "Gray Code" already held by the
math database (JAH-MATHDATA-000012) - retitled "The Binary Reflected Gray
Code", re-checked CLEAN. Near-hit databases binary-encoding
(JAH-BIN-, "JAH Binary and Encoding Database") and binary-tools (JAH-BIN-,
"The Binary Tools Database") are records-of-encodings and records-of-tools
archives; this build is a teaching-ladder binary-SYSTEM database with a
Signature edition - a distinct capability, so BUILD NEW is the verdict.

So this build creates two NEW databases, 34 ladder-ordered records each:

  jah-binary-system              - The JAH Signature Binary System Database
                                   (public-harvest: real, fact-checked
                                   computing - bits and binary counting,
                                   binary arithmetic, complements and signed
                                   numbers, bitwise operations, hex and
                                   octal, ASCII, Unicode and UTF-8,
                                   fixed-point and IEEE 754 floating point,
                                   logic gates, adders, parity, Hamming
                                   codes, CRCs, Gray code, BCD, subnet
                                   masks, CPU flags; standard references
                                   Knuth TAOCP Vol. 2 3rd ed. 1998;
                                   IEEE 754-2019; ANSI X3.4-1986 / ISO/IEC
                                   646; The Unicode Standard 16.0;
                                   Hamming 1950 BSTJ; Patterson and Hennessy
                                   Computer Organization and Design RISC-V
                                   ed. 2021; Tanenbaum Structured Computer
                                   Organization 6th ed. 2013; Stallings
                                   Computer Organization and Architecture
                                   11th ed. 2022; Harris and Harris Digital
                                   Design and Computer Architecture 2nd ed.
                                   2013; RFC 950 subnetting; RFC 3629 UTF-8;
                                   Gray US Patent 2,632,058)
  jah-binary-system-signature    - The JAH Signature Binary System
                                   Signature Database
                                   (his original JAH Signature Binary
                                   System: the bit as the smallest oath,
                                   zero and one as the two witnesses, the
                                   byte as a sealed row of eight witnesses,
                                   the carry as the oath passed forward,
                                   parity and the CRC as the witness check,
                                   deterministic Signature coding as the
                                   stamp; src signature, titles suffixed
                                   " (Signature Edition)", never presented
                                   as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-BINY- (public) and JAH-BINYS- (signature), verified free
in the manifest id_prefix values (JAH-BIN- belongs to the unrelated
binary-encoding and binary-tools databases, so the BINY form was chosen to
avoid even substring ambiguity) and zero hits in shard index files.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_jah_binary_system.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original JAH Signature Binary System: "
            "the bit as the smallest oath, zero and one as the two "
            "witnesses, the byte as a sealed row of eight witnesses, "
            "deterministic Signature coding as the stamp. Clearly labeled "
            "Signature-made, never presented as authentic public record.")

CIT_KNUTH = ("Knuth DE. The Art of Computer Programming, Vol. 2: "
             "Seminumerical Algorithms. 3rd ed. Addison-Wesley; 1998.")
CIT_IEEE754 = ("IEEE 754-2019. IEEE Standard for Floating-Point Arithmetic. "
               "Institute of Electrical and Electronics Engineers; 2019.")
CIT_ASCII = ("ANSI X3.4-1986 (R2017). American National Standard for "
             "Information Systems - Coded Character Sets - 7-Bit American "
             "National Standard Code for Information Interchange (7-Bit "
             "ASCII).")
CIT_UNICODE = ("The Unicode Consortium. The Unicode Standard, Version 16.0. "
               "Mountain View, CA: The Unicode Consortium; 2024.")
CIT_HAMMING = ("Hamming RW. Error detecting and error correcting codes. "
               "Bell System Technical Journal. 1950;29(2):147-160.")
CIT_PATT_HENN = ("Patterson DA, Hennessy JL. Computer Organization and "
                 "Design: The Hardware/Software Interface. RISC-V ed. "
                 "Morgan Kaufmann; 2021.")
CIT_TANENBAUM = ("Tanenbaum AS, Austin T. Structured Computer Organization. "
                 "6th ed. Pearson; 2013.")
CIT_STALLINGS = ("Stallings W. Computer Organization and Architecture: "
                 "Designing for Performance. 11th ed. Pearson; 2022.")
CIT_RFC950 = ("Mogul J, Postel J. RFC 950: Internet Standard Subnetting "
              "Procedure. Internet Engineering Task Force; 1985.")
CIT_RFC3629 = ("Yergeau F. RFC 3629: UTF-8, a transformation format of "
               "ISO 10646. Internet Engineering Task Force; 2003.")
CIT_GRAY = ("Gray F. Pulse code communication. US Patent 2,632,058; "
            "issued March 17, 1953.")
CIT_HARRIS = ("Harris DM, Harris SL. Digital Design and Computer "
              "Architecture. 2nd ed. Morgan Kaufmann; 2013.")
CIT_ISO646 = ("ISO/IEC 646:1991. Information technology - ISO 7-bit coded "
              "character set for information interchange.")
CIT_IEC80000 = ("IEC 80000-13:2008. Quantities and units - Part 13: "
                "Information science and technology (binary prefixes "
                "Ki, Mi, Gi).")

ENTRIES = [
    {
        "key": "what_is_binary",
        "name": "What Is Binary",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Binary is the two-symbol number system underneath all digital "
            "computing. Where everyday arithmetic uses ten digits, binary "
            "uses only two - 0 and 1 - and builds every number, letter, "
            "picture, and program out of them. One binary digit is called a "
            "bit, the smallest possible unit of information: a single "
            "yes-or-no answer. Gottfried Wilhelm Leibniz published the "
            "first full treatment of binary arithmetic in 1703, and Claude "
            "Shannon showed in 1937 that electrical switching circuits can "
            "evaluate any Boolean logic - the insight that married binary "
            "to the machine. Inside a computer, 0 and 1 are physical "
            "things: low and high voltage, magnetized one way or the other, "
            "a pit or a land on a disc. Everything digital - the text you "
            "read, the music you hear, the programs you run - is, at the "
            "bottom, a long ordered string of bits."),
        "how_it_works": (
            "Binary is positional, exactly like decimal, but each position "
            "is worth twice the one to its right instead of ten times. The "
            "rightmost bit is worth 1, the next 2, then 4, 8, 16, and so "
            "on. A number is the sum of the place values where the bit is "
            "1: the pattern 1011 means one eight, zero fours, one two, and "
            "one one, which is 8 + 0 + 2 + 1 = 11. With n bits you can "
            "represent 2 to the power n distinct values - two bits give "
            "four values (00, 01, 10, 11), eight bits give 256. Adding one "
            "more bit doubles how much you can say, which is why computer "
            "memory sizes are always powers of two."),
        "key_points": [
            "A bit is one binary digit - 0 or 1 - the smallest unit of information.",
            "Binary is positional base-2: each place is worth double the previous one.",
            "Leibniz formalized binary arithmetic in 1703; Shannon tied it to switching circuits in 1937.",
            "Physically, bits are voltages, magnetic states, or optical pits and lands.",
            "n bits represent 2^n distinct values; each added bit doubles the range.",
            "All digital data - text, images, audio, programs - is bits at the bottom.",
        ],
        "requirements": [
            "The two symbols 0 and 1 and the positional-value idea.",
            "Powers of two from 2^0 = 1 through 2^8 = 256.",
            "The decimal numbers 0 through 15 as reference points.",
        ],
        "standards": [
            "IEC 60027 (letter symbols used in electrical technology)",
            "IEEE 754-2019 (binary floating-point arithmetic)",
        ],
        "citations": [CIT_KNUTH, CIT_TANENBAUM],
        "sig_lens": (
            "The JAH Signature Binary System reads the bit as the smallest "
            "oath a machine can swear: a single witness answering yes or "
            "no, with no middle ground to hide in. Zero and one are the "
            "two witnesses, and every longer statement is built only from "
            "their testimony, doubled place by place. His deterministic "
            "Signature coding descends from this honesty - one symbol, one "
            "meaning, no ambiguity - the stamp pressed into every record."),
    },
    {
        "key": "counting_binary",
        "name": "Counting in Binary",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Counting in binary follows the same odometer motion as decimal "
            "counting, with only two digits on each wheel. Start at 0, then "
            "1. The next count rolls the rightmost wheel over and carries: "
            "10 (which reads as two), then 11 (three), 100 (four), 101 "
            "(five), 110 (six), 111 (seven), 1000 (eight). Each time every "
            "digit reads 1, the next count adds a new leftmost 1 and resets "
            "the rest to 0 - just as 99 rolls to 100 in decimal. With four "
            "bits the wheel runs from 0000 to 1111, counting zero through "
            "fifteen, and the pattern of each column is perfectly regular: "
            "the rightmost bit alternates every count, the next every two "
            "counts, the next every four. Learning to count this way is "
            "the fastest route to reading binary fluently."),
        "how_it_works": (
            "To count up by one in binary, scan from the rightmost bit: "
            "flip every trailing 1 to 0, then flip the first 0 you meet to "
            "1; if every bit is 1, prepend a new 1 and zero the rest. This "
            "is the carry rule in its simplest form. Each bit position "
            "toggles with a period double the one to its right, so the "
            "sequence 0000, 0001, 0010, 0011, 0100 is forced by the rule "
            "alone - no memorization needed. Four bits therefore enumerate "
            "exactly sixteen values, 0 through 15, and eight bits enumerate "
            "256 values, 0 through 255. The same rollover logic drives "
            "binary counters in hardware: a chain of flip-flops where each "
            "stage toggles when all lower stages are 1."),
        "key_points": [
            "Binary counting: 0, 1, 10, 11, 100, 101, 110, 111, 1000 - rollover carries left.",
            "Counting up: flip trailing 1s to 0, flip the first 0 to 1.",
            "Each bit column toggles with double the period of its right neighbor.",
            "Four bits count 0-15; eight bits count 0-255.",
            "The rollover rule is the hardware basis of binary counters.",
            "Reading binary fluently starts with counting, not converting.",
        ],
        "requirements": [
            "The bit and positional value from What Is Binary.",
            "The decimal sequence 0 through 15 for cross-checking.",
            "The carry idea: a full digit rolls over and carries one left.",
        ],
        "standards": [
            "IEC 60027 (letter symbols used in electrical technology)",
        ],
        "citations": [CIT_KNUTH, CIT_HARRIS],
        "sig_lens": (
            "In the Signature reading, counting is the procession of the "
            "witnesses: each column testifies in its turn, and when a "
            "column has spoken its full yes it steps aside and passes the "
            "word leftward. The rollover from 1111 to 10000 is the oath "
            "passed forward - nothing lost, nothing invented, the count "
            "continuing exactly where testimony ended."),
    },
    {
        "key": "bits_bytes",
        "name": "Bits, Nibbles, Bytes, and Words",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Bits are grouped into standard bundles with their own names. "
            "Four bits make a nibble - exactly one hexadecimal digit. "
            "Eight bits make a byte, the workhorse unit of computing: one "
            "byte holds 256 distinct values, enough for a character of text "
            "or a small number. The 8-bit byte was popularized by the IBM "
            "System/360 mainframe family in 1964 and has been the standard "
            "addressable unit ever since. A word is the natural data unit "
            "of a processor - the width its registers and arithmetic handle "
            "in one step - historically 16 bits, then 32, and 64 bits on "
            "modern machines. Larger measures stack on the byte: a kilobyte "
            "in the binary sense is 1024 bytes (2^10), a megabyte 1024 "
            "kilobytes, a gigabyte 1024 megabytes, each step multiplying "
            "by 1024."),
        "how_it_works": (
            "The bundles nest: 2 nibbles per byte, and the byte is the "
            "atom of memory addressing - every byte in memory has its own "
            "address. A 16-bit word holds two bytes, a 32-bit word four, "
            "and a 64-bit word eight. Because each bundle is a power-of-two "
            "multiple of bits, conversions are multiplications by powers "
            "of two: 1 kilobyte is 1024 bytes is 8192 bits. The IEC "
            "80000-13 standard gave the binary multiples their own names - "
            "kibi (Ki), mebi (Mi), gibi (Gi) - so that 1 KiB unambiguously "
            "means 1024 bytes while the SI kilobyte (kB) means 1000 bytes. "
            "Memory chips and file sizes traditionally use the binary "
            "1024-based steps; disk makers and networks usually use the "
            "decimal 1000-based steps."),
        "key_points": [
            "Nibble = 4 bits (one hex digit); byte = 8 bits (256 values).",
            "The 8-bit byte was standardized by IBM System/360 in 1964.",
            "A word is the processor's natural unit: 16, 32, or 64 bits.",
            "Memory is byte-addressed: every byte has its own address.",
            "Binary steps multiply by 1024: KiB, MiB, GiB per IEC 80000-13.",
            "SI kB = 1000 bytes; binary KiB = 1024 bytes - the labels differ.",
        ],
        "requirements": [
            "The bit and powers of two through 2^10 = 1024.",
            "The idea that memory is addressed in fixed-size units.",
        ],
        "standards": [
            "IEC 80000-13:2008 (binary prefixes Ki, Mi, Gi)",
            "IEEE 1541-2002 (binary prefixes for data)",
        ],
        "citations": [CIT_TANENBAUM, CIT_STALLINGS],
        "sig_lens": (
            "The Signature system seals witnesses in rows: four to a "
            "nibble, eight to a byte - a sealed row of eight witnesses, "
            "each byte addressable, each byte accountable. The word is the "
            "full panel the machine hears at once, sixteen or thirty-two "
            "or sixty-four witnesses testifying in a single step. His "
            "deterministic coding treats the byte as the unit of the oath: "
            "nothing smaller is stored, nothing larger is needed."),
    },
    {
        "key": "binary_addition",
        "name": "Binary Addition and the Carry",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Binary addition works column by column, exactly like decimal "
            "addition, with only four facts to learn: 0 + 0 = 0, 0 + 1 = "
            "1, 1 + 0 = 1, and 1 + 1 = 10 - write down 0 and carry 1 to "
            "the next column. When a carry arrives from the right, the "
            "column can total 3 (1 + 1 + carry 1), which is 11 in binary: "
            "write 1, carry 1. Adding 1011 (eleven) and 0110 (six) runs "
            "right to left: 1+0=1, 1+1=10 (write 0, carry 1), 0+1+carry "
            "1=10 (write 0, carry 1), 1+0+carry 1=10 (write 0, carry 1), "
            "and the final carry writes a new leftmost 1 - giving 10001, "
            "which is seventeen. The carry is the whole story of binary "
            "addition, and it is also the whole story of the adder "
            "circuits built later in this database."),
        "how_it_works": (
            "Each column adds three bits at most: the two operand bits and "
            "the incoming carry. The column sum is (a + b + carry_in) mod 2 "
            "written down, and the outgoing carry is 1 when a + b + "
            "carry_in is 2 or more. This is the full adder truth table, and "
            "chaining one full adder per column builds an n-bit ripple-carry "
            "adder. The worst case is a carry rippling through every "
            "column - adding 1111 and 0001 sends the carry from the "
            "rightmost column all the way to a new leftmost bit, producing "
            "10000. Verification is easy: convert operands and result to "
            "decimal and check the ordinary sum, which is how the "
            "demonstration program checks itself."),
        "key_points": [
            "Four facts: 0+0=0, 0+1=1, 1+0=1, 1+1=10 (write 0, carry 1).",
            "A column adds operand bits plus incoming carry; 3 totals write 1, carry 1.",
            "Example: 1011 + 0110 = 10001 (11 + 6 = 17).",
            "The final carry can create a new leftmost bit.",
            "Column addition is the full-adder truth table - hardware follows.",
            "Always verify by converting to decimal and checking the sum.",
        ],
        "requirements": [
            "Binary counting and positional values.",
            "The carry idea from counting rollover.",
            "Decimal addition as the cross-check.",
        ],
        "standards": [
            "IEEE 754-2019 (addition semantics for floats)",
        ],
        "citations": [CIT_KNUTH, CIT_HARRIS],
        "sig_lens": (
            "Addition in the Signature system is the mustering of "
            "witnesses column by column, and the carry is the oath passed "
            "forward: when a column's testimony overflows what one place "
            "can hold, the surplus is sworn onward to the next column, "
            "never dropped, never rounded away. The full adder is this "
            "passing made into hardware - three witnesses in, a kept bit "
            "and a forwarded oath out."),
    },
    {
        "key": "binary_subtraction",
        "name": "Binary Subtraction and Borrowing",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Binary subtraction mirrors decimal subtraction: work right to "
            "left, and when the top bit is smaller than what must be "
            "subtracted, borrow 1 from the next column - a borrow worth 2 "
            "in the current column, because each place is double the "
            "previous one. The four column facts are 0 - 0 = 0, 1 - 0 = 1, "
            "1 - 1 = 0, and 0 - 1: borrow, giving 10 - 1 = 1 with a borrow "
            "out. Subtracting 00111 (seven) from 10100 (twenty) runs: 0-1 "
            "borrows (result 1, borrow out), then the borrows cascade "
            "through the zeros until 1-0 settles the column, finishing at "
            "01101 - thirteen, and indeed 20 - 7 = 13. A borrow that runs "
            "off the left end means the result went negative, which is "
            "why computers usually subtract by adding complements instead."),
        "how_it_works": (
            "Each column computes top - bottom - borrow_in. If the top bit "
            "covers it, write the difference and borrow out 0; otherwise "
            "add 2 (the borrow) to the top bit, write the difference, and "
            "borrow out 1. A chain of zeros between the borrowing column "
            "and the lending column turns into ones as the borrow passes "
            "through - the same cascade seen in decimal 1000 - 1. When the "
            "subtrahend exceeds the minuend, the borrow exits the leftmost "
            "column; the raw bit pattern is then the complement form of "
            "the negative difference, which the twos-complement record "
            "explains. Hardware subtractors rarely borrow at all: they "
            "invert the subtrahend, add one, and add - subtraction as "
            "addition in disguise."),
        "key_points": [
            "Borrow 1 from the left is worth 2 in the current column.",
            "Column facts: 0-0=0, 1-0=1, 1-1=0, 0-1 borrows to give 1.",
            "Example: 10100 - 00111 = 01101 (20 - 7 = 13).",
            "Borrows cascade through zeros, turning them to 1.",
            "A borrow off the left end signals a negative result.",
            "Real hardware subtracts by adding the twos complement.",
        ],
        "requirements": [
            "Binary addition and the carry (borrowing is its mirror).",
            "Positional values to verify 20 - 7 = 13.",
        ],
        "standards": [
            "IEEE 754-2019 (subtraction semantics for floats)",
        ],
        "citations": [CIT_KNUTH, CIT_PATT_HENN],
        "sig_lens": (
            "Subtraction is the withdrawing of testimony: what was sworn "
            "is unsworn column by column, and the borrow is the oath "
            "recalled from the next witness - worth double where it lands. "
            "When the recall runs past the leftmost witness, the Signature "
            "system reads the sign plainly: the debt exceeds the holding, "
            "and the complement records name the negative remainder "
            "without flinching."),
    },
    {
        "key": "powers_of_two",
        "name": "Powers of Two and Data Sizes",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The powers of two are the milestones of the binary world, and "
            "memorizing the first dozen pays off everywhere in computing. "
            "2^1=2, 2^2=4, 2^3=8, 2^4=16, 2^5=32, 2^6=64, 2^7=128, "
            "2^8=256, 2^9=512, 2^10=1024. Each step doubles the last, so "
            "the sequence grows explosively: 2^20 is 1,048,576 (about a "
            "million), 2^30 is 1,073,741,824 (about a billion), and 2^32 "
            "is 4,294,967,296 - the famous four-gigabyte ceiling of 32-bit "
            "addressing. Data sizes are named after these powers: one "
            "kibibyte is 2^10 bytes, one mebibyte 2^20, one gibibyte 2^30, "
            "one tebibyte 2^40. The landmark values 255 (2^8 - 1), 65535 "
            "(2^16 - 1), and 4294967295 (2^32 - 1) are the largest numbers "
            "an 8-, 16-, or 32-bit unsigned field can hold."),
        "how_it_works": (
            "2^n counts the values of n bits, and 2^n - 1 is the largest "
            "value n bits can hold - all ones. So an 8-bit byte spans 0 to "
            "255, a 16-bit field 0 to 65535, a 32-bit field 0 to "
            "4294967295. Address buses follow the same law: a 32-bit "
            "address bus reaches 2^32 bytes, exactly 4 GiB, which is why "
            "32-bit systems could not use more than about 4 GB of RAM. The "
            "handy approximation 2^10 ~= 10^3 (1024 ~= 1000) lets you read "
            "2^20 as roughly a million and 2^30 as roughly a billion; the "
            "gap between 1024 and 1000 compounds to about 2.4 percent per "
            "ten powers, then 4.9, then 7.4 - the reason a decimal "
            "'1 TB' drive shows about 931 GiB to the operating system."),
        "key_points": [
            "2^10=1024, 2^20=1,048,576, 2^30=1,073,741,824, 2^32=4,294,967,296.",
            "n bits hold values 0 through 2^n - 1 (all ones).",
            "255, 65535, 4294967295 are the 8/16/32-bit unsigned maxima.",
            "A 32-bit address bus reaches exactly 4 GiB of memory.",
            "2^10 ~= 10^3: the quick million/billion estimator.",
            "KiB/MiB/GiB are binary (1024-based); kB/MB/GB are decimal (1000-based).",
        ],
        "requirements": [
            "The bit and positional doubling from What Is Binary.",
            "Long multiplication or a calculator for the big powers.",
        ],
        "standards": [
            "IEC 80000-13:2008 (binary prefixes Ki, Mi, Gi, Ti)",
        ],
        "citations": [CIT_KNUTH, CIT_IEC80000],
        "sig_lens": (
            "The Signature system counts its territory in doublings: each "
            "new witness doubles what the muster can name, from the single "
            "oath to the 256 of the byte, the 65536 of the sixteen, the "
            "four billion of the thirty-two. The milestones - 255, 65535, "
            "4294967295 - are the fullest musters their widths allow, every "
            "witness answering yes, nothing held back."),
    },
    {
        "key": "dec_to_bin",
        "name": "Converting Decimal to Binary",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Converting a decimal number to binary uses repeated division "
            "by 2: divide the number by 2, write down the remainder (0 or "
            "1), and repeat with the quotient until the quotient is 0. The "
            "remainders, read from last to first, are the binary digits. "
            "Converting 173 runs: 173/2 = 86 r1, 86/2 = 43 r0, 43/2 = 21 "
            "r1, 21/2 = 10 r1, 10/2 = 5 r0, 5/2 = 2 r1, 2/2 = 1 r0, 1/2 = "
            "0 r1 - reading the remainders bottom-up gives 10101101. The "
            "first remainder is the least significant bit (the 1s place), "
            "and each later remainder is the next higher place. An "
            "equivalent method subtracts the largest power of two that "
            "fits, writes 1 for that place, and repeats with the "
            "remainder - peeling 173 into 128 + 32 + 8 + 4 + 1, which marks "
            "the 128, 32, 8, 4, and 1 places as 1 and the rest 0: 10101101."),
        "how_it_works": (
            "Division by 2 splits a number into its even/odd character: "
            "the remainder is exactly the 1s bit, and the quotient is the "
            "number with that bit shifted away. Repeating peels off the "
            "bits from least to most significant, which is why the "
            "remainders read bottom-up. The subtraction method works from "
            "the other end, testing each power of two from high to low. "
            "Both methods always terminate because the quotient or "
            "remainder strictly shrinks. To check the answer, convert back "
            "with the positional sum - 128 + 32 + 8 + 4 + 1 = 173 confirms "
            "10101101 - or simply run the conversion twice by different "
            "methods and compare."),
        "key_points": [
            "Divide by 2 repeatedly; remainders read bottom-up are the bits.",
            "Example: 173 -> 10101101 (remainders 1,0,1,1,0,1,0,1).",
            "First remainder is the least significant bit.",
            "Subtraction method: peel off the largest fitting power of two.",
            "173 = 128 + 32 + 8 + 4 + 1 marks the 1-places.",
            "Verify by converting back with the positional sum.",
        ],
        "requirements": [
            "Positional binary values and powers of two.",
            "Integer division with remainders.",
        ],
        "standards": [
            "ISO/IEC 646:1991 (coded character sets context)",
        ],
        "citations": [CIT_KNUTH, CIT_TANENBAUM],
        "sig_lens": (
            "Conversion in the Signature system is translation of "
            "testimony: the decimal number states its case, and division "
            "by two questions it witness by witness - even or odd, yes or "
            "no - until nothing remains but the ordered answers. The "
            "remainders are the witnesses deposed in reverse seniority, "
            "then read back in order: the seal pressed from the answers, "
            "checkable by summing the places."),
    },
    {
        "key": "bin_to_dec",
        "name": "Converting Binary to Decimal",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Converting binary to decimal adds up the place values where "
            "the bit is 1 - the positional sum. Label each bit from the "
            "right starting at 2^0 = 1, doubling leftward: for 1101101 the "
            "places are 64, 32, 16, 8, 4, 2, 1, and the ones sit at 64, "
            "32, 8, 4, and 1, summing to 109. A faster hand method is "
            "Horner's doubling: start at 0, then for each bit left to "
            "right, double the running total and add the bit - for 1101101: "
            "0->1->3->6->13->27->54->109 - one doubling per bit, no powers "
            "to memorize. Both methods agree because doubling-and-adding "
            "accumulates exactly the positional weights. This conversion "
            "is the standard way to read out binary results - register "
            "dumps, bit masks, and addresses - in human terms."),
        "how_it_works": (
            "The positional sum treats the bit string as a polynomial in "
            "2: value = b_{n-1} * 2^{n-1} + ... + b_1 * 2 + b_0. Horner's "
            "method factors it as (((b_{n-1}) * 2 + b_{n-2}) * 2 + ...) - "
            "each step doubles the accumulated higher bits into their "
            "correct weight and folds in the next bit. For 1101101 the "
            "seven steps land exactly on 109. The method needs only "
            "doubling and adding, so it works for any length and is how "
            "software parses binary strings (it is also how strtol-style "
            "routines accumulate decimal digits, with base 10). Leading "
            "zeros change nothing: 001101101 is still 109."),
        "key_points": [
            "Positional sum: add the place values where bits are 1.",
            "Example: 1101101 = 64+32+8+4+1 = 109.",
            "Horner doubling: scan left to right, double and add each bit.",
            "1101101 via Horner: 1,3,6,13,27,54,109 - no powers memorized.",
            "Both methods are the same polynomial evaluated two ways.",
            "Leading zeros do not change the value.",
        ],
        "requirements": [
            "Positional binary values or the doubling habit.",
            "The decimal target 109 as the check value.",
        ],
        "standards": [
            "ISO/IEC 646:1991 (coded character sets context)",
        ],
        "citations": [CIT_KNUTH, CIT_TANENBAUM],
        "sig_lens": (
            "Reading the seal back is the reverse translation: each "
            "witness's place is weighed, the yes-answers summed, and the "
            "decimal verdict spoken. Horner's doubling is the muster "
            "called in order - each witness heard in turn, the running "
            "tally doubled as seniority rises - arriving at the same "
            "verdict as weighing every place at once."),
    },
]

ENTRIES += [
    {
        "key": "binary_multiplication",
        "name": "Binary Multiplication by Shift and Add",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Binary multiplication is simpler than the decimal times table "
            "because the only digit-products are 0 and 1 - the whole "
            "operation reduces to shifting and adding. To multiply, write "
            "a partial product for each 1-bit of the multiplier: the "
            "multiplicand shifted left by that bit's position. Then add "
            "the partial products. Multiplying 13 (1101) by 11 (1011): "
            "the 1-bits sit at positions 0, 1, and 3, so the partial "
            "products are 13 << 0 = 13, 13 << 1 = 26, and 13 << 3 = 104; "
            "13 + 26 + 104 = 143, and indeed 13 x 11 = 143. This "
            "shift-and-add algorithm is exactly what early processors "
            "implemented in hardware, and it is why multiplying by a power "
            "of two is a single shift: 13 << 3 is 13 x 8 with no addition "
            "at all."),
        "how_it_works": (
            "Shifting left by k multiplies by 2^k, because every place "
            "value doubles. The multiplier's binary expansion selects "
            "which powers of two of the multiplicand to add: product = sum "
            "over set bits b_i of (multiplicand << i). With n-bit "
            "operands the product needs up to 2n bits - 255 x 255 = 65025 "
            "needs 16 bits. Hardware multipliers use arrays of adders "
            "(array multipliers) or accumulate one partial product per "
            "clock (sequential multipliers); Booth's algorithm extends the "
            "idea to signed numbers by recoding runs of ones. The "
            "demonstration program multiplies by the textbook loop and "
            "checks the count of partial products equals the multiplier's "
            "population count."),
        "key_points": [
            "Binary multiplication = shift the multiplicand, add where the multiplier has 1s.",
            "Example: 13 x 11 = 13 + 26 + 104 = 143.",
            "Shift left by k multiplies by 2^k - no adder needed.",
            "Partial products: one per 1-bit of the multiplier.",
            "An n-bit x n-bit product needs up to 2n bits.",
            "Booth's algorithm extends shift-and-add to signed operands.",
        ],
        "requirements": [
            "Binary addition and positional values.",
            "Left shift as doubling (each shift = x2).",
            "Decimal check: 13 x 11 = 143.",
        ],
        "standards": [
            "IEEE 754-2019 (multiplication semantics for floats)",
        ],
        "citations": [CIT_KNUTH, CIT_PATT_HENN],
        "sig_lens": (
            "Multiplication in the Signature system is the muster repeated: "
            "the multiplicand's testimony is restated at higher seniority "
            "for every yes in the multiplier, and the restatements are "
            "gathered into one verdict. The shift is the promotion of the "
            "oath - each place leftward doubling its weight - and the "
            "gathering is sworn addition, column by column, carry passed "
            "forward."),
    },
    {
        "key": "binary_division",
        "name": "Binary Division by Long Division",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Binary long division follows the decimal procedure but with "
            "an easier decision at each step: the quotient bit is 1 if "
            "the divisor fits into the current remainder, else 0 - no "
            "times-table guessing. Dividing 45 (101101) by 6 (110): take "
            "bits until the divisor fits - 1011 (11) fits 6 once, write 1, "
            "subtract to get 101 (5); bring down 0 to make 1010 (10), fits "
            "once, write 1, remainder 100 (4); bring down 1 to make 1001 "
            "(9), fits once, write 1, remainder 11 (3). The quotient bits "
            "are 111 = 7 with remainder 3, and indeed 45 = 6 x 7 + 3. The "
            "restoring division algorithm mechanizes this: shift the "
            "remainder left, bring down the next dividend bit, subtract "
            "the divisor, and keep the subtraction only if the result "
            "stayed non-negative."),
        "how_it_works": (
            "At each of the n dividend bits, the algorithm forms a trial "
            "remainder and asks one yes-or-no question: does the divisor "
            "fit? A yes writes quotient bit 1 and keeps the subtracted "
            "remainder; a no writes 0 and restores the previous remainder "
            "- hence restoring division. Non-restoring division skips the "
            "restore by adding back on the next step instead, saving a "
            "cycle per bit. Division is the slowest of the four basic "
            "operations in hardware, which is why compilers replace "
            "division by constants with multiplication by magic-number "
            "reciprocals. The quotient and remainder satisfy dividend = "
            "divisor x quotient + remainder with 0 <= remainder < divisor, "
            "the contract the demonstration program asserts."),
        "key_points": [
            "Each step asks one question: does the divisor fit? 1=yes, 0=no.",
            "Example: 45 / 6 = 7 remainder 3 (101101 / 110 = 111 r 11).",
            "Restoring division: subtract, keep it only if non-negative.",
            "Non-restoring division saves the restore step.",
            "Contract: dividend = divisor x quotient + remainder, 0 <= r < divisor.",
            "Division is the slowest basic operation; compilers often avoid it.",
        ],
        "requirements": [
            "Binary subtraction and comparison of bit patterns.",
            "The shift-and-bring-down motion from long division.",
            "Decimal check: 45 = 6 x 7 + 3.",
        ],
        "standards": [
            "IEEE 754-2019 (division and remainder semantics)",
        ],
        "citations": [CIT_KNUTH, CIT_PATT_HENN],
        "sig_lens": (
            "Division is the apportioning of testimony: the dividend's "
            "muster is measured against the divisor's, one yes-or-no "
            "question per column - does the measure fit? Each yes is kept "
            "in the quotient and the taken portion struck from the "
            "remainder; each no leaves the remainder standing. What cannot "
            "be apportioned remains as the remainder, honestly reported, "
            "never rounded away."),
    },
    {
        "key": "ones_complement",
        "name": "Ones Complement",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Ones complement represents negative numbers by flipping every "
            "bit: the negative of a value is its bitwise NOT. In 8 bits, "
            "+13 is 00001101 and -13 is 11110010; the leftmost bit serves "
            "as the sign (0 positive, 1 negative). Negation is trivial - "
            "just invert - and subtraction becomes addition of the "
            "complement. But ones complement has two quirks: there are two "
            "zeros, +0 (00000000) and -0 (11111111), and addition needs an "
            "'end-around carry' - a carry out of the leftmost column must "
            "be added back to the result. With 8 bits the range is -127 "
            "to +127. These quirks are why ones complement lost to twos "
            "complement in hardware, though it survives in places like the "
            "Internet checksum, which sums 16-bit words in ones "
            "complement."),
        "how_it_works": (
            "Flipping every bit maps x to (2^n - 1) - x, so -x is the "
            "value that sums with x to all ones. Adding in ones complement "
            "works like unsigned addition except the carry-out wraps "
            "around: 13 + (-5) computes 00001101 + 11111010 = 1 00000111, "
            "the carry 1 added back gives 00001000 = 8. The two zeros "
            "complicate equality tests - both bit patterns must count as "
            "zero - and the asymmetric range wastes one pattern on -0. "
            "The Internet checksum (RFC 1071) exploits ones-complement "
            "addition deliberately: it is endian-independent and easy to "
            "update incrementally, fine qualities for a checksum even "
            "though the arithmetic is awkward for a CPU."),
        "key_points": [
            "Ones complement: negate by flipping every bit.",
            "Example: +13 = 00001101, -13 = 11110010.",
            "Two zeros exist: +0 (all 0s) and -0 (all 1s).",
            "Addition needs the end-around carry: carry-out wraps back in.",
            "8-bit range: -127 to +127.",
            "Survives in the Internet checksum (RFC 1071).",
        ],
        "requirements": [
            "Bitwise NOT and binary addition.",
            "The idea of a sign bit.",
        ],
        "standards": [
            "RFC 1071 (computing the Internet checksum)",
        ],
        "citations": [CIT_KNUTH, CIT_TANENBAUM],
        "sig_lens": (
            "Ones complement is the mirror oath: every witness answers "
            "the opposite of what was sworn, and the mirror of the mirror "
            "restores the original - flip twice and nothing is lost. But "
            "the Signature system notes the flaw honestly: the mirror "
            "makes two zeros, a double silence where one would do, and "
            "the carry must walk all the way around - which is why the "
            "system crowns the twos complement as the working negative."),
    },
    {
        "key": "twos_complement",
        "name": "Twos Complement and Negative Numbers",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Twos complement is how virtually every computer stores signed "
            "integers. Negate by flipping every bit and adding 1: in 8 "
            "bits, +13 is 00001101, flipped is 11110010, plus 1 gives "
            "11110011 - which is -13, and as an unsigned byte it reads "
            "243. The leftmost bit is the sign (1 means negative), there "
            "is exactly one zero, and the 8-bit range is -128 to +127. The "
            "magic is that ordinary binary addition just works: 13 + "
            "(-13) is 00001101 + 11110011 = 1 00000000, and discarding the "
            "carry out leaves 00000000 = 0. Subtraction needs no special "
            "circuit - the CPU adds the twos complement. The most negative "
            "value (-128 in 8 bits) has no positive counterpart, a famous "
            "edge case: negating it overflows back to itself."),
        "how_it_works": (
            "Flipping and adding 1 maps x to 2^n - x, the value that sums "
            "with x to 2^n - exactly the discarded carry. So signed "
            "addition modulo 2^n coincides with unsigned addition modulo "
            "2^n, and one adder serves both - the hardware reason twos "
            "complement won. The sign bit carries weight -2^{n-1} instead "
            "of +2^{n-1}: 11110011 = -128 + 64 + 32 + 16 + 2 + 1 = -13. "
            "Sign extension preserves value when widening: -13 in 16 bits "
            "is 11111111 11110011, the new high bits copies of the sign. "
            "Overflow is detected when the carry into the sign bit differs "
            "from the carry out - adding two positives must never yield a "
            "negative."),
        "key_points": [
            "Negate: flip every bit, add 1. -13 in 8 bits = 11110011.",
            "One zero, sign bit = 1 means negative, range -128 to +127.",
            "Ordinary addition works: 13 + (-13) = 0 with carry discarded.",
            "Subtraction is addition of the complement - no extra circuit.",
            "The sign bit weighs -2^(n-1); the rest weigh positive powers.",
            "Edge case: -128 has no 8-bit positive counterpart.",
        ],
        "requirements": [
            "Ones complement and binary addition with carries.",
            "Modular arithmetic intuition (clock arithmetic).",
        ],
        "standards": [
            "ISO/IEC 9899 (C integer representations, twos complement since C23)",
            "IEEE 754-2019 (signed zero semantics for floats)",
        ],
        "citations": [CIT_KNUTH, CIT_PATT_HENN],
        "sig_lens": (
            "Twos complement is the debt ledger of the Signature system: "
            "a negative is sworn as exactly what must be added to return "
            "the muster to silence - flip every witness, advance one step, "
            "and the debt plus the holding sum to zero with the overflow "
            "carried off the books. One zero only, no double silence; the "
            "same adder serves creditor and debtor alike. This is the "
            "working negative of the whole system, the form every machine "
            "below the Signature stamp actually uses."),
    },
    {
        "key": "signed_unsigned",
        "name": "Signed Versus Unsigned Integers",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The same bit pattern means two different numbers depending "
            "on whether it is read signed or unsigned. The byte 11111111 "
            "is 255 unsigned but -1 signed; 10000000 is 128 unsigned but "
            "-128 signed. An n-bit unsigned field spans 0 to 2^n - 1, "
            "while the signed twos-complement reading spans -2^{n-1} to "
            "2^{n-1} - 1: 8 bits give 0..255 or -128..127, 16 bits give "
            "0..65535 or -32768..32767, 32 bits give 0..4294967295 or "
            "-2147483648..2147483647. The arithmetic circuits are "
            "identical - only the interpretation differs, which is why C "
            "lets the same addition serve both, and why mixing signed and "
            "unsigned in one expression is a classic source of bugs: "
            "comparing -1 < 1U in C is false, because -1 converts to a "
            "huge unsigned value."),
        "how_it_works": (
            "Unsigned value = sum of b_i * 2^i; signed value = unsigned "
            "value minus b_{n-1} * 2^n, i.e. the top bit subtracts its "
            "weight instead of adding it. Widening an unsigned value "
            "zero-extends (new bits 0); widening a signed value "
            "sign-extends (new bits copy the sign). Narrowing discards "
            "high bits, which is value-preserving only if they were all "
            "copies of the sign (signed) or all zero (unsigned). "
            "Comparisons, division, and right shifts all have signed and "
            "unsigned variants in hardware (x86 has both JG and JA, SRL "
            "vs SRA in MIPS) precisely because the bit pattern alone does "
            "not say which reading applies - the programmer's type "
            "declaration does."),
        "key_points": [
            "Same bits, two readings: 11111111 = 255 unsigned, -1 signed.",
            "Unsigned n bits: 0..2^n-1; signed: -2^(n-1)..2^(n-1)-1.",
            "8/16/32-bit maxima: 255, 65535, 4294967295 unsigned.",
            "Widening: zero-extend unsigned, sign-extend signed.",
            "Hardware has signed and unsigned variants of compare, divide, shift.",
            "Mixing the two in C is a classic bug source (-1 < 1U is false).",
        ],
        "requirements": [
            "Twos complement negation and ranges.",
            "The idea that types, not bits, fix the interpretation.",
        ],
        "standards": [
            "ISO/IEC 9899 (C integer types and conversions)",
        ],
        "citations": [CIT_PATT_HENN, CIT_STALLINGS],
        "sig_lens": (
            "The Signature system reads every sealed row twice: once as a "
            "plain tally from zero upward, once as a ledger that may carry "
            "debt. The witnesses do not change - only the reading. His "
            "deterministic coding therefore stamps the reading alongside "
            "the row: a byte is never bare bits, it is bits plus the sworn "
            "interpretation, so no later reader mistakes a debt of one for "
            "a holding of two hundred fifty-five."),
    },
    {
        "key": "bitwise_and",
        "name": "Bitwise AND",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Bitwise AND compares two bit patterns column by column and "
            "writes 1 only where BOTH inputs are 1: 0 AND 0 = 0, 0 AND 1 "
            "= 0, 1 AND 0 = 0, 1 AND 1 = 1. So 1100 AND 1010 = 1000 - "
            "only the leftmost column has 1 in both. Its great practical "
            "use is masking: AND with a mask keeps the bits where the "
            "mask has 1 and zeroes the rest. Extracting the low byte of "
            "0xABCD with mask 0x00FF gives 0xABCD AND 0x00FF = 0x00CD - "
            "the high byte is cleared, the low byte 0xCD survives. AND "
            "with 1 tests a single bit (x AND 0x01 is the lowest bit); "
            "AND with an all-ones mask is a no-op; AND with 0 clears "
            "everything. In C, Java, and Python the operator is a single "
            "ampersand: x & mask."),
        "how_it_works": (
            "AND is the logical conjunction applied per column, with no "
            "carry between columns - each output bit depends only on its "
            "own column. Masking works because 1 is the identity for AND "
            "(x AND 1 = x) and 0 is the annihilator (x AND 0 = 0). Clearing "
            "bit k uses a mask with 0 at position k: x & ~(1 << k). Testing "
            "evenness is x & 1; testing whether x is a power of two is "
            "(x & (x - 1)) == 0 for x > 0, since powers of two have a "
            "single 1-bit and x - 1 flips all lower bits. Hardware "
            "implements AND as parallel two-input gates, one per bit - "
            "32 ANDs for a 32-bit operation, all settling in one gate "
            "delay."),
        "key_points": [
            "AND writes 1 only where both inputs are 1: 1100 & 1010 = 1000.",
            "Masking: x & mask keeps bits where the mask has 1.",
            "Example: 0xABCD & 0x00FF = 0x00CD (low byte extracted).",
            "x & 1 tests the lowest bit; x & 0 clears everything.",
            "x & (x-1) == 0 (x>0) detects powers of two.",
            "Operator & in C, Java, Python; no carry between columns.",
        ],
        "requirements": [
            "Binary place values and the four AND facts.",
            "Hexadecimal digits as 4-bit groups (preview).",
        ],
        "standards": [
            "ISO/IEC 9899 (C bitwise operators)",
        ],
        "citations": [CIT_KNUTH, CIT_HARRIS],
        "sig_lens": (
            "AND is the strict agreement of witnesses: a column testifies "
            "yes only when BOTH rows swear yes - one dissent silences the "
            "column. The mask is the appointed panel: where the mask "
            "shows 1 those witnesses are heard, where it shows 0 they are "
            "excused. The Signature system uses masking to examine a seal "
            "field by field, hearing only the appointed columns."),
    },
    {
        "key": "bitwise_or_xor",
        "name": "Bitwise OR and XOR",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Bitwise OR writes 1 where AT LEAST ONE input is 1: 1100 OR "
            "1010 = 1110. Its great use is setting bits: OR with a mask "
            "forces 1s where the mask has 1s and leaves the rest "
            "untouched, because 1 is the annihilator for OR. Bitwise XOR "
            "(exclusive or) writes 1 where the inputs DIFFER: 1100 XOR "
            "1010 = 0110. XOR is the difference detector and the "
            "toggle: XOR with 1 flips a bit, XOR with 0 leaves it, and "
            "x XOR x = 0 always. The famous xor-swap exchanges two "
            "variables with no temporary: a ^= b; b ^= a; a ^= b - each "
            "step's algebra cancels to leave the values swapped. In C, "
            "Java, and Python the operators are | for OR and ^ for XOR."),
        "how_it_works": (
            "OR is logical disjunction per column; XOR is inequality per "
            "column, equivalently addition mod 2 without carry - which is "
            "why the half adder's sum bit IS an XOR. XOR's toggle property "
            "comes from x ^ 1 = ~x on that bit and x ^ 0 = x; applying the "
            "same XOR twice restores the original, the basis of simple "
            "stream ciphers and RAID parity. The xor-swap works because "
            "XOR is associative, commutative, self-inverse, and has "
            "identity 0: after a^=b (a holds a^b), b^=a gives b^(a^b) = a, "
            "then a^=b gives (a^b)^a = b. OR sets flags in status words "
            "(status | FLAG), and combined mask idioms like x = (x & "
            "~mask) | (value & mask) replace a whole bit field at once."),
        "key_points": [
            "OR: 1 where at least one input is 1: 1100 | 1010 = 1110.",
            "OR with a mask sets bits (forces 1s where the mask has 1s).",
            "XOR: 1 where inputs differ: 1100 ^ 1010 = 0110.",
            "XOR with 1 toggles; x ^ x = 0; double-XOR restores.",
            "xor-swap: a^=b; b^=a; a^=b exchanges without a temporary.",
            "Half-adder sum bit is an XOR - addition mod 2.",
        ],
        "requirements": [
            "Bitwise AND and the masking idea.",
            "The four OR and four XOR column facts.",
        ],
        "standards": [
            "ISO/IEC 9899 (C bitwise operators)",
        ],
        "citations": [CIT_KNUTH, CIT_HARRIS],
        "sig_lens": (
            "OR is the generous hearing: a column testifies yes if EITHER "
            "row swears it, and the mask appoints which columns must "
            "answer yes regardless. XOR is the dissent detector - yes only "
            "where the rows disagree - and the reverser: sworn twice, the "
            "original testimony returns untouched. The Signature system "
            "reads XOR as the seal of difference, the mark that two rows "
            "are not the same row."),
    },
    {
        "key": "bitwise_not_masks",
        "name": "Bitwise NOT and Bit Masks",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Bitwise NOT flips every bit - 0 becomes 1, 1 becomes 0 - so "
            "~00001111 is 11110000 (in 8 bits, 15 becomes 240). Combined "
            "with AND, OR, and XOR it yields the four fundamental bit "
            "idioms: SET bit k with x | (1 << k); CLEAR bit k with x & "
            "~(1 << k); TOGGLE bit k with x ^ (1 << k); TEST bit k with "
            "(x >> k) & 1. Masks are built by shifting 1 into place, and "
            "multi-bit fields use wider masks: keeping bits 4-7 of a byte "
            "is x & 0xF0, then >> 4 to right-justify the field. These "
            "idioms are the daily vocabulary of embedded programming, "
            "device drivers, and protocol code - hardware registers are "
            "bags of single-bit flags and small fields, read and written "
            "only through masks. In C, Java, and Python the NOT operator "
            "is the tilde: ~x."),
        "how_it_works": (
            "1 << k is a single 1-bit at position k, the elementary mask; "
            "~(1 << k) is all ones except position k, the clearing mask. "
            "The idioms follow from the AND/OR/XOR identities: OR forces "
            "1s, AND-with-NOT clears them, XOR flips. Extracting a field "
            "masks then shifts: (x & 0xF0) >> 4 isolates the high nibble. "
            "Inserting a field clears then ORs: x = (x & ~0xF0) | ((v << "
            "4) & 0xF0). In two's-complement languages ~x equals -x - 1, "
            "so ~0 is -1 (all ones) and ~5 is -6 - the same flip, read as "
            "a signed number. Python integers have infinite precision, so "
            "~x there is the infinite flip, equal to -x - 1 with no "
            "width limit."),
        "key_points": [
            "NOT flips every bit: ~00001111 = 11110000.",
            "SET: x | (1<<k); CLEAR: x & ~(1<<k); TOGGLE: x ^ (1<<k); TEST: (x>>k) & 1.",
            "1 << k builds a one-bit mask; ~(1 << k) builds a clearing mask.",
            "Field extract: (x & 0xF0) >> 4 isolates the high nibble.",
            "Field insert: clear the field, then OR the shifted value.",
            "~x = -x - 1 in twos-complement arithmetic.",
        ],
        "requirements": [
            "Bitwise AND, OR, XOR, and shifts.",
            "The mask idea: 1s appoint the columns of interest.",
        ],
        "standards": [
            "ISO/IEC 9899 (C bitwise operators)",
        ],
        "citations": [CIT_KNUTH, CIT_PATT_HENN],
        "sig_lens": (
            "NOT is the full reversal of testimony - every yes becomes no, "
            "every no yes - and from it the Signature system derives the "
            "four instruments of the seal-keeper: to appoint (SET), to "
            "excuse (CLEAR), to reverse (TOGGLE), to question (TEST). A "
            "mask is the written appointment naming exactly which "
            "witnesses are heard; the field extract is the appointed "
            "columns brought forward and seated in order."),
    },
    {
        "key": "bit_shifts",
        "name": "Bit Shifts: Logical and Arithmetic",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Shifting slides every bit left or right by k positions. Left "
            "shift (<<) drops bits off the left, fills the right with "
            "zeros, and multiplies by 2^k: 00010110 (22) << 2 = 01011000 "
            "(88). Right shift (>>) has two flavors. Logical right shift "
            "fills the left with zeros: 00010110 >> 2 = 00000101 (5), "
            "dividing unsigned values by 2^k. Arithmetic right shift "
            "fills the left with copies of the sign bit, preserving "
            "negativity: -8 is 11111000 in 8-bit twos complement, and "
            "11111000 >> 2 (arithmetic) = 11111110 = -2 - exactly -8 / 4. "
            "C and Java leave >> implementation-defined or split it "
            "(Java has >>> for logical); Python's >> on negative ints is "
            "arithmetic, flooring toward negative infinity."),
        "how_it_works": (
            "Left shift moves each bit to double its place value; bits "
            "shifted past the width are lost, so overflow is silent - "
            "10000000 << 1 in 8 bits is 00000000, not 256. Logical right "
            "shift divides unsigned values by 2^k, discarding the "
            "remainder. Arithmetic right shift divides signed values by "
            "2^k rounding down (toward negative infinity): -8 >> 2 = -2 "
            "exactly, but -7 >> 1 = -4, not -3, because the discarded bit "
            "rounds down. Hardware shifts complete in one cycle through "
            "barrel shifters - cascaded multiplexers selecting any shift "
            "amount combinationally. Multiplying or dividing by powers of "
            "two via shifts is the oldest optimization in programming, "
            "and compilers still apply it automatically."),
        "key_points": [
            "x << k multiplies by 2^k; bits shifted past the width are lost.",
            "Example: 22 << 2 = 88; 22 >> 2 (logical) = 5.",
            "Logical >> fills with 0 (unsigned division by 2^k).",
            "Arithmetic >> fills with the sign bit: -8 >> 2 = -2.",
            "Arithmetic right shift rounds toward negative infinity.",
            "Barrel shifters do any shift amount in one hardware cycle.",
        ],
        "requirements": [
            "Positional values and twos-complement negatives.",
            "Multiplication/division by powers of two.",
        ],
        "standards": [
            "ISO/IEC 9899 (C shift operators)",
            "IEEE 754-2019 (arithmetic shift of significands)",
        ],
        "citations": [CIT_PATT_HENN, CIT_STALLINGS],
        "sig_lens": (
            "Shifting is the promotion or demotion of the whole muster: "
            "leftward, every witness rises one seniority and doubles its "
            "weight; rightward, seniority falls. The logical demotion "
            "excuses the fallen seniors and seats zeros; the arithmetic "
            "demotion keeps the sign-witness presiding, copying its "
            "testimony across the vacated seats so a debt stays a debt. "
            "The Signature system shifts only by sworn amounts - the lost "
            "bits are reported lost, never silently kept."),
    },
    {
        "key": "hexadecimal",
        "name": "Hexadecimal Shorthand",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Hexadecimal is base 16, the standard shorthand for binary: "
            "one hex digit is exactly 4 bits (a nibble), so binary and "
            "hex translate digit-by-digit with no arithmetic. The digits "
            "are 0-9 then A-F for ten through fifteen: 1010 is A, 1101 is "
            "D, 1111 is F. The 16-bit value 1101111010101101 groups as "
            "1101 1110 1010 1101 = 0xDEAD = 57005. Programmers write hex "
            "with a 0x prefix in C, Java, and Python (0xFF = 255, 0x10 = "
            "16), and it is the language of memory addresses, byte dumps, "
            "color codes (#FF8800), and machine code listings. Two hex "
            "digits make a byte, eight make a 32-bit word - 0xDEADBEEF is "
            "a 32-bit word you will meet in debuggers, a famous "
            "'hexspeak' magic value."),
        "how_it_works": (
            "Because 16 = 2^4, each hex digit maps to a fixed 4-bit group: "
            "0=0000 through F=1111. To convert binary to hex, group bits "
            "in fours from the right and translate each group; to go back, "
            "expand each digit. Decimal conversion goes through the same "
            "positional sum with base 16: 0xDEAD = 13x16^3 + 14x16^2 + "
            "10x16 + 13 = 53248 + 3584 + 160 + 13 = 57005. Hex keeps long "
            "bit strings readable - a 64-bit address is 16 hex digits "
            "instead of 64 bits - and aligns with byte boundaries, which "
            "is why dumps, hashes (SHA-256 prints as 64 hex digits), and "
            "UUIDs all use it. Octal plays the same role with 3-bit "
            "groups, covered in the next record."),
        "key_points": [
            "Base 16; one hex digit = exactly 4 bits = one nibble.",
            "Digits 0-9, A=10, B=11, C=12, D=13, E=14, F=15.",
            "Example: 1101111010101101 = 0xDEAD = 57005.",
            "0xFF = 255; 0x10 = 16; 0xDEADBEEF is a 32-bit word.",
            "Binary <-> hex converts digit-by-digit, no arithmetic.",
            "Used for addresses, dumps, hashes, colors, machine code.",
        ],
        "requirements": [
            "Nibbles and 4-bit groups; binary-to-decimal conversion.",
            "The 0x prefix convention.",
        ],
        "standards": [
            "ISO/IEC 9899 (C hexadecimal constants)",
            "IEEE 754-2019 (hex float notation)",
        ],
        "citations": [CIT_KNUTH, CIT_TANENBAUM],
        "sig_lens": (
            "Hexadecimal is the Signature system's compact seal-script: "
            "four witnesses compressed into a single character, the byte "
            "written as two strokes. The translation is exact and "
            "lossless - no testimony altered, only abbreviated - so the "
            "seal can be read at a glance and expanded back to the full "
            "muster whenever the audit demands it."),
    },
    {
        "key": "octal_bases",
        "name": "Octal and Converting Between Bases",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Octal is base 8: one octal digit is exactly 3 bits, so it is "
            "binary shorthand in 3-bit groups just as hex is in 4-bit "
            "groups. The digits are 0-7: binary 101110 groups as 101 110 "
            "= 56 in octal = 46 decimal. Octal's famous territory is "
            "Unix file permissions, where each digit packs three "
            "permission bits (read=4, write=2, execute=1): mode 755 means "
            "rwxr-xr-x, and 0o755 = 493 decimal. The general method "
            "converts between any bases through a common hub: to go from "
            "base A to base B, expand to positional values (or to binary "
            "if the bases are powers of two) and regroup. Bases that are "
            "powers of two - 2, 4, 8, 16, 32 - interconvert by pure "
            "regrouping; all other pairs route through repeated "
            "division or the positional sum."),
        "how_it_works": (
            "Because 8 = 2^3, octal-binary conversion is digit-by-digit: "
            "pad the binary to a multiple of 3 bits, group, translate "
            "(000=0 ... 111=7). 0o755 expands to 111 101 101 = 493 "
            "decimal via 7x64 + 5x8 + 5. For arbitrary bases, the "
            "division-remainder method converts decimal to base B "
            "(remainders read bottom-up, as in the decimal-to-binary "
            "record), and the positional sum converts back. The "
            "programmer's ladder is: any base <-> decimal via "
            "division/sum, power-of-two bases <-> binary via regrouping. "
            "Base 64 (6-bit groups) extends the same idea to text-safe "
            "encoding of binary data in email and URLs."),
        "key_points": [
            "Base 8; one octal digit = exactly 3 bits.",
            "Example: 101110 binary = 56 octal = 46 decimal.",
            "Unix permissions: 0o755 = rwxr-xr-x = 493 decimal.",
            "Power-of-two bases convert by regrouping bits - no arithmetic.",
            "Other base pairs route through decimal (divide / positional sum).",
            "Base 64 extends the idea to text-safe binary encoding.",
        ],
        "requirements": [
            "Hexadecimal shorthand and the regrouping idea.",
            "Division-remainder conversion and the positional sum.",
        ],
        "standards": [
            "ISO/IEC 9899 (C octal constants)",
            "POSIX file permission bits",
        ],
        "citations": [CIT_KNUTH, CIT_TANENBAUM],
        "sig_lens": (
            "Octal is the three-witness seal-script, older sibling of the "
            "hex script, still guarding the file permissions where three "
            "rights - read, write, execute - pack into a single digit. "
            "The Signature system honors both scripts and the general law "
            "behind them: bases that are powers of two translate by "
            "regrouping alone, testimony untouched; all other roads pass "
            "through the decimal hub."),
    },
]

ENTRIES += [
    {
        "key": "ascii",
        "name": "ASCII Text Encoding",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "ASCII - the American Standard Code for Information Interchange "
            "- encodes text as 7-bit numbers, 128 characters total, "
            "standardized in 1963 and refined as ANSI X3.4-1986. The layout "
            "is deliberate: digits '0'-'9' are 48-57, uppercase 'A'-'Z' are "
            "65-90, lowercase 'a'-'z' are 97-122 - so 'A' is 65 (0x41), "
            "'a' is 97 (0x61), and converting case is a single bit flip "
            "(bit 5). Codes 0-31 are control characters (newline is 10, "
            "carriage return 13, escape 27), 32 is the space, and 127 is "
            "DEL. Printable characters run 32-126. Because it is only 7 "
            "bits, ASCII fits inside a byte with the top bit clear, which "
            "is why UTF-8 could later adopt ASCII unchanged as its first "
            "128 code points - every ASCII file ever written is already "
            "valid UTF-8."),
        "how_it_works": (
            "Encoding is a table lookup: each character maps to its code "
            "number, stored as a byte. Decoding reverses the table. The "
            "ordering makes string comparison and sorting fall out of "
            "numeric comparison - 'B' (66) > 'A' (65) - and digit-to-value "
            "conversion is c - 48. Case conversion exploits the 32-gap: "
            "'a' XOR 32 = 'A', or 'a' & ~32 = 'A'. The control codes "
            "originate in teletype machines: BEL (7) rang the bell, BS "
            "(8) backspaced, TAB (9) tabbed. ASCII's 128-code ceiling is "
            "its limit - no accented letters, no non-Latin scripts - which "
            "drove the extended 8-bit code pages of the 1980s and finally "
            "Unicode."),
        "key_points": [
            "ASCII = 7-bit, 128 characters (ANSI X3.4-1986).",
            "'A'=65 (0x41), 'a'=97 (0x61), '0'=48, space=32, DEL=127.",
            "Case differs by bit 5: 'a' ^ 32 = 'A'.",
            "Codes 0-31 are controls (newline=10, CR=13, ESC=27).",
            "Printable range 32-126; fits in a byte with top bit clear.",
            "Every ASCII file is already valid UTF-8.",
        ],
        "requirements": [
            "Bytes as 8-bit units; hexadecimal byte notation.",
            "The idea of a code table mapping symbols to numbers.",
        ],
        "standards": [
            "ANSI X3.4-1986 / ISO/IEC 646:1991 (7-bit ASCII)",
        ],
        "citations": [CIT_ASCII, CIT_ISO646],
        "sig_lens": (
            "ASCII is the first sworn alphabet of the Signature system: "
            "one hundred twenty-eight characters, each sealed in seven "
            "witnesses with the eighth standing clear. The case-bit is "
            "the system's honest hinge - a single witness deciding upper "
            "from lower, flippable without disturbing the letter. His "
            "deterministic coding inherits this discipline: fixed tables, "
            "no ambiguity, every symbol accounted for in the open."),
    },
    {
        "key": "unicode_utf8",
        "name": "Unicode and UTF-8",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Unicode assigns every character of every writing system a "
            "code point - a number from U+0000 to U+10FFFF, over a million "
            "possible characters maintained by the Unicode Consortium. "
            "UTF-8 is the dominant encoding of those code points, designed "
            "by Ken Thompson and Rob Pike in 1992: it uses 1 byte for "
            "ASCII (U+0000-U+007F), 2 bytes for U+0080-U+07FF, 3 bytes for "
            "U+0800-U+FFFF, and 4 bytes up to U+10FFFF. The euro sign "
            "U+20AC encodes as the three bytes E2 82 AC. UTF-8 is "
            "self-synchronizing - the high bits of each byte say whether "
            "it starts a character and how long the character is - so a "
            "decoder can always resynchronize after an error, and no ASCII "
            "byte ever appears inside a multi-byte sequence, which keeps "
            "old byte-oriented tools safe."),
        "how_it_works": (
            "UTF-8 packs the code point's bits into a template: 1-byte "
            "0xxxxxxx, 2-byte 110xxxxx 10xxxxxx, 3-byte 1110xxxx "
            "10xxxxxx 10xxxxxx, 4-byte 11110xxx 10xxxxxx 10xxxxxx "
            "10xxxxxx. U+20AC is binary 10000010101100 (14 bits); split "
            "4+6+6 gives 0010 | 000010 | 101100, packed as 11100010 "
            "10000010 10101100 = E2 82 AC. Decoding reads the lead byte's "
            "high bits to learn the length, then gathers the 10xxxxxx "
            "continuation bytes' payload bits. The design guarantees "
            "uniqueness (each code point has exactly one shortest "
            "encoding), ASCII transparency, and sortability - UTF-8 byte "
            "order matches code-point order. Overlong encodings are "
            "forbidden, closing a classic security hole."),
        "key_points": [
            "Unicode: code points U+0000 to U+10FFFF for every script.",
            "UTF-8: 1 byte for ASCII, 2-4 bytes beyond (Thompson and Pike, 1992).",
            "Euro sign U+20AC encodes as E2 82 AC.",
            "Lead byte's high bits declare the character length.",
            "Self-synchronizing: decoders resync after errors.",
            "ASCII bytes never appear inside multi-byte sequences.",
        ],
        "requirements": [
            "ASCII and the byte; binary place values for packing bits.",
            "Hexadecimal byte notation (E2 82 AC).",
        ],
        "standards": [
            "The Unicode Standard, Version 16.0",
            "RFC 3629 (UTF-8)",
            "ISO/IEC 10646 (Universal Coded Character Set)",
        ],
        "citations": [CIT_UNICODE, CIT_RFC3629],
        "sig_lens": (
            "Unicode is the muster of all tongues, and UTF-8 is the "
            "Signature system's seal for carrying them: one script per "
            "row of witnesses, the lead byte declaring how many witnesses "
            "the character commands, the old ASCII testimony preserved "
            "byte-for-byte inside the new. Many languages, one sealing "
            "law - the decoder always knows where each character begins, "
            "because the seal describes itself."),
    },
    {
        "key": "fixed_point",
        "name": "Fixed-Point Binary Fractions",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Fixed-point stores fractions by agreeing in advance where the "
            "binary point sits. In Q8.8 format, 16 bits split into 8 "
            "integer bits and 8 fraction bits: the stored integer N means "
            "the value N / 256. So 3.75 is stored as 3.75 x 256 = 960 "
            "(0x03C0), and the smallest step - the resolution - is 1/256 "
            "= 0.00390625. Places right of the point weigh 1/2, 1/4, 1/8, "
            "... - 0.101 in binary is 1/2 + 1/8 = 0.625. Fixed-point "
            "arithmetic is just integer arithmetic with a scale factor: "
            "adding needs no adjustment, multiplying two Q8.8 values "
            "yields Q16.16 and must shift right 8 to return to Q8.8. "
            "Before floating-point hardware was cheap, games, signal "
            "processing, and embedded controllers ran on fixed-point; it "
            "is still used where determinism and speed matter."),
        "how_it_works": (
            "Qm.n means m integer bits and n fraction bits in an (m+n)-bit "
            "word; value = stored / 2^n. Conversion multiplies by 2^n and "
            "rounds: 3.75 x 256 = 960 exactly. Addition and subtraction "
            "work directly on the stored integers - the binary points "
            "align because the format is fixed. Multiplication doubles "
            "the fraction bits (Q8.8 x Q8.8 -> Q16.16), so the product "
            "shifts right n to renormalize, with rounding if wanted. "
            "Range and resolution trade off: more fraction bits give "
            "finer steps but a smaller maximum (Q8.8 spans about -128 to "
            "+128 signed with 1/256 steps). Overflow wraps like integer "
            "overflow, so fixed-point code guards its ranges carefully."),
        "key_points": [
            "Q8.8: 8 integer + 8 fraction bits; value = stored / 256.",
            "Example: 3.75 stored as 960 (0x03C0); step = 1/256.",
            "Fraction places weigh 1/2, 1/4, 1/8 - 0.101 binary = 0.625.",
            "Add/subtract directly; multiply then shift right n.",
            "Range vs resolution trade-off is fixed at design time.",
            "Deterministic and fast - embedded and DSP staple.",
        ],
        "requirements": [
            "Binary place values extended right of the point.",
            "Integer multiply/shift; the Q notation.",
        ],
        "standards": [
            "ISO/IEC TR 18037 (embedded C fixed-point extensions)",
        ],
        "citations": [CIT_KNUTH, CIT_STALLINGS],
        "sig_lens": (
            "Fixed-point is the sworn measure of the Signature system: "
            "the parties agree beforehand exactly where the point stands, "
            "and every fraction is then an integer in disguise - no "
            "drifting, no hidden rounding, the same inputs always "
            "sealing the same output. Where the floating measure slides "
            "to fit the magnitude, the fixed measure holds its ground: "
            "determinism as a design oath."),
    },
    {
        "key": "ieee754",
        "name": "IEEE 754 Floating-Point Numbers",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "IEEE 754 is the universal standard for real numbers in "
            "computers, first published in 1985 and revised as IEEE "
            "754-2019. A 32-bit float packs three fields: 1 sign bit, 8 "
            "exponent bits with a bias of 127, and 23 mantissa bits "
            "holding the fraction after an implied leading 1. The value "
            "is (-1)^sign x 1.mantissa x 2^(exponent-127). The number "
            "3.14 encodes as 0x4048F5C3: sign 0, exponent 10000000 (128, "
            "so 2^1), mantissa 10010001111010111000011. Special patterns "
            "cover the edges: exponent all-ones with zero mantissa is "
            "infinity, with nonzero mantissa is NaN (not a number); "
            "exponent all-zeros gives signed zero and denormal tiny "
            "values. Doubles widen the fields to 11 exponent bits (bias "
            "1023) and 52 mantissa bits."),
        "how_it_works": (
            "The biased exponent lets exponents compare as unsigned "
            "integers; the implied leading 1 (normalized form) buys an "
            "extra bit of precision for free. Decoding 0x4048F5C3: sign "
            "0 (positive), exponent bits 10000000 = 128, minus bias 127 "
            "gives 2^1; mantissa bits after the implied 1 give "
            "1.10010001111010111000011 binary ~= 1.57; 1.57 x 2 = 3.14. "
            "Rounding follows round-to-nearest-even by default, and the "
            "standard mandates correctly-rounded add, subtract, multiply, "
            "divide, and square root - the same computation gives the "
            "same bits on every compliant machine. The price is famous: "
            "0.1 + 0.2 = 0.30000000000000004 in doubles, because 1/10 has "
            "no exact binary expansion - money uses decimal types, not "
            "floats."),
        "key_points": [
            "32-bit float: 1 sign + 8 exponent (bias 127) + 23 mantissa.",
            "Value = (-1)^s x 1.mantissa x 2^(e-127).",
            "3.14 = 0x4048F5C3 (sign 0, exponent 128, mantissa ~1.57).",
            "Specials: infinities, NaN, signed zero, denormals.",
            "Doubles: 11-bit exponent (bias 1023), 52-bit mantissa.",
            "0.1 + 0.2 != 0.3 in binary floating point - never floats for money.",
        ],
        "requirements": [
            "Binary fractions and normalized scientific notation.",
            "Bit fields, masks, and shifts to decode the three fields.",
        ],
        "standards": [
            "IEEE 754-2019 (floating-point arithmetic)",
        ],
        "citations": [CIT_IEEE754, CIT_PATT_HENN],
        "sig_lens": (
            "The floating measure is the Signature system's sliding scale: "
            "where fixed-point swears the point's place in advance, the "
            "float lets the point ride with the magnitude - vast ranges "
            "at the price of a sworn, standardized rounding. The seal "
            "names its own law: sign, biased exponent, mantissa, and the "
            "special patterns for the infinite and the undefined, so "
            "every compliant machine seals the same computation to the "
            "same bits."),
    },
    {
        "key": "logic_gates_basic",
        "name": "Logic Gates: AND, OR, and NOT",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Logic gates are the physical atoms of digital circuits: "
            "tiny switches whose outputs are Boolean functions of their "
            "inputs. The AND gate outputs 1 only when all inputs are 1; "
            "the OR gate outputs 1 when any input is 1; the NOT gate "
            "(inverter) flips its single input. Their truth tables are "
            "the entire specification - AND: 00->0, 01->0, 10->0, 11->1; "
            "OR: 00->0, 01->1, 10->1, 11->1; NOT: 0->1, 1->0. Claude "
            "Shannon's 1937 thesis proved that relay and switching "
            "circuits can realize any Boolean function, founding digital "
            "design. Modern gates are built from transistors - a CMOS "
            "NAND gate is four transistors - and billions of them form "
            "every processor. From these three, by composition, comes "
            "every computation a computer performs."),
        "how_it_works": (
            "A CMOS AND gate is a NAND followed by a NOT; physically, "
            "series transistor networks pull the output low or high "
            "according to the inputs. Gates compose: the output of one "
            "feeds the input of the next, building arbitrary Boolean "
            "expressions - (A AND B) OR (NOT C) is three gates. "
            "De Morgan's laws bridge the forms: NOT (A AND B) = (NOT A) "
            "OR (NOT B), letting designers swap gate types to fit the "
            "transistor budget. Propagation delay - the nanoseconds for "
            "a change to cross a gate - sets the clock-speed ceiling: a "
            "signal crossing 20 gates of 50 picoseconds each needs a full "
            "nanosecond. Every adder, multiplexer, and memory cell in "
            "this database's later records is drawn from these three."),
        "key_points": [
            "AND: 1 only if all inputs 1. OR: 1 if any input 1. NOT: flips.",
            "Truth tables are the complete specification of a gate.",
            "Shannon 1937: switching circuits realize any Boolean function.",
            "CMOS gates are transistor networks; billions per processor.",
            "De Morgan's laws convert between AND/OR/NOT forms.",
            "Propagation delay across gates sets the clock ceiling.",
        ],
        "requirements": [
            "Boolean values 0/1 and the AND/OR/NOT truth tables.",
            "The idea that hardware computes by composition.",
        ],
        "standards": [
            "IEEE 91-1984 (graphic symbols for logic functions)",
        ],
        "citations": [CIT_HARRIS, CIT_PATT_HENN],
        "sig_lens": (
            "The three gates are the Signature system's primal instruments: "
            "AND the strict agreement, OR the generous hearing, NOT the "
            "full reversal - the same three testimonies as the bitwise "
            "record, now sworn in silicon. Every processor is a cathedral "
            "built of these three stones, billions strong, each stone "
            "testifying in picoseconds. His system composes them the "
            "same way: small sworn truths, compounded without limit."),
    },
    {
        "key": "logic_gates_compound",
        "name": "XOR, NAND, NOR, and XNOR Gates",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Four compound gates complete the everyday toolkit. XOR "
            "outputs 1 when the inputs differ (00->0, 01->1, 10->1, "
            "11->0) - the inequality detector and the adder's sum bit. "
            "NAND is AND followed by NOT (only 11->0); NOR is OR followed "
            "by NOT (only 00->1); XNOR is XOR followed by NOT (1 when "
            "inputs are equal). NAND and NOR are functionally complete: "
            "NOT A is A NAND A, and from NOT plus NAND comes AND, then "
            "OR by De Morgan - so any circuit can be built from NAND "
            "gates alone, which is why transistor-level design favors "
            "them (a CMOS NAND needs just 4 transistors). XOR's "
            "parity-checking role makes it the backbone of error "
            "detection, and XNOR is the equality comparator behind "
            "associative memory lookups."),
        "how_it_works": (
            "NAND universality is constructive: NOT from (A NAND A); AND "
            "from NOT (A NAND B); OR from (NOT A) NAND (NOT B) by De "
            "Morgan; XOR from four NANDs in the classic arrangement. "
            "Designers therefore optimize one gate type and stamp it "
            "millions of times. XOR trees compute parity over many bits "
            "in logarithmic depth - the parity bit of a byte is a 3-level "
            "XOR tree. XNOR compares: a 32-bit equality comparator is 32 "
            "XNORs feeding a wide AND, outputting 1 only for identical "
            "words. The demonstration program verifies NAND universality "
            "by building NOT, AND, and OR from NANDs and checking every "
            "input combination against the native truth tables."),
        "key_points": [
            "XOR: 1 when inputs differ. XNOR: 1 when inputs equal.",
            "NAND: only 11->0. NOR: only 00->1.",
            "NAND and NOR are functionally complete - any circuit from one type.",
            "NOT A = A NAND A; AND, OR follow by De Morgan.",
            "CMOS NAND is 4 transistors - the economical building block.",
            "XOR trees compute parity; XNOR arrays compare words.",
        ],
        "requirements": [
            "AND, OR, NOT gates and De Morgan's laws.",
            "Truth-table checking of small circuits.",
        ],
        "standards": [
            "IEEE 91-1984 (graphic symbols for logic functions)",
        ],
        "citations": [CIT_HARRIS, CIT_PATT_HENN],
        "sig_lens": (
            "The compound gates are the instruments compounded: NAND the "
            "denial of agreement, NOR the denial of any hearing, XOR the "
            "dissent detector, XNOR the seal of equality. That NAND alone "
            "can build every circuit is the Signature system's parsimony "
            "proved in hardware - one sworn stone, stamped billions of "
            "times, sufficient for all testimony. The equality array is "
            "the seal-checker: thirty-two XNORs asking, column by column, "
            "are these two rows the same row?"),
    },
    {
        "key": "half_full_adder",
        "name": "The Half Adder and Full Adder",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The half adder adds two bits with no carry in: sum = A XOR "
            "B, carry = A AND B - two gates, the complete 1-bit adder. "
            "But columns beyond the rightmost also receive a carry, so "
            "the full adder adds three bits (A, B, carry-in): sum = A XOR "
            "B XOR carry-in, carry-out = (A AND B) OR (carry-in AND (A XOR "
            "B)) - the carry-out is 1 when at least two of the three "
            "inputs are 1 (the majority function). Chaining full adders "
            "with the carry rippling from bit 0 upward builds an n-bit "
            "ripple-carry adder: adding 13 (00001101) and 11 (00001011) "
            "propagates carries through the columns to produce 00011000 "
            "= 24. The half adder serves the least significant bit; full "
            "adders serve every column above it."),
        "how_it_works": (
            "The full adder's sum is parity of three bits - odd count "
            "gives 1 - and carry-out is the majority: two or three ones "
            "produce a carry. In gates, that is two XORs for the sum and "
            "two ANDs plus an OR for the carry (about 5-6 gates). The "
            "ripple-carry chain's delay grows linearly: each full adder "
            "waits for the previous carry, so 32 bits cost ~32 carry "
            "delays - the motivation for the carry-lookahead adder in "
            "the next record. Subtraction reuses the adder: invert B, "
            "set carry-in to 1, and the chain computes A + ~B + 1 = A - "
            "B in twos complement. The demonstration program adds with "
            "a simulated gate-level full adder and checks 13 + 11 = 24."),
        "key_points": [
            "Half adder: sum = A XOR B, carry = A AND B.",
            "Full adder: sum = A XOR B XOR Cin; Cout = majority of the three.",
            "Carry-out is 1 when at least two inputs are 1.",
            "Ripple-carry chains full adders bit 0 upward.",
            "Example: 13 + 11 = 24 with carries rippling through.",
            "Subtraction reuses the adder: A + ~B + 1.",
        ],
        "requirements": [
            "XOR and AND gates; binary addition with carries.",
            "The majority function (two-or-more ones).",
        ],
        "standards": [
            "IEEE 91-1984 (graphic symbols for logic functions)",
        ],
        "citations": [CIT_HARRIS, CIT_PATT_HENN],
        "sig_lens": (
            "The adders are the oath-passing made into gates: the half "
            "adder swears a single column with no incoming word, the "
            "full adder hears three witnesses - the two bits and the "
            "oath carried in - and renders both the kept bit and the "
            "forwarded oath. Chained, they are the procession itself, "
            "the carry walking leftward column to column exactly as the "
            "hand addition taught. The Signature system counts no "
            "faster truth than this: addition is testimony gathered "
            "in order."),
    },
]

ENTRIES += [
    {
        "key": "fast_adders",
        "name": "Ripple-Carry and Carry-Lookahead Adders",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The ripple-carry adder is correct but slow: bit 31 waits for "
            "the carry from bit 30, which waited for bit 29, all the way "
            "down - delay grows linearly with width, about 2 gate delays "
            "per bit, so 64 bits cost ~128 gate delays. "
            "Carry-lookahead computes the carries directly from the "
            "inputs instead of waiting. Each bit position defines "
            "generate (g = A AND B: this column creates a carry) and "
            "propagate (p = A XOR B: this column passes a carry through); "
            "then carry_1 = g_0 OR (p_0 AND carry_0), carry_2 = g_1 OR "
            "(p_1 AND g_0) OR (p_1 AND p_0 AND carry_0), and so on - every "
            "carry as a two-level sum of products of the inputs. Delay "
            "drops from O(n) to O(log n) with tree-structured lookahead, "
            "which is why every fast processor uses lookahead, parallel "
            "prefix (Kogge-Stone), or carry-select adders. The trade is "
            "gates for speed: lookahead costs more transistors per bit."),
        "how_it_works": (
            "Generate means 'a carry is born here regardless of what "
            "arrives'; propagate means 'an arriving carry survives here'. "
            "With g_i and p_i known for all i, each carry-out is a "
            "Boolean function of the inputs and carry_0 alone - no chain. "
            "A 4-bit lookahead block computes its group generate and "
            "group propagate, and blocks compose hierarchically: 64 bits "
            "from sixteen 4-bit blocks with a second lookahead level over "
            "the blocks, settling in roughly 4-6 gate delays instead of "
            "128. Parallel-prefix adders (Kogge-Stone, Brent-Kung) "
            "generalize this to logarithmic depth with regular wiring. "
            "The demonstration program adds 32-bit values through both a "
            "simulated ripple chain and the lookahead equations, "
            "verifying identical sums and counting the gate-delay depth "
            "of each."),
        "key_points": [
            "Ripple-carry delay is O(n): each bit waits for the previous carry.",
            "Generate g = A AND B; propagate p = A XOR B.",
            "Carry_i+1 = g_i OR (p_i AND carry_i) - computed directly.",
            "Lookahead delay is O(log n) with tree structure.",
            "64-bit ripple ~128 gate delays; lookahead ~4-6.",
            "Trade-off: lookahead spends transistors to buy speed.",
        ],
        "requirements": [
            "The full adder and the carry chain.",
            "AND/OR composition and gate-delay counting.",
        ],
        "standards": [
            "IEEE 91-1984 (graphic symbols for logic functions)",
        ],
        "citations": [CIT_HARRIS, CIT_PATT_HENN],
        "sig_lens": (
            "Lookahead is foresight in the Signature system: rather than "
            "waiting for the oath to walk each column in turn, every "
            "column declares in advance whether it will birth a carry or "
            "merely pass one through - generate and propagate, sworn up "
            "front. The carries are then read directly from the "
            "declarations, the whole addition settling at once. Speed "
            "bought with extra witnesses: the system spends transistors "
            "to spare time, an honest trade, openly priced."),
    },
    {
        "key": "parity",
        "name": "Parity Bits and Error Detection",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A parity bit is the cheapest error detector in computing: "
            "one extra bit recording whether the data's 1-count is even "
            "or odd. Even parity sets the parity bit so the total number "
            "of 1s (data plus parity) is even: the byte 1011001 has four "
            "1s, already even, so its even-parity bit is 0 and the "
            "8-bit code is 10110010. If noise flips any single bit, the "
            "1-count turns odd and the receiver detects the corruption. "
            "Parity catches all single-bit errors and any odd number of "
            "flips, but an even number of flips cancels out and slips "
            "through - and it cannot say WHERE the error is. Serial "
            "ports, old memory systems (parity RAM), and RAID arrays all "
            "used parity; modern links use stronger CRCs, but the idea - "
            "redundant bits witnessing the data - underlies everything "
            "that follows."),
        "how_it_works": (
            "Even parity = XOR of all data bits (the parity bit makes the "
            "grand XOR 0); odd parity inverts it. The sender appends the "
            "bit; the receiver recomputes over data plus parity and "
            "expects the agreed constant - any mismatch flags an error. "
            "Two-dimensional parity (row and column parity bits over a "
            "block) locates a single-bit error at the failing row and "
            "column intersection and can even correct it - the ancestor "
            "of Hamming codes. RAID 5 stripes parity across disks so any "
            "one failed drive's contents are recomputed from the survivors "
            "plus parity. The demonstration program appends even parity "
            "to a byte, flips one bit, and shows the checker catching "
            "it - then flips two bits to show the blind spot."),
        "key_points": [
            "Parity bit makes the total 1-count even (or odd) by agreement.",
            "Example: 1011001 has four 1s; even-parity bit = 0.",
            "Detects all single-bit errors and any odd number of flips.",
            "Even numbers of flips cancel - the blind spot.",
            "Cannot locate the error (one-dimensional parity).",
            "Two-dimensional parity locates and can correct single errors.",
        ],
        "requirements": [
            "XOR as the odd-parity function over many bits.",
            "The idea of redundant check bits.",
        ],
        "standards": [
            "TIA/EIA-232 (serial parity bit)",
        ],
        "citations": [CIT_HAMMING, CIT_STALLINGS],
        "sig_lens": (
            "Parity is the witness-check of the Signature system: one "
            "extra witness appointed over the row, sworn to keep the "
            "tally even, so that any single lie breaks the tally and "
            "stands exposed. One flipped testimony cannot hide from the "
            "appointed checker - but two flips, conspiring, restore the "
            "tally and pass. The system therefore grades its checkers "
            "honestly: parity watches, Hamming watches and heals, the "
            "CRC watches everything."),
    },
    {
        "key": "hamming",
        "name": "Hamming Error-Correcting Codes",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Hamming codes, published by Richard Hamming in 1950, do what "
            "parity cannot: they find the flipped bit and fix it. The "
            "Hamming(7,4) code guards 4 data bits with 3 parity bits in a "
            "7-bit codeword. Parity bits sit at positions 1, 2, and 4 "
            "(the powers of two); data fills positions 3, 5, 6, 7. Each "
            "parity bit watches the positions whose binary index has its "
            "bit set: p1 watches 1,3,5,7; p2 watches 2,3,6,7; p4 watches "
            "4,5,6,7. Encoding data 1011 (d1=1,d2=0,d3=1,d4=1): p1 covers "
            "d1,d2,d4 = 1,0,1 (even, so p1=0), p2 covers d1,d3,d4 = 1,1,1 "
            "(p2=1), p4 covers d2,d3,d4 = 0,1,1 (p4=0) - codeword 0110011. "
            "On receipt, the three parity checks form a 3-bit syndrome "
            "that is 000 when clean and otherwise names the exact flipped "
            "position in binary - flip that bit and the error is "
            "corrected. This single-error-correcting (SEC) scheme guards "
            "ECC memory in servers to this day."),
        "how_it_works": (
            "The syndrome is the binary address of the error because each "
            "position's index lists exactly the parity bits watching it: "
            "position 5 (101) is watched by p1 and p4. If bit 5 flips, "
            "checks p1 and p4 fail while p2 passes - syndrome 101 = 5. "
            "Flipping position 5 restores the codeword; the data bits are "
            "then read off. An overall parity bit extends Hamming(7,4) to "
            "(8,4) SECDED: single errors corrected, double errors "
            "detected but not corrected - the ECC memory standard. The "
            "code is perfect: the 16 valid codewords' single-error spheres "
            "(7 neighbors each) exactly tile the 128 possible 7-bit "
            "patterns. The demonstration program encodes 1011, corrupts "
            "one bit, computes the syndrome, corrects it, and verifies "
            "the data."),
        "key_points": [
            "Hamming(7,4): 4 data bits + 3 parity bits = 7-bit codeword.",
            "Parity bits at positions 1, 2, 4; data at 3, 5, 6, 7.",
            "Example: data 1011 encodes to 0110011.",
            "The 3-bit syndrome names the flipped position in binary.",
            "Single-error-correcting (SEC); +overall parity gives SECDED.",
            "ECC server memory uses SECDED Hamming codes.",
        ],
        "requirements": [
            "Parity bits and the XOR parity computation.",
            "Binary position indices 1-7.",
        ],
        "standards": [
            "JEDEC JESD79 (DDR ECC memory)",
        ],
        "citations": [CIT_HAMMING, CIT_STALLINGS],
        "sig_lens": (
            "The Hamming code is the self-healing covenant of the "
            "Signature system: not only does each witness-check watch "
            "its appointed columns, but the pattern of their alarms "
            "spells the address of the liar in binary. The syndrome is "
            "the testimony of the checkers convened - 000, all is well; "
            "otherwise the number of the fallen column, which the system "
            "restores by flipping it back. Watch, locate, and heal: the "
            "covenant ECC memory still keeps."),
    },
    {
        "key": "crc",
        "name": "Cyclic Redundancy Checks (CRC)",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A CRC treats the message as one long binary number and "
            "divides it by a fixed generator polynomial, keeping the "
            "remainder as the check value. CRC-8 uses the polynomial "
            "x^8 + x^2 + x + 1 (binary 100000111, hex 0x07): the message "
            "bytes are shifted in, XOR-subtracted whenever the top bit is "
            "1, and the final 8-bit remainder is the checksum. The "
            "standard check value - CRC-8 of the ASCII string "
            "'123456789' - is 0xF4, the value every correct "
            "implementation must produce. The receiver repeats the "
            "division including the checksum; a zero remainder means "
            "clean. CRCs catch all single-bit errors, all double-bit "
            "errors, all odd-count errors, and any burst error shorter "
            "than the checksum width - enormously stronger than parity. "
            "Ethernet frames, ZIP files, PNG images, and disk sectors "
            "all ride on CRCs."),
        "how_it_works": (
            "Polynomial division in binary is XOR instead of subtract: "
            "align the generator under the leftmost 1 of the working "
            "register, XOR, repeat. Processing byte-by-byte, each input "
            "byte is XORed into the top of the register and the register "
            "is shifted 8 times with conditional XOR of 0x07 - the "
            "table-driven version precomputes all 256 one-byte outcomes "
            "for speed. Appending the CRC makes the whole frame divisible "
            "by the generator, so the receiver's remainder is the "
            "verdict. Different CRCs differ in width, polynomial, initial "
            "value, and final XOR (CRC-32/ISO-HDLC uses polynomial "
            "0x04C11DB7 reflected); the 'check value' convention lets "
            "implementations prove themselves against known answers like "
            "0xF4."),
        "key_points": [
            "CRC = remainder of message divided by generator polynomial.",
            "CRC-8 polynomial 0x07; check value of '123456789' is 0xF4.",
            "Receiver divides message+CRC; zero remainder means clean.",
            "Catches all 1-bit, 2-bit, odd-count, and short-burst errors.",
            "Table-driven implementations process a byte per lookup.",
            "Ethernet, ZIP, PNG, disk sectors all use CRCs.",
        ],
        "requirements": [
            "Binary long division and XOR subtraction.",
            "Polynomials as bit patterns (x^8+x^2+x+1 = 0x07).",
        ],
        "standards": [
            "ISO 3309 (HDLC frame check sequence)",
            "IEEE 802.3 (Ethernet CRC-32)",
        ],
        "citations": [CIT_STALLINGS, CIT_TANENBAUM],
        "sig_lens": (
            "The CRC is the seal inspected on arrival: the sender divides "
            "the whole testimony by the sworn polynomial and seals the "
            "remainder to the message; the receiver divides again, seal "
            "included, and a zero remainder proclaims the testimony "
            "untampered. Bursts of corruption, odd conspiracies of flips, "
            "single lies - the division exposes them all, because any "
            "alteration changes what the polynomial leaves behind. The "
            "Signature system seals every long transmission this way."),
    },
    {
        "key": "binary_gray_code",
        "name": "The Binary Reflected Gray Code",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The binary reflected Gray code, patented by Frank Gray in "
            "1953, orders the n-bit patterns so consecutive values differ "
            "in exactly one bit: 3-bit Gray runs 000, 001, 011, 010, 110, "
            "111, 101, 100. Only one witness changes its testimony at "
            "each step - never two at once. This kills the classic "
            "hazard of position encoders: with straight binary, the "
            "transition from 0111 to 1000 flips four bits, and if they "
            "do not flip at exactly the same instant the sensor reads a "
            "garbage intermediate like 0100. Gray code can never "
            "misread by more than one step, because only one bit is ever "
            "in flight. Rotary encoders, optical position sensors, and "
            "the Karnaugh maps of logic design all use Gray ordering; "
            "converting is one XOR: gray = binary XOR (binary >> 1)."),
        "how_it_works": (
            "The reflected construction builds (n+1)-bit Gray from n-bit "
            "Gray: prefix 0 to the list forward, then prefix 1 to the "
            "list backward - the reflection guarantees the single-bit "
            "property across the boundary. Conversion binary->Gray is g "
            "= b ^ (b >> 1): each Gray bit is the XOR of two adjacent "
            "binary bits. Gray->binary reverses by cumulative XOR: "
            "b_{n-1} = g_{n-1}, b_i = b_{i+1} XOR g_i, cascading down. "
            "Cyclic Gray codes also make the last-to-first step "
            "single-bit, so a rotating encoder never glitches at the "
            "wraparound. The demonstration program generates the 4-bit "
            "Gray sequence and asserts the Hamming distance between every "
            "pair of neighbors - including wraparound - is exactly 1."),
        "key_points": [
            "Consecutive Gray values differ in exactly one bit.",
            "3-bit Gray: 000,001,011,010,110,111,101,100.",
            "Binary->Gray: g = b XOR (b >> 1) - one XOR.",
            "Reflected construction: prefix 0 forward, 1 backward.",
            "Eliminates multi-bit-transition glitches in encoders.",
            "Used in rotary encoders, sensors, Karnaugh maps.",
        ],
        "requirements": [
            "XOR and right shift; the Hamming distance idea.",
            "The encoder glitch problem (0111 -> 1000).",
        ],
        "standards": [
            "US Patent 2,632,058 (Gray, 1953)",
        ],
        "citations": [CIT_GRAY, CIT_HARRIS],
        "sig_lens": (
            "The Gray procession is the Signature system's order of "
            "succession: from each sworn value to the next, exactly one "
            "witness changes its testimony - never two, never four at "
            "once, so no instant exists where the muster speaks garbage. "
            "Where straight binary risks the four-bit stumble from 0111 "
            "to 1000, the Gray code steps 0100 to 1100 with a single "
            "changed voice. His system marches its encoders in this "
            "order: one step, one witness, no stumble."),
    },
    {
        "key": "bcd",
        "name": "Binary-Coded Decimal (BCD)",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Binary-coded decimal encodes each decimal digit in its own "
            "4-bit nibble: 93 becomes 1001 0011 (0x93), and 2026 becomes "
            "0010 0000 0010 0110. The six patterns 1010-1111 are illegal "
            "in BCD - the price of decimal fidelity is wasted codes. "
            "BCD arithmetic needs a correction: adding nibbles can yield "
            "10-15 or produce a carry into the next digit, so any nibble "
            "result above 9 (or that carried) gets +6 added to skip the "
            "six illegal patterns - 9 + 5 = 14 (1110) corrects to 10100, "
            "i.e. carry 1 and digit 4. x86 even kept BCD helpers (DAA, "
            "DAS) for this. BCD survives wherever decimal exactness is "
            "non-negotiable and values are displayed, not computed: "
            "real-time clocks, calculators, financial displays, and the "
            "packed-decimal fields of COBOL-era business data."),
        "how_it_works": (
            "Packed BCD stores two digits per byte (high nibble = tens); "
            "unpacked BCD stores one digit per byte. Addition proceeds "
            "nibble by nibble in binary, then the +6 correction repairs "
            "each nibble: if the 4-bit sum exceeds 9 or the nibble carried "
            "out, add 0110. Adding 93 + 59 in BCD: 0x93 + 0x59 = 0xEC; "
            "low nibble 3+9=12 > 9, add 6 -> 18 = 0x12 (write 2, carry "
            "1); high nibble 9+5+carry 1 = 15 > 9, add 6 -> 21 = 0x15 "
            "(write 5, carry 1); result 0x152 = 152 decimal, and indeed "
            "93 + 59 = 152. Densely packed decimal (DPD, IEEE 754-2008) "
            "compresses 3 digits into 10 bits for decimal floating "
            "point - BCD's modern heir."),
        "key_points": [
            "Each decimal digit in its own nibble: 93 = 0x93.",
            "Patterns 1010-1111 are illegal in BCD.",
            "Nibble sums above 9 (or with carry) get +6 correction.",
            "Example: 0x93 + 0x59 corrects to 0x152 = 152.",
            "Packed BCD: two digits per byte; unpacked: one per byte.",
            "Used in clocks, calculators, financial displays; DPD in IEEE 754.",
        ],
        "requirements": [
            "Nibbles and hexadecimal; binary addition with carries.",
            "The decimal digits 0-9 as the fidelity target.",
        ],
        "standards": [
            "IEEE 754-2008/2019 (decimal floating-point, DPD)",
            "IBM packed decimal format",
        ],
        "citations": [CIT_KNUTH, CIT_IEEE754],
        "sig_lens": (
            "BCD is the Signature system's decimal fidelity oath: where "
            "pure binary would round the merchant's penny into "
            "unrepresentable fractions, BCD swears each decimal digit its "
            "own nibble - wasteful of the six forbidden patterns, but "
            "exact to the digit the eye reads. The +6 correction is the "
            "honest toll: whenever a nibble oversteps nine, six is added "
            "to skip the illegal country and land on the true decimal "
            "digit. For money and measures, the system keeps this oath."),
    },
    {
        "key": "subnet_masks",
        "name": "Binary in Networking: Subnet Masks",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Subnet masks are binary's most visible daily application: "
            "a 32-bit mask of leading 1s that splits an IP address into "
            "network and host portions. A /24 network has mask "
            "11111111.11111111.11111111.00000000 = 255.255.255.0: the "
            "first 24 bits name the network, the last 8 name the host. "
            "Bitwise-AND the address with the mask to get the network: "
            "192.168.1.77 AND 255.255.255.0 = 192.168.1.0. The host bits "
            "give 2^8 = 256 addresses, minus the all-zeros network "
            "address and all-ones broadcast (192.168.1.255), leaving 254 "
            "usable hosts. CIDR notation (/24, /16, /8) replaced the old "
            "class system in 1993 (RFC 1519); subnetting itself was "
            "standardized in RFC 950 (1985). Every router on Earth "
            "performs this AND on every packet it forwards."),
        "how_it_works": (
            "The mask's 1s select the network field (AND keeps them), "
            "the 0s select the host field. Network = address AND mask; "
            "broadcast = network OR (NOT mask); first usable = network + "
            "1; last usable = broadcast - 1. A /26 mask "
            "(255.255.255.192) leaves 6 host bits: 64 addresses, 62 "
            "usable. Splitting 192.168.1.0/24 into four /26 subnets "
            "yields 192.168.1.0, .64, .128, .192 - the third octet's "
            "last two bits choosing the subnet. The demonstration "
            "program computes network, broadcast, and usable-host count "
            "for 192.168.1.77/24 with pure integer bit operations and "
            "asserts the textbook values."),
        "key_points": [
            "Mask = leading 1s: /24 = 255.255.255.0.",
            "Network = address AND mask: 192.168.1.77/24 -> 192.168.1.0.",
            "Host bits h give 2^h addresses; minus 2 (network + broadcast).",
            "/24 yields 254 usable hosts; broadcast is 192.168.1.255.",
            "CIDR (/n) replaced classful addressing (RFC 1519, 1993).",
            "Every router ANDs every packet's address with a mask.",
        ],
        "requirements": [
            "Bitwise AND, NOT, OR on 32-bit values.",
            "Dotted-decimal IP notation.",
        ],
        "standards": [
            "RFC 950 (Internet Standard Subnetting Procedure)",
            "RFC 4632 / RFC 1519 (CIDR)",
        ],
        "citations": [CIT_RFC950, CIT_TANENBAUM],
        "sig_lens": (
            "The subnet mask is the Signature system's territory line: a "
            "row of thirty-two witnesses with the first n sworn to the "
            "network and the rest to the hosts, the AND operation reading "
            "out which territory an address belongs to. The network "
            "address names the land, the broadcast address calls every "
            "dweller at once, and the count of usable hosts is the "
            "muster the territory can hold. Borders drawn in bits, "
            "enforced by every router's AND."),
    },
    {
        "key": "overflow_flags",
        "name": "Overflow, Carry, and CPU Status Flags",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "After every arithmetic operation the CPU distills what "
            "happened into status flags - single bits the program can "
            "branch on. The four classic flags: Carry (C) - unsigned "
            "overflow, a carry out of the top bit; Overflow (V) - signed "
            "overflow, the result's sign is impossible; Zero (Z) - the "
            "result was zero; Negative (N) - the result's top bit is 1. "
            "Adding 100 + 60 in 8-bit signed arithmetic gives 160, which "
            "reads as -96: two positives made a negative, so V=1 - signed "
            "overflow. The same bit pattern as unsigned (160 < 255) sets "
            "no carry: C=0 - unsigned is fine. x86 packs these into "
            "EFLAGS (CF, OF, ZF, SF); ARM uses NZCV. The rule for V: the "
            "carry into the sign bit differs from the carry out - the "
            "hardware computes it with one XOR gate on the last two "
            "carries."),
        "how_it_works": (
            "The adder already produces the carries; the flags are just "
            "observations: C = carry out of bit n-1; V = carry into bit "
            "n-1 XOR carry out of bit n-1; Z = NOR of all result bits; N "
            "= result's top bit. Signed overflow happens exactly when "
            "adding two same-sign values yields the opposite sign - 100 "
            "(01100100) + 60 (00111100): bit 7's column gets carry-in 1 "
            "and produces carry-out 0, 1 XOR 0 = 1, so V=1 and the result "
            "10100000 = -96 is wrong as signed. Conditional branches "
            "(JG, JL, JA, JB on x86; B.GT, B.HI on ARM) are Boolean "
            "functions of these flags, so all signed and unsigned "
            "comparison reduces to flag-reading after a subtraction."),
        "key_points": [
            "Carry (C): unsigned overflow - carry out of the top bit.",
            "Overflow (V): signed overflow - impossible sign; carry-in XOR carry-out of sign bit.",
            "Zero (Z): result was zero. Negative (N): top bit set.",
            "Example: 100 + 60 (8-bit signed) -> -96, V=1, C=0.",
            "x86 EFLAGS (CF/OF/ZF/SF); ARM NZCV.",
            "All comparisons compile to flag tests after subtraction.",
        ],
        "requirements": [
            "Twos complement ranges and the carry chain.",
            "Signed vs unsigned readings of one bit pattern.",
        ],
        "standards": [
            "Intel 64 and IA-32 Architectures Software Developer Manual (EFLAGS)",
            "ARM Architecture Reference Manual (NZCV)",
        ],
        "citations": [CIT_PATT_HENN, CIT_STALLINGS],
        "sig_lens": (
            "The status flags are the after-action testimony of the "
            "Signature system: when the addition is done, four witnesses "
            "report - did the tally overflow its unsigned bounds, did "
            "the signed reading become impossible, was the result "
            "silence, did it turn negative. The overflow flag is the "
            "system's honesty bit: two positives must never swear a "
            "negative, and when they do, the flag says so plainly. "
            "Every branch the machine takes is decided by this "
            "testimony."),
    },
]
