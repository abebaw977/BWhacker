import dns.resolver

def subdomain_bruteforce(domain, wordlist_file):
    resolver = dns.resolver.Resolver()

    with open(wordlist_file, 'r') as file:
        words = file.read().splitlines()

    print(f"🔍 Starting brute-force on: {domain}\n")

    for word in words:
        subdomain = f"{word}.{domain}"
        try:
            answers = resolver.resolve(subdomain, 'A')
            for rdata in answers:
                print(f"[✅ FOUND] {subdomain} --> {rdata}")
        except dns.resolver.NXDOMAIN:
            pass
        except dns.resolver.NoAnswer:
            pass
        except dns.exception.Timeout:
            print(f"[⏱ TIMEOUT] {subdomain}")
        except Exception as e:
            print(f"[⚠ ERROR] {subdomain}: {e}")

if __name__ == "__main__":
    target_domain = input("🌐 Enter target domain (e.g., example.com): ")
    wordlist_path = input("📄 Enter path to wordlist (e.g., subdomains.txt): ")
    subdomain_bruteforce(target_domain, wordlist_path)	
