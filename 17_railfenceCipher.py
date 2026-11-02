def railfenceCipher(text , rails , mode):
    if mode == "E":
        fence = [""] *rails

        row =0
        direction = 1

        for char in text:
            fence[row]+=char
            if row==0:
                direction = 1
            elif row == rails -1:
                direction = -1
            
            row += direction
        return "".join(fence)

    else:

        pattern = []
        row = 0
        direction = 1

        for i in range(len(text)):
            pattern.append(row)

            if row ==0:
                direction =1
            elif row == rails- 1:
                direction = -1

            row += direction

        counts = [pattern.count(i) for i in range(rails)]
        fence= []
        start = 0
         
        for count in counts:
            fence.append(list(Text[start:start +count]))
            start +=count

        for r in pattern:
            result += fence[r]. pop(0)
            return result
text = input("Enter the text: ")

rails = 3

print("\nNumber of rails:", rails)
print("1. Encryption")
print("2. Decryption")

choice = input("Enter your choice: ")

if choice == "1":
    encrypted = railFenceCipher(text, rails, "E")
    print("Encrypted text:", encrypted)

elif choice == "2":
    decrypted = railFenceCipher(text, rails, "D")
    print("Decrypted text:", decrypted)

else:
    print("Invalid choice")