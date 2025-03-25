#!/usr/bin/python3

# INET4031
# Seare Mebrahtu
# March 25, 2025
# March 25, 2025

# os lets the script run system commands like creating users or setting passwords
# re is used to check if a line starts with a # so we know to skip it
# sys lets the script read each line from the input file that we pass in
import os
import re
import sys

def main():
    for line in sys.stdin:


        # This regex checks if the line starts with a '#' character.
        # if the line has a # at the start, we skip it and don’t try to make a user from it
        match = re.match("^#",line)
	
        # This print just shows what the match variable found (used for testing)
        print ("The Content of the Match Varable were: ", match)

        # This splits the line using ":" so we can grab the info separately
        # like username, password, first name, last name, and the groups
        # We need each part by itself because later in the code we use the username to make the user,
        # the password to set their login, and the group part to know where they belong
        fields = line.strip().split(':')

        # This print shows how the line was split (also just for testing)
        print("Length of field was: ", fields)

        # this checks if the line starts with a # or if it doesn’t have 5 things in it
        # if it’s a comment or missing info, it skips the line and doesn’t try to make a user from it
        # It uses the "match" from earlier to catch comments, and "fields" to make sure we got all 5 parts of the user info  
        if match or len(fields) != 5:
            continue

        # This grabs the username and password so we can use them to make the account
        # the gecos just puts the first and last name together so it shows up in the system
        # this info ends up in the passwd file so we know who the user is
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        # This breaks up the groups by the commas in case the user is supposed to be in more than one group
        # we need them separate so we can loop through and add the user to each group
        groups = fields[4].split(',')

        # This prints out which user is being made
        print("==> Creating account for %s..." % (username))
        # This makes the command to create the user without a password and adds their name info
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        # This runs the command we built earlier (cmd) to actually create the user on the system
        #print cmd
        os.system(cmd)

        # This tells us which user is about to have their password set
        print("==> Setting the password for %s..." % (username))
        # This builds a command that sends the password twice (like typing it in) to the passwd command
        # cmd will hold the full command that sets the user’s password without having to type it manually
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #print cmd
        os.system(cmd)

        for group in groups:
            # This checks if the group isn’t just a dash (-), which means no group
            # if it's a real group name, it adds the user to that group
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                os.system(cmd)

if __name__ == '__main__':
    main()
