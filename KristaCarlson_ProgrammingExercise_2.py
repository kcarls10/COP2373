import re

def spam_email_scanner(email):
    #30 keywords commonly found in spam emails
    common_keywords = [ "winner", "click here", "prize", "unsubscribe", "congratulations",
                        "pre-qualify", "account suspended", "social security", "compromised",
                        "urgent", "click below", "apply now", "limited time", "free", "cash bonus",
                        "immediate action", "last call", "prize", "cancel now", "register now", "order now",
                        "earn money", "pre-approved", "investment", "exclusive deal", "act now", "debt",
                        "work from home", "don't delete", "cheap", "discount", "million dollars"]

    text = email.lower()
    score = 0
    keywords_found = []

    #scan for keywords
    for word in common_keywords:
        count = text.count(word)
        if count > 0:
            score += count
            keywords_found.append(word)
    #Spam score
    if score == 0:
        likelihood = "Not Likely Spam"
    elif score < 5:
           likelihood = "Average likelihood to be spam"
    else:
        likelihood = "Higher than average likelihood to be spam"
    return likelihood, keywords_found, score

print("Enter suspicious email: ")
email = ""
while True:
     try:
        line = input()
        email += line
     except EOFError:
        break

likelihood, keywords_found, score = spam_email_scanner(email)

print("Spam Email Scanner Results")
print(f"Overall Spam Score: {score}")
print(f"likely Spam Score: {likelihood}")
print(f"Spam Keywords Found: {', '.join(keywords_found) if keywords_found else 'No keywords found'})")