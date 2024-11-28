import requests
from bs4 import BeautifulSoup

class EmailTracker:
    def __init__(self, email: str) -> None:
        self.email = email
        self.user_agent = (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        )

        # Service checks
        self.instagram = self.check_instagram()
        self.twitter = self.check_twitter()
        self.pinterest = self.check_pinterest()
        self.patreon = self.check_patreon()
        self.spotify = self.check_spotify()
        self.firefox = self.check_firefox()
        self.lastpass = self.check_lastpass()
        self.archive = self.check_archive()
        self.pornhub = self.check_pornhub()
        self.xnxx = self.check_xnxx()
        self.xvideos = self.check_xvideos()

    # Helper for Instagram check
    def check_instagram(self) -> bool:
        try:
            session = requests.Session()
            headers = {
                'User-Agent': self.user_agent,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Origin': 'https://www.instagram.com',
                'Connection': 'keep-alive',
                'Referer': 'https://www.instagram.com/',
            }

            # Step 1: Get the CSRF token
            response = session.get(
                "https://www.instagram.com/accounts/emailsignup/",
                headers=headers
            )
            if response.status_code == 200 and 'csrftoken' in session.cookies:
                csrf_token = session.cookies['csrftoken']
            else:
                return None

            # Step 2: Send email verification request
            headers.update({
                "x-csrftoken": csrf_token,
                "Referer": "https://www.instagram.com/accounts/emailsignup/",
            })
            data = {"email": self.email}
            response = session.post(
                url="https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/",
                headers=headers,
                data=data,
            )

            if response.status_code == 200:
                return "email_is_taken" in response.text
            return False
        except Exception:
            return None

    # Helper for Twitter check
    def check_twitter(self) -> bool:
        try:
            session = requests.Session()
            response = session.get(
                url="https://api.twitter.com/i/users/email_available.json",
                params={"email": self.email}
            )

            if response.status_code == 200:
                return response.json().get("taken", False)
            return None
        except Exception:
            return None

    # Helper for Pinterest check
    def check_pinterest(self) -> bool:
        try:
            session = requests.Session()
            response = session.get(
                url="https://www.pinterest.com/_ngjs/resource/EmailExistsResource/get/",
                params={
                    "source_url": "/",
                    "data": f'{{"options": {{"email": "{self.email}"}},"context": {{}}}}'
                },
            )
            if response.status_code == 200:
                resource_response = response.json().get("resource_response", {})
                message = resource_response.get("message", "")
                data = resource_response.get("data", None)

                if message == "Invalid email.":
                    return False
                if message == "ok" and data is not None:
                    return data
            return None
        except Exception:
            return None

    # Other services follow similar patterns:
    def check_patreon(self) -> bool:
        return self._simple_post_check(
            url="https://www.plurk.com/Users/isEmailFound",
            data={"email": self.email},
            success_keyword="True"
        )

    def check_spotify(self) -> bool:
        return self._simple_get_check(
            url="https://spclient.wg.spotify.com/signup/public/v1/account",
            params={"validate": "1", "email": self.email},
            success_condition=lambda res: res.json().get("status") == 20
        )

    def check_firefox(self) -> bool:
        return self._simple_post_check(
            url="https://api.accounts.firefox.com/v1/account/status",
            data={"email": self.email},
            success_keyword="true"
        )

    def check_lastpass(self) -> bool:
        return self._simple_get_check(
            url=f"https://lastpass.com/create_account.php?check=avail&username={self.email.replace('@', '%40')}",
            success_keyword="no"
        )

    def check_archive(self) -> bool:
        return self._simple_post_check(
            url="https://archive.org/account/signup",
            data=f"""
                -----------------------------
                Content-Disposition: form-data; name="input_name"
                username
                -----------------------------
                Content-Disposition: form-data; name="input_value"
                {self.email}
                -----------------------------
                Content-Disposition: form-data; name="submit_by_js"
                true
                -----------------------------
            """,
            success_keyword="is already taken"
        )

    def check_pornhub(self) -> bool:
        return self._simple_post_check(
            url="https://www.pornhub.com/user/create_account_check",
            data={"check_what": "email", "email": self.email},
            success_keyword="Email has been taken"
        )

    def check_xnxx(self) -> bool:
        return self._simple_get_check(
            url=f"https://www.xnxx.com/account/checkemail?email={self.email.replace('@', '%40')}",
            success_keyword="This email is already in use"
        )

    def check_xvideos(self) -> bool:
        return self._simple_get_check(
            url="https://www.xvideos.com/account/checkemail",
            params={"email": self.email},
            success_keyword="This email is already in use"
        )

    # Utility functions for repeated patterns
    def _simple_post_check(self, url: str, data: dict, success_keyword: str) -> bool:
        try:
            session = requests.Session()
            response = session.post(url, data=data)
            if response.status_code == 200:
                return success_keyword in response.text
            return None
        except Exception:
            return None

    def _simple_get_check(self, url: str, params: dict = None, success_keyword: str = "", success_condition=None) -> bool:
        try:
            session = requests.Session()
            response = session.get(url, params=params)
            if response.status_code == 200:
                if success_condition:
                    return success_condition(response)
                return success_keyword in response.text
            return None
        except Exception:
            return None

