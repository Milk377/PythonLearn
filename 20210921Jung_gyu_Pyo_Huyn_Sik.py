
import re

print("----------------------------------")
f = open("C:/Users/teddy/PycharmProjects/pythonProject/input.txt" , 'r')

while True:
    print("Input value to excute. \n")
    print("1. Find Jungsoo \n")
    print("2. Find SIlsu \n")
    print("3. Find String sangsu \n")
    print("4. Find Comment Moon \n")
    print("5. Quit Program. \n")

    val = int(input())

    if(val>=1 and val <= 5):
        print("-------------------")
        print("You input : " ,val)
        print("-------------------")
        if(val == 1):
            print("Find junsgsu \n")


            while True:
                line = f.readline()
                if not line: break

                # 정수를 찾는 로직

                ## 음의 정수를 찾는 로직도 추가해야한다.
                ## \b 앞에 [+-] 을 붙이면 된다.
                ## 양의정수, 음의정수, 0 을 찾는 로직 OK
                matchObj = re.match(r'[+-]\b[0-9]+\b',line)

                if(matchObj != None ):
                    print(matchObj.group())

                # 정수 찾는 로직 종료

                else:
                    print("Can't Find it")
                    print("-------------------")


            # 한자리수, 한자리수 이상, 양수, 음수
            # 한자리수 = 0 ~ 9 까지 가능
            # 두자리수이상 = 앞자리가 0이 아니어야 함
            # 음수 = 맨 앞의 기호가 - 이어야함
            # 양수 = 맨 앞의 기호가 없어야 함


        elif(val ==2):

            print("Find Silsu \n")

            while True:
                line = f.readline()
                if not line: break

                # 실수를 찾는 로직

                ## 음의 정수를 찾는 로직도 추가해야한다.
                ## \b 앞에 [+-] 을 붙이면 된다.
                ## 양의정수, 음의정수, 0 을 찾는 로직 OK
                matchObj = re.match('^[+-]?\d*(\.?\d*)$',line)

                if(matchObj != None ):
                    print(matchObj.group())

                # 실수 찾는 로직 종료

                else:
                    print("Can't Find it")
                    print("-------------------")


        elif(val == 3):
            print("Find StringSangsu \n")


            while True:
                line = f.readline()
                if not line: break

                # 스트링 상수를 찾는 로직
                matchObj = re.match('[a-zA-Z\s]+',line)

                if(matchObj != None ):
                    print(matchObj.group())

                # 스트링 상수를 찾는 로직 종료


        elif(val == 4):
            print("Find Comment moon \n")

            while True:
                line = f.readline()
                if not line: break

                # 스트링 상수를 찾는 로직 # 띄어쓰기 포함을 위해 \s 를 추가함.
                matchObj = re.match('#{1}[a-zA-Z0-9.\s]+',line)

                if(matchObj != None ):
                    print(matchObj.group())



        elif(val == 5):
            print("Quit program. bye bye")

            break

        print("-------------------")



    else:
        print("input right value from 1 to 5. \n")









f.close()