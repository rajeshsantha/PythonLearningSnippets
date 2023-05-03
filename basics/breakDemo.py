successful = False
for num in range(3):
    print("Attempt")
    if successful:
        print(f"succesful!!!! at {num} time")
        break
else:
    print(f"attempted {num+1} times and failed")
