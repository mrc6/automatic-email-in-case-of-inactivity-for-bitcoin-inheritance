from pathlib import Path
import diff_days
import email_sender

def write_file(filename, options, data):
    with open(filename, options) as f:
        f.write(data)
        f.close()

def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        f.close()
        return lines

####### Main
def main():
    path = Path('./sended_emails.txt')
    diff = diff_days.days()
    
    
    # Time intervals to send a e-mail
    # Remind you to hit the script
    if diff >= 2 and diff < 30:
        email_sender.main("your.email.here@gmail.com", "You haven't updated your proof of life in at least "+str(diff)+" days", "You haven't updated your proof of life in at least "+str(diff)+" days. Update or wait for instructions in the next email")

    # first e-mail with instructions
    if diff >= 30 and diff < 90:
        count = '1\n'
        if path.is_file():
            lines = read_file('sended_emails.txt')
            if len(lines) < 1:
                #Send e-mail with message: The password to open the will file is ########
                email_sender.main("your.email.here@gmail.com, friend.spouse.email.here@gmail.com", "Instructions for opening the will file", "The password to open the will file is is ########")
                write_file('sended_emails.txt', 'a+', count)
            else:
                if lines[0] != count:
                    #Send e-mail with message: The password to open the will file is ########
                    email_sender.main("your.email.here@gmail.com, friend.spouse.email.here@gmail.com", "Instructions for opening the will file", "The password to open the will file is is ########")
                    write_file('sended_emails.txt', 'a+', count)
        else:
            #Send e-mail with message: The password to open the will file is ########
            email_sender.main("your.email.here@gmail.com, friend.spouse.email.here@gmail.com", "Instructions for opening the will file", "The password to open the will file is is ########")
            write_file('sended_emails.txt', 'a+', count)

    # second e-mail with instructions
    if diff >= 90 and diff < 180:
        count = '2\n'
        if path.is_file():
            lines = read_file('sended_emails.txt')
            if len(lines) < 2:
                #Send e-mail with message: the password to open seed file is ########
                email_sender.main("your.email.here@gmail.com, friend.spouse.email.here@gmail.com", "Instructions for opening the seed file", "The password to open the seed file is ########")
                write_file('sended_emails.txt', 'a+', count)
            else:
                if lines[1] != count:
                    #Send e-mail with message: the password to open seed file is ########
                    email_sender.main("your.email.here@gmail.com, friend.spouse.email.here@gmail.com", "Instructions for opening the seed file", "The password to open the seed file is ########")
                    write_file('sended_emails.txt', 'a+', count)
        else:
            #Send e-mail with message: Proccess of delivering e-mail was broken, please go to plan B
            email_sender.main("your.email.here@gmail.com, friend.spouse.email.here@gmail.com", "Process broken", "The automatic email delivery process is broken, please go to plan B")
    # last e-mail with instructions
    if diff >= 180 and diff < 360:
        count = '3\n'
        if path.is_file():
            lines = read_file('sended_emails.txt')
            if len(lines) < 3:
                #Send e-mail with message: the password to open passphrase file is ########
                email_sender.main("your.email.here@gmail.com, friend.spouse.email.here@gmail.com", "Instructions for opening the passphrase file", "The password to open the passphrase file is ########")
                write_file('sended_emails.txt', 'a+', count)
            else:
                if lines[2] != count:
                    #Send e-mail with message: the password to open passphrase file is ########
                    email_sender.main("your.email.here@gmail.com, friend.spouse.email.here@gmail.com", "Instructions for opening the passphrase file", "The password to open the passphrase file is ########")
                    write_file('sended_emails.txt', 'a+', count)
        else:
            #Send e-mail with message: Proccess of delivering e-mail was broken, please go to plan B
            email_sender.main("your.email.here@gmail.com, friend.spouse.email.here@gmail.com", "Process broken", "The automatic email delivery process is broken, please go to plan B")

if __name__ == "__main__":
    main()