# #
# import sys
# liczba_argumentow + len(sys.argv)
# historia = None
#
# if liczba_argumentow == 1:
#     print('za mało argumentow')
# elif sys.argv[1] =='saldo':
#     if liczba_argumentow != 4 and liczba_argumentow > 2:
#         print('zla liczba argumentów dla polecenia "saldo".')
#     else:
#         saldo = []
#         while True:
#             historia = input()
#             if historia == 'saldo':
#                 saldo.append(int(input))
#                 saldo.append(input())
#             if historia == 'stop':
#                 break
#         if liczba_argumentow == 4:
#             saldo.append(int(sys.argv[2]))
#             saldo.append(sys.argv[3])
# elif sys.argv[1] == 'sprzedaz':
#     pass
# print(saldo)

saldo = 0
magazyn = {}

akcje = []
while True:
    akcja = input()
    if akcja == 'stop':
        break
    if akcja == 'saldo':
        pass

    historia.append(akcja)


print(historia)
