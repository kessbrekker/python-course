age = int(input("Yaşınız: "))

if age >= 99:
    print("Ehliyet almak için çok yaşlısın!")
elif age >= 18:
    print("Ehliyet Alabilirsin!")
elif age <= 0:
    print("Daha doğmadın!")
else:
    print("Ehliyet Alamazsın!")
