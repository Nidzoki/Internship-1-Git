def center_align_text(text, m, n):
    lines = []
    words = text.split() 
    current_line = []

    for word in words:
        if len(" ".join(current_line + [word])) <= m:
            current_line.append(word)
        else:
            lines.append(" ".join(current_line)) 
            current_line = [word] 

    if current_line:
        lines.append(" ".join(current_line))

    aligned_lines = []
    for line in lines:
        empty_space = n - len(line)
        left_space = empty_space // 2
        right_space = empty_space - left_space
        centered_line = " " * left_space + line + " " * right_space
        aligned_lines.append(centered_line)

    return "\n".join(aligned_lines)

def getUserInputAndPrint():
    m = int(input("Maximum number of characters per line: "))
    n = int(input("Line width: "))
    text = input("Text: ")

    if n < m:
        print("Line width cannot be shorter than the maximum number of characters per line.")
    else:
        aligned_text = center_align_text(text, m, n)
        print("\nCentered text:\n")
        print(aligned_text)

getUserInputAndPrint()