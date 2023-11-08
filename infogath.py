import whois
import dns.resolver
import shodan
import requests
import argparse
import socket

argparse = argparse.ArgumentParser(description="This is a basic information gathering tool.", usage ="Python3 infogath.py -d DOMAIN [-s]")
argparse.add_argument("-d","--domain",help="Enter the domain name for footprinting")
argparse.add_argument("-s","--shodan",help="Enter the Ip for shodan search.")

args =argparse.parse_args()
domain =args.domain
ip = args.shodan

##print("[+] Domain {} and IP {}".format(domain,ip))

try:
    # Network query
    # whois module
    print("[+] Getting whois info..")
    # using whois library ,creating instances
    py = whois.query(domain)
    print("[+] Whois info found. ")
    print("Name: {}".format(py.name))
    print("Registrar: {}".format(py.registrar))
    print("Creation Date: {}".format(py.creation_date))
    print("Expiration Date: {}".format(py.expiration_date))
    print("Registrant: {}".format(py.registrant))
    print("registrant country: {}".format(py.registrant_country))

except:
    pass


 #DNS MODULE
 print("[+] Getting DNS info..")
#implementing dns.resolver from dnspython

try:
    for a in dns.resolver.resolve(domain,'A'):
        print("[+] A record: {}".format(a.to_text()))
    for ns in dns.resolver.resolve(domain, 'NS'):
        print("[+] NS record: {}".format(ns.to_text()))
    for mx in dns.resolver.resolve(domain,'MX'):
        print("[+] MX record: {}".format(mx.to_text()))
    for txt in dns.resolver.resolve(domain, 'TXT'):
        print("[+] TXT record: {}".format(txt.to_text()))

except:
    pass

#Geolocation module
print("[+] Getting geolocation info..")
#implementation of request for web request
try:
    response = requests.('GET' , "https://geolocation-db.com/json/" + socket.gethostbyname(domain)).json()
    print("[+] Country: {}".format(response['country_name']))
    print("[+] Lattitude: {}".format(response['lattitude']))
    print("[+] Longitude: {}".format(response['longitude']))
    print("[+] City: {}".format(response['city']))
    print("[+] State: {}".format(response['state']))

except:
    pass