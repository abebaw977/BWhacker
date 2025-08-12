import dns.resolver
from abu_color import AbuAll
def subdomain_bruteforce():
    resolver = dns.resolver.Resolver()
    target_domain = input(" Enter target domain (e.g., example.com): ")
    wordlist_path = input(" Enter path to wordlist (e.g., subdomains.txt): ")
    
    with open(wordlist_file, 'r') as file:
        words = file.read().splitlines()

    print(f"🔍 Starting brute-force on: {domain}\n")

    for word in words:
        subdomain = f"{word}.{domain}"
        try:
            answers = resolver.resolve(subdomain, 'A')
            for rdata in answers:
                print(AbuAll(f"[ FOUND] {subdomain} --> {rdata}",bg="yellow",sty="b"))
        except dns.resolver.NXDOMAIN:
            pass
        except dns.resolver.NoAnswer:
            pass
        except dns.exception.Timeout:
            print(f"[TimeOut] {subdomain}")
        except Exception as e:
            print(f"[!] {subdomain}: {e}")

