import dns.resolver

# Read domains from a text file
with open('url.txt', 'r') as file:
    domains = file.read().splitlines()

# Iterate over the domains
for domain in domains:
    answers = dns.resolver.resolve(domain, 'NS')

    with open('nameservers.txt', 'a') as file:
        for server in answers:
            ns = str(server.target)
            ip_answers = dns.resolver.resolve(ns, 'A')

            for ip in ip_answers:
                file.write(f"Domain: {domain}\tNameserver: {ns}\tIP Address: {ip.address}\n")

