
print("메뉴를 선택해주세요")

print("----------")

print("1. 커피 800")
print("2. 크로 2000")
print("3. 페퍼 1000")
print("4. 이온 1500")
print("5. 스무 3000")

choice = int(input("1~5"))

print("-----------")
if(choice == 1) :
    itemPrice = 800
elif(choice == 2):
    itemPrice = 2000
elif(choice == 3):
    itemPrice = 1000
elif(choice == 4):
    itemPrice = 1500
elif(choice == 5):
    itemPrice = 3000
else:
    itemPrice = 0


print(choice, "를 선택하셨습니다")
print(itemPrice, "를 넣어주세요.")

print("-----------")
note10000 = int(input("10,000 : "))
note5000 = int(input("5,000 : "))
note1000 = int(input("1,000 : "))
note500 = int(input("500 : "))
note100 = int(input("100 : "))
note50 = int(input("50: "))
note10 = int(input("10: "))

total = note10000 * 10000 + note5000 *5000 + note1000*1000 + note500 * 500 + note100 * 100 + note50*50 + note10*10

print("-----------")

print("입력한 금액 : " , total)

if (total < itemPrice):
    print("돈이 부족합니다.")
    print("돈은 불우 이웃 돕기에 사용됩니다.")
    print("농담이고 돈 돌려드립니다.")
    namuji = total
else :
    namuji = total - itemPrice

print("-----------")

print("잔돈 받으세요 : ", namuji)
print("또롱 또롱 또롱 ")
print("-----------")
nam10000 = namuji // 10000
namuji = namuji % 10000

nam5000 = namuji // 5000
namuji = namuji % 5000


nam1000 = namuji // 1000
namuji = namuji % 1000


nam500 = namuji // 500
namuji = namuji % 500


nam100 = namuji // 100
namuji = namuji % 100


nam50 = namuji // 50
namuji = namuji % 50


nam10 = namuji // 10
namuji = namuji % 10

print("10000원권 : ", nam10000)


print("5000원권 : ", nam5000)

print("1000원권 : ", nam1000)

print("500원권 : ", nam500)

print("100원권 : ", nam100)

print("50원권 : ", nam50)

print("10원권 : ", nam10)




