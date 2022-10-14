#tic-tac-toe!

print("tic-tac-toe!", "\n"*2)
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
used_positions= []
position = input("\nChoose a position for X: (x,y/ x= column, y=row)")
used_positions.append(position)
posicao = position.split(",")
column = int(posicao[0])
row = int(posicao[1])

map[row-1][column-1] = "❌"
print(f"{row1}\n{row2}\n{row3}")
caunter=1

while caunter!=9:
    if caunter % 2 != 0:
        position = input("\nChoose a position for ⭕️: (x,y/ x= column, y=row)")
        if position in used_positions:
            print("Position already used, choose anotherPosition already used, choose another!")
        else:
            used_positions.append(position)
            posicao = position.split(",")
            column = int(posicao[0])
            row = int(posicao[1])
            map[row-1][column-1] = "⭕️"
            print(f"{row1}\n{row2}\n{row3}")
            caunter += 1
        if row1.count('⭕️') == 3 or row2.count('⭕️') == 3 or row3.count('⭕️') == 3:
            print("⭕️ win!")
            break
        if map[0][0] == "⭕️" and map[1][0] == "⭕️" and map[2][0] == "⭕️":
            print("⭕️ win!")
            break
        if map[0][1] == "⭕️" and map[1][1] == "⭕️" and map[2][1] == "⭕️":
            print("⭕️ win!")
            break
        if map[0][2] == "⭕️" and map[1][2] == "⭕️" and map[2][2] == "⭕️":
            print("⭕️ win!")
            break
        if map[0][0] == "⭕️" and map[1][1] == "⭕️" and map[2][2] == "⭕️":
            print("⭕️ win!")
            break
        if map[0][2] == "⭕️" and map[1][1] == "⭕️" and map[2][0] == "⭕️":
            print("⭕️ win!")
            break

    else:
        position = input("\nChoose a position for ❌: (x,y/ x= column, y=row)")
        if position in used_positions:
            print("Position already used, choose anotherPosition already used, choose another!")
        else:
            used_positions.append(position)
            posicao = position.split(",")
            column = int(posicao[0])
            row = int(posicao[1])
            map[row-1][column-1] = "❌"
            print(f"{row1}\n{row2}\n{row3}")
            caunter += 1
        if row1.count('❌') == 3 or row2.count('❌') == 3 or row3.count('❌') == 3:
            print("❌ win!")
            break
        if map[0][0] == "❌" and map[1][0] == "❌" and map[2][0] == "❌":
            print("❌ win!")
            break
        if map[0][1] == "❌" and map[1][1] == "❌" and map[2][1] == "❌":
            print("❌ win!")
            break
        if map[0][2] == "❌" and map[1][2] == "❌" and map[2][2] == "❌":
            print("❌ win!")
            break
        if map[0][0] == "❌" and map[1][1] == "❌" and map[2][2] == "❌":
            print("❌ win!")
            break
        if map[0][2] == "❌" and map[1][1] == "❌" and map[2][0] == "❌":
            print("❌ win!")
            break

        if caunter == 9:
            print("Draw!")
            
print("Draw!")