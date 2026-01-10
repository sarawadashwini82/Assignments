scores=[50,80,45,78,42]
total_scores=sum(scores)
print("total_scores:",total_scores)
avg_scores=total_scores/len(scores)
print("avg_scores:",avg_scores)
count=0
for i in range(len(scores)):
    if scores[i]>avg_scores:
        count+=1
print("count of scores above average are:",count)        
