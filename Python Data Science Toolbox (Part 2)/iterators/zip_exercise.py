mutants =['charles xavier', 'bobby drake', 'kurt wagner', 'max eisenhardt', 'kitty pryde']
aliases =['prof x', 'iceman', 'nightcrawler', 'magneto', 'shadowcat']
powers=['telepathy','thermokinesis','teleportation','magnetokinesis','intangibility']

z= zip(mutants,aliases,powers)
z1,z2=zip(*z)
print(z1)
