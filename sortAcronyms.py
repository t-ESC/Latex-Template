import re

FILENAMES = ["ads/acronyms.tex"]
ORDER_TRANSLATION_TABLE = str.maketrans('','',"^$_\{\}")
PATTERN_REMOVE_COMMANDS = r"(\\[^{]*{)"

def main(filename):

    all_acro_lines = {}
    all_comment_lines = []

    with open(filename, "r", encoding="utf8") as file:
        text = file.readlines()

    # read file and store lines
    for line in text:
        if line.startswith("%"):
            all_comment_lines.append(line)
        elif "\\acro{" in line:
            if not line.endswith("\n"):
                line += "\n"
            if '[' in line:
                all_acro_lines[line.split('[')[1].split(']')[0]] = line
            else:
                all_acro_lines[line.split("{")[1].split("}")[0]] = line
        

    # sort the acronyms
    sorted_acro_lines = [i[1] for i in sorted(all_acro_lines.items(), key=lambda x:(re.sub(PATTERN_REMOVE_COMMANDS,"",x[0]).translate(ORDER_TRANSLATION_TABLE).lower()
    , x[1]))]

    # rewrite the file
    with open(filename, "w", encoding="utf8") as file:
        file.writelines(all_comment_lines)
        file.writelines(sorted_acro_lines)


if __name__ == '__main__':
    [main(i) for i in FILENAMES]
    # input("press enter to exit...")