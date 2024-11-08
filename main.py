#Function: This program determines if a student will be admitted or rejected.
#Input:  Interactive
#Output: Accept or Reject

# Get input and convert to correct data type for testScore and classRank
testScore = input("Enter test score: ")
classRank = input("Enter class rank: ")

# Test using admission requirements and print Accept or Reject
if int(testScore) >= 90:
  if int(classRank) >= 25:
    print("Accept")
  else:
    print("Reject")
else:
  if int(testScore) >= 80:
    if int(classRank) >= 50:
      print("Accept")
    else:
      print("Reject")
  else:
    if int(testScore) >= 70:
      if int(classRank) >= 75:
        print("Accept")
      else:
        print("Reject")
    else:
      print("Reject")
