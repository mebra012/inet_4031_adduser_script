#!/usr/bin/python3

# INET4031
# Seare Mebrahtu
# March 25, 2025
# March 25, 2025

# Importing modules:
# os – lets us run system commands
# re – used for regular expressions
# sys – used to read from standard input
import os
import re
import sys

def main():
    # Prompt the user to determine if the script should run in dry-run mode (no commands executed)
    dry_run = input("Run in dry-run mode? (Y/N): ").strip().upper()

    # Read all input lines provided to the script (typically from redirected stdin)
    lines = sys.stdin.readlines()

    # Process each line from the input
    for line in lines:
        line = line.strip()

        # Skip lines starting with '#' (comments) or invalid lines with incorrect number of fields
        match = re.match("^#", line)
        fields = line.split(':')

        if match or len(fields) != 5:
            if dry_run == 'Y':
                # In dry-run mode, print the skipped or invalid line to inform the user
                print(f"Skipping or invalid line: {line}")
            continue

        # Extract username, password, GECOS info, and group memberships from the input line
        username, password = fields[0], fields[1]
        gecos = f"{fields[3]} {fields[2]},,,"
        groups = fields[4].split(',')

        # Print message about creating the user account
        print(f"==> Creating account for {username}...")
        cmd_create = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"

        if dry_run == 'Y':
            # Dry-run mode: Only print the command instead of executing it
            print(f"DRY-RUN: {cmd_create}")
        else:
            # Normal mode: Execute the command to create the user
            os.system(cmd_create)

        # Print message about setting the user's password
        print(f"==> Setting the password for {username}...")
        cmd_passwd = f"/bin/echo -ne '{password}\n{password}' | /usr/bin/sudo /usr/bin/passwd {username}"

        if dry_run == 'Y':
            # Dry-run mode: Only print the command instead of executing it
            print(f"DRY-RUN: {cmd_passwd}")
        else:
            # Normal mode: Execute the command to set the password
            os.system(cmd_passwd)

        # Assign the user to each group listed (excluding '-')
        for group in groups:
            if group != '-':
                print(f"==> Assigning {username} to the {group} group...")
                cmd_group = f"/usr/sbin/adduser {username} {group}"

                if dry_run == 'Y':
                    # Dry-run mode: Only print the command instead of executing it
                    print(f"DRY-RUN: {cmd_group}")
                else:
                    # Normal mode: Execute the command to assign user to group
                    os.system(cmd_group)

if __name__ == '__main__':
    main()
