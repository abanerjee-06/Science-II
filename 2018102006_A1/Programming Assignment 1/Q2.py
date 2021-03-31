"""
In this question, we are using the M.AaaS1ORF662P gene which is a methyl transferase gene. We are checking for the restriction enzyme called ApoI.
Recognition site for ApoI is RAATTY. R = A or G  and   Y = C or T
"""

import numpy as np
import matplotlib.pyplot as plt
from RE import RE_sites

pairs = {
    'A': 'T',
    'C': 'G',
    'G': 'C',
    'T': 'A'
}

DNA_seq = ""
f = open("M.AaaS1ORF662P.txt","r")
DNA_seq = f.read().replace('\n','').replace('\r','').replace(' ','')

l = len(DNA_seq)
start1 = 0
end1 = 6
L1 = []
count = 0
cuts = []

print("Length of M.AaaS1ORF662P gene = ",l,"nt\n")
print("UNIQUE SEQUENCES WITH LENGTH 6:\n")
while (end1-l < 6):
    if (end1 <= l):
        site1 = DNA_seq[start1:end1:] 
        if (site1[1]=='A' and site1[2]=='A' and site1[3]=='T' and site1[4]=='T' and (site1[0]=='A' or site1[0]=='G') and (site1[5]=='C' or site1[5]=='T')):           
            print("Site No.: ",count,"\tat ",start1+1," - ",end1,"\tRE Site: ",site1,"\tRE Name: ApoI \t cuts after ",start1+1)
            cuts.append(start1+1)
    else:
        site1 = DNA_seq[start1:l:]+DNA_seq[0:end1-l:]
        if (site1[1]=='A' and site1[2]=='A' and site1[3]=='T' and site1[4]=='T' and (site1[0]=='A' or site1[0]=='G') and (site1[5]=='C' or site1[5]=='T')):           
            print("Site No.: ",count,"\tat ",start1+1," - ",end1-l,"\tRE Site: ",site1,"\tRE Name: ApoI")
            cuts.append(start1+1)

    start1 += 1
    end1 += 1

plt.figure(figsize=(10,10))
x1 = np.linspace(1,l)
y1 = np.zeros(len(x1))
plt.plot(x1,y1,color='#1507ec',linewidth=8)
colors = ['red','orange','yellow','green','brown','violet']
for i in range(len(cuts)):
    y = np.linspace(0,9-i)
    x = cuts[i] * np.ones(len(y))
    plt.plot(x,y,color=colors[i],linewidth=2,linestyle=':')
    plt.text(cuts[i]-2,y[-1],'ApoI ('+str(cuts[i])+')',fontsize=12)
plt.xlabel('M.AaaS1ORF662P gene [length = '+str(l)+'nt]')
plt.ylabel('Cut positions for ApoI')
plt.title('Restriction Map for ApoI in M.AaaS1ORF662P gene')
plt.show()