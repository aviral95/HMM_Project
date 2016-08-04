import re
import math

obs=raw_input('Enter the sequence:')
obs=re.findall("[A-Z]+",obs)
obs=reduce(lambda i,j:i+j,obs)
states=['N','C']



start_p={"C":math.log10(0.5),"N":math.log10(0.5)}

a=['G','A','V','L','I']
b=['S','C','T','M']
c=['P']
d=['F','Y','W']
e=['D','E','N','Q']
f=['H','K','R']
         
for i in a:
    obs=obs.replace(i,'a')
for i in b:
    obs=obs.replace(i,'b')
for i in c:
    obs=obs.replace(i,'c')
for i in d:
    obs=obs.replace(i,'d')
for i in e:
    obs=obs.replace(i,'e')
for i in f:
    obs=obs.replace(i,'f')

print obs

        
trans_p={'C':{'C':math.log10(0.845818492663),'N':math.log10(0.154181507337)},'N':{'C':math.log10(0.00124496070874),'N':math.log10(0.998755039291)}}

emit_p={'N':{'a':math.log10(0.17808777399999998),'b':math.log10(0.198663392),'c':math.log10(0.109939597),
             'd':math.log10(0.055756220999999995),'e':math.log10(0.27758376500000004),'f':math.log10(0.171461905)},

        #'C':{'a':math.log10(0.22373848000000002),'b':math.log10(0.183318385),'c':math.log10(0.151254274),
    #             'd':math.log10(0.055756220999999995),'e':math.log10(0.204802246),'f':math.log10(0.185506189)

        'C':{'a':0.31517302573203193,'b':0.18225377107364685,'c':0.12706299911268856,'d':0.025199645075421474,
                'e':0.1852706299911269,'f':0.1650399290150843}

        #'C':{'ali':0.31517302573203193,'hyd':0.18225377107364685,'cyc':0.12706299911268856,'aro':0.025199645075421474,
        #        'bas':0.1852706299911269,'aci':0.1650399290150843},

        }


 

def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}
 
    for y in states:
        V[0][y] = start_p[y] + emit_p[y][obs[0]]
        path[y] = [y]

    for t in range(1, len(obs)):
        V.append({})
        newpath = {}
 
        for y in states:
            (prob, state) = max((V[t-1][y0] + trans_p[y0][y] + emit_p[y][obs[t]], y0) for y0 in states)
            V[t][y] = prob
            newpath[y] = path[state] + [y]
 
        path = newpath
        print prob
    n=0
    if len(obs)!=1:
        n=t
    (prob, state)= max((V[n][y],y) for y in states)
    return (prob, path[state])

print viterbi(obs, states, start_p, trans_p, emit_p)

        
            
