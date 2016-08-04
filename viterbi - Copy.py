import re

obs=raw_input('Enter the sequence:')
obs=re.findall("[A-Z]+",obs)
obs=reduce(lambda i,j:i+j,obs)
states=['N','C']

start_p={"C":0.5,"N":0.5}

trans_p={'C':{'C':0.845818492663,'N':0.154181507337},'N':{'C':0.00124496070874,'N':0.998755039291}}

emit_p={'N':{'A':0.045262496,'C':0.018304828,'D':0.055531785,'E':0.069877187,'F':0.018699099,'G':0.054335488,
            'H':0.055214248,'I':0.021390933,'K':0.060908256,'L':0.026880809,'M':0.033653565,'N':0.072021945,
            'P':0.109939597,'Q':0.080152848,'R':0.055339401,'S':0.094081541,'T':0.061130806,'V':0.030218048,'W':0.015131357,'Y':0.021925765},

        'C':{'A':0.063631691,'C':0.006309705,'D':0.041325898,'E':0.074220578,'F':0.016431523,'G':0.083689366,
            'H':0.021413025,'I':0.013638164,'K':0.082934151,'L':0.036275237,'M':0.025146217,'N':0.029504778,
            'P':0.151254274,'Q':0.059750992,'R':0.081159013,'S':0.090731657,'T':0.061130806,'V':0.026504022,'W':0.017442693,'Y':0.016863931},
        }


 

def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}
 
    for y in states:
        V[0][y] = start_p[y] * emit_p[y][obs[0]]
        path[y] = [y]

    for t in range(1, len(obs)):
        V.append({})
        newpath = {}
 
        for y in states:
            (prob, state) = max((V[t-1][y0] * trans_p[y0][y] * emit_p[y][obs[t]], y0) for y0 in states)
            V[t][y] = prob
            newpath[y] = path[state] + [y]
 
        path = newpath
    n=0
    if len(obs)!=1:
        n=t
    (prob, state)= max((V[n][y],y) for y in states)
    return (prob, path[state])

print viterbi(obs, states, start_p, trans_p, emit_p)

        
            
