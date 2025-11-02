#!/usr/bin/python

import os
import sys
import shutil


license_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "licenses")
licenses = [
    os.path.splitext(f)[0] for f in os.listdir(license_dir) if f.endswith(".txt")
]


def print_licenses():
    for license in licenses:
        print(license)


def help_message():
    print("Usage: license <license|subcommand>")
    print("Subcommands:")
    print("  list                list available licenses (one per line)")
    print("  help                show this help message")
    print("  read                print license to stdout")
    print("  shell <language>    print shell completions (`fish`)")
    print("  <license> [file]    save license file to `file` (default: `LICENSE`)")


def fish_completions(cmd: str):
    # https://fishshell.com/docs/current/completions.html
    # TODO: make this much better

    licenses_str = " ".join(licenses)
    subcmds_str = " ".join(["help", "list", "shell", "read"])

    print(
        f'complete -c {cmd} -n "not __fish_seen_subcommand_from read" -a "{subcmds_str}" -f'
    )
    print(f'complete -c {cmd} -a "{licenses_str}" -f')
    print(
        f'complete -c {cmd} -n "__fish_seen_subcommand_from read" -a "{licenses_str}" -f'
    )


def shell_completions(cmd: str, language: str):
    if language != "fish":
        print("Error: only fish shell completions are supported as of now")
        exit(1)
    fish_completions(cmd)


def save_license(name: str, out: str):
    path = os.path.join(license_dir, f"{name}.txt")
    shutil.copyfile(path, out)
    print(f"Saved license {name} as {out}")
    print("Remember to change the name and year in the license file!")


def read_license(name: str):
    path = os.path.join(license_dir, f"{name}.txt")
    with open(path, "r") as f:
        shutil.copyfileobj(f, sys.stdout)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        help_message()
        exit(1)

    command = sys.argv[1]
    if command == "help":
        help_message()
    elif command == "list":
        print_licenses()
    elif command == "shell":
        if len(sys.argv) < 3:
            print("Usage: license shell <langage>")
            print("Available shell completion languages are `fish`, yeah only `fish`")
            exit(1)
        language = sys.argv[2]
        cmd = os.path.basename(sys.argv[0])
        shell_completions(cmd, language)
    elif command == "read":
        if len(sys.argv) < 3:
            print("Usage: license read <license>")
            exit(1)
        name = sys.argv[2]
        read_license(name)
    else:
        if command not in licenses:
            print(f"Error: Unknown command/license - `{command}`")
            exit(1)

        out = sys.argv[2] if len(sys.argv) >= 3 else "LICENSE"
        save_license(command, out)
