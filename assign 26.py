feedback={"Positive": 45, "Neutral": 18, "Negative": 7}
total_feedback=sum(feedback.values())
print(total_feedback)
high_feedback=max(feedback,key=feedback.get)
print(high_feedback)
