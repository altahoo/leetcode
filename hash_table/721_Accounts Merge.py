# 721. Accounts Merge

# Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

# After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_account = collections.defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                email_to_account[email].append(i)
        visited = set()
        result = []

        for i in range(len(accounts)):
            if i in visited:
                continue
            queue = collections.deque([i])
            emails = set()
            while queue:
                cur_account = queue.popleft()
                visited.add(cur_account)
                for email in accounts[cur_account][1:]:
                    emails.add(email)
                    for account in email_to_account[email]:
                        if account in visited:
                            continue
                        queue.append(account)
                        visited.add(account)
            result.append([accounts[i][0]] + sorted(list(emails)))
        return result