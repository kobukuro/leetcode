# Tags: Array, String, Hash Set
from typing import List


class Solution:
    def num_unique_emails(self, emails: List[str]) -> int:
        """
        Complexity Analysis:
            Time: O(n * m)
                - n: number of emails
                - m: average length of each email
                - We iterate through each email once, and for each email we perform
                  split, replace operations which are O(m)

            Space: O(n * m)
                - In the worst case, all emails are unique after normalization
                - Each normalized email could be up to O(m) in length
                - The set stores up to n unique emails
        """
        unique_emails = set()
        for email in emails:
            names = email.split('@')
            local_name = names[0].split('+')[0].replace('.', '')
            domain_name = names[1]
            unique_emails.add(local_name + '@' + domain_name)
        return len(unique_emails)
