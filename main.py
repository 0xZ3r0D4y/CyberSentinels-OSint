from modules.email_tracker import EmailTracker
from modules.username_tracker import UsernameTracker
from src.util import map_banner, extract_nums

class CsOSIntTool:
    """
    OSINT tool for tracking emails and usernames across platforms.
    """

    def __init__(self):
        """
        Initializes the tool and displays the available modules for interaction.
        """
        print(map_banner)
        self.run_tool()

    def run_tool(self):
        """
        Displays the menu and handles user input for selecting modules.
        """
        while True:
            print("\n\nModules available:")
            print("    1 - Email Tracker")
            print("    2 - Username Tracker")
            print("    99 - Exit")

            try:
                cmd = extract_nums(input("[?] Enter module code: "))
                match cmd:
                    case 1:
                        self.email_tracker()
                    case 2:
                        self.username_tracker()
                    case 99:
                        print("[+] Exiting the tool. Goodbye!")
                        break
                    case _:
                        print("[!] Not a valid code")
            except Exception as e:
                print(f"[!] Error: {e}")

    def email_tracker(self):
        """
        Prompts the user for an email to track and displays the associated accounts.
        """
        email = input("[?] Enter the email to track: ")

        tracker = EmailTracker(email)
        emails = tracker.__dict__

        print("[+] Accounts Found (Note: May include false positives):")
        
        counter = 1
        for email in emails.keys():

            if emails[email] == True:
                print(f"[+]    {counter} - {email.capitalize()}")
                counter += 1

    def username_tracker(self):
        """
        Prompts the user for a username to track and displays the associated accounts.
        """
        username = input("[?] Enter the username to track: ")

        print("[+] Accounts Found (Note: May include false positives):")
        UsernameTracker(username)


if __name__ == "__main__":
    CsOSIntTool()
