from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = 0
        emails_received = set()
        for email in emails:
            parts = email.split('@')
            parts[0] = parts[0].replace('.', '')
            parts[0] = parts[0].split('+')[0]
            email_res = parts[0] + '@' + parts[1]
            if email_res not in emails_received:
                emails_received.add(email_res)
                res += 1
        return res
