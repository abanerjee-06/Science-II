from RE import RE_sites

pairs = {
    'A': 'T',
    'C': 'G',
    'G': 'C',
    'T': 'A'
}

DNA_seq = ""
f = open("seq.txt","r")
DNA_seq = f.read().replace('\n','').replace('\r','').replace(' ','')

l = len(DNA_seq)
site_length = [6,8]
start1 = 0
start2 = 0
end1 = 6
end2 = 8
L1 = []
L2 = []
count = 0

print("UNIQUE SEQUENCES WITH LENGTH 6:\n")
while (end1-l < 6):
    if (end1 <= l):
        site1 = DNA_seq[start1:end1:] 
        if (site1[5]==pairs[site1[0]] and site1[4]==pairs[site1[1]] and site1[3]==pairs[site1[2]]):
            if (site1 not in L1):
                count += 1
                L1.append(site1)
                if (site1 in RE_sites):
                    if (site1 == "GCTAGC"):             # BmtI and NheI have the same restriction recognition sites, although they cut at different points
                        print("Site No.: ",count,"\tat ",start1+1," - ",end1,"\tRE Site: ",site1,"\tRE Name: BmtI , NheI")
                    else:    
                        print("Site No.: ",count,"\tat ",start1+1," - ",end1,"\tRE Site: ",site1,"\tRE Name: ",RE_sites[site1])
                else:
                    print("Site No.: ",count,"\tat ",start1+1," - ",end1,"\tRE Site: ",site1)
        if (site1[1]=='A' and site1[2]=='A' and site1[3]=='T' and site1[4]=='T' and (site1[0]=='A' or site1[0]=='G') and (site1[5]=='C' or site1[5]=='T')):           # recognition site for ApoI is RAATTY. R = A or G  and   Y = C or T
            print("Site No.: ",count,"\tat ",start1+1," - ",end1,"\tRE Site: ",site1,"\tRE Name: ApoI")
    else:
        site1 = DNA_seq[start1:l:]+DNA_seq[0:end1-l:]
        if (site1[5]==pairs[site1[0]] and site1[4]==pairs[site1[1]] and site1[3]==pairs[site1[2]]):
            if (site1 not in L1):
                count += 1
                L1.append(site1)
                if (site1 in RE_sites):
                    if (site1 == "GCTAGC"):             # BmtI and NheI have the same restriction recognition sites, although they cut at different points
                        print("Site No.: ",count,"\tat ",start1+1," - ",end1,"\tRE Site: ",site1,"\tRE Name: BmtI , NheI")
                    else:    
                        print("Site No.: ",count,"\tat ",start1+1," - ",end1-l,"\tRE Site: ",site1,"\tRE Name: ",RE_sites[site1])
                else:
                    print("Site No.: ",count,"\tat ",start1+1," - ",end1-l,"\tRE Site: ",site1)
        if (site1[1]=='A' and site1[2]=='A' and site1[3]=='T' and site1[4]=='T' and (site1[0]=='A' or site1[0]=='G') and (site1[5]=='C' or site1[5]=='T')):           # recognition site for ApoI is RAATTY. R = A or G  and  Y = C or T
            print("Site No.: ",count,"\tat ",start1+1," - ",end1-l,"\tRE Site: ",site1,"\tRE Name: ApoI")

    start1 += 1
    end1 += 1

count = 0

print("\nUNIQUE SEQUENCES WITH LENGTH 8:\n")
while (end2-l < 6):
    if (end2 <= l):
        site2 = DNA_seq[start2:end2:]
        if (site2[7]==pairs[site2[0]] and site2[6]==pairs[site2[1]] and site2[5]==pairs[site2[2]] and site2[4] == pairs[site2[3]]):
            if (site2 not in L2):
                count += 1
                L2.append(site2)
                print("Site No.: ",count,"\tat ",start2+1," - ",end2,"\tRE Site: ",site2)
        if (site2[0]=='C' and site2[7]=='G' and site2[2]=='C' and site2[5]=='G' and site2[3]=='C' and site2[4]=='G' and (site1[1]=='A' or site1[1]=='G') and (site1[6]=='C' or site1[6]=='T')):       # recognition site for SgrAI is CRCCGGYG
            print("Site No.: ",count,"\tat ",start2+1," - ",end2,"\tRE Site: ",site2,"\tRE Name: SgrAI")                             # R = A or G  and   Y = C or T
    else:
        site2 = DNA_seq[start2:l:]+DNA_seq[0:end2-l:]
        if (site2[7]==pairs[site2[0]] and site2[6]==pairs[site2[1]] and site2[5]==pairs[site2[2]] and site2[4] == pairs[site2[3]]):
            if (site2 not in L2):
                count += 1
                L2.append(site2)
                print("Site No.: ",count,"\tat ",start2+1," - ",end2-l,"\tRE Site: ",site2)
        if (site2[0]=='C' and site2[7]=='G' and site2[2]=='C' and site2[5]=='G' and site2[3]=='C' and site2[4]=='G' and (site1[1]=='A' or site1[1]=='G') and (site1[6]=='C' or site1[6]=='T')):       # recognition site for SgrAI is CRCCGGYG
            print("Site No.: ",count,"\tat ",start2+1," - ",end2-l,"\tRE Site: ",site2,"\tRE Name: SgrAI")                             # R = A or G  and   Y = C or T

    start2 += 1
    end2 += 1

