# INET4031 Add Users Script and User List

## Program Description

This Python script helps automate adding multiple users to an Ubuntu system. Instead of running commands like `useradd`, `passwd`, and `usermod` for each user manually, the script reads a list of users from a file and does it all for you automatically.

## Program User Operation

This program reads user info from an input file, processes each line, and runs the needed system commands to add users and assign groups.

### Input File Format

Each line in the input file follows this format:
- To skip a line, add `#` at the beginning.
- To skip group creation, use `-` in the group section.

### Command Excuction

Make the script executable:
```bash
chmod +x create-users.py
sudo ./create-users.py < create-users.input
