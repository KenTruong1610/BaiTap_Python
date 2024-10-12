"""
Bài 33: Sử dụng import random để tạo game kéo búa bao.
import random
"""
def game():
    choices = ['kéo', 'búa', 'bao']
    player = input("Bạn hãy lựa chọn kéo, búa hoặc bao: ").upper()
    computer = random.choice(choices).upper()
    print("Bạn đã lựa chọn: ", player)
    print("Máy đã lựa chọn: ", computer)
    if player == computer:
        return "Hòa!"
    if (player == "kéo" and computer == "bao") or (player == "búa" and computer == "kéo") or (player == "bao" and computer == "búa"):
        return "Bạn đã thắng!"
    else:
        return "Bạn đã thua!"
print(game())
