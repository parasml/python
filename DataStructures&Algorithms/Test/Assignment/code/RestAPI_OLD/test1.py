from faker import Faker  
faker = Faker()  
ip_addr = faker.ipv4() 
hostName = faker.hostname()
domainName = faker.domain_name()
domainWord = faker.domain_word()
TLD = faker.tld()
loopBack = faker.ipv4(network=False)
