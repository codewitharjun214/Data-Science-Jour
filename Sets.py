# # # # # # # # # # # Lets Start The Sets in Python
# # # # # # # # # #
# # # # # # # # # # #set creation
# # # # # # # # # #
# # # # # # # # # # s = {10,20,30,40,50}
# # # # # # # # # # print(s)
# # # # # # # # # #
# # # # # # # # # # # lets make addition of two sets
# # # # # # # # # #
# # # # # # # # # # set1 = {10,20,30,40,50}
# # # # # # # # # # set2 = {10,70,50,80}
# # # # # # # # # #
# # # # # # # # # # set3 = set1.union(set2)
# # # # # # # # # #
# # # # # # # # # # print(set3)
# # # # # # # # # #
# # # # # # # # # # # Add elements
# # # # # # # # # #
# # # # # # # # # # s = {1,3,4}
# # # # # # # # # # s.add(5)
# # # # # # # # # # print(s)
# # # # # # # # #
# # # # # # # # # #Remove Elements
# # # # # # # # #
# # # # # # # # # s = {1,3,4}
# # # # # # # # # s.remove(3)
# # # # # # # # # print(s)
# # # # # # # # #
# # # # # # # #
# # # # # # # # # Lets union the sets (combine)
# # # # # # # #
# # # # # # # # a = {1,2,3,4,5}
# # # # # # # # b = {5,6,7,8,9}
# # # # # # # #
# # # # # # # # print(a | b)
# # # # # # # #
# # # # # # # # c = a.union(b)
# # # # # # # # print(c)
# # # # # # # #
# # # # # # #
# # # # # # # # Lets intersection values ( common values will print)
# # # # # # #
# # # # # # # a = {1,2,3,4,5}
# # # # # # # b = {5,2,5,8,9}
# # # # # # #
# # # # # # # print(a & b)
# # # # # # #
# # # # # # # c = a.intersection(b)
# # # # # # # print(c)
# # # # # # #
# # # # # # # difference (this remove same value and gives us what set we want without that value)
# # # # # #
# # # # # # a = {1,2,3,4}
# # # # # # b = {4,5,6,7}
# # # # # #
# # # # # # print(a - b)
# # # # # # print(b - a)
# # # # # #
# # # # #
# # # # # # Symmetric Difference ( this is used to new set without same values)
# # # # #
# # # # # a = {1, 2, 3}
# # # # # b = {3, 4, 5}
# # # # #
# # # # # print(a ^ b)
# # # # #
# # # # #
# # # #
# # # # # Loop in set
# # # #
# # # # s = {10, 20, 30}
# # # #
# # # # for i in s:
# # # #     print(i)
# # # #
# # # # # print only even numbers
# # # #
# # # # s = {1, 2, 3, 4, 5, 6}
# # # #
# # # # for i in s:
# # # #     if i % 2 == 0:
# # # #         print(i)
# # #
# # # # Count Elements in Set
# # #
# # # s = {5, 10, 15}
# # #
# # # count = 0
# # #
# # # for i in s:
# # #     count += 1
# # #
# # # print("Total elements:", count)
# # #
# # #
# #
# # # Sum of Elements
# #
# # s = {1, 2, 3, 4}
# #
# # total = 0
# #
# # for i in s:
# #     total += i
# #
# # print("Sum:", total)
# #
#
# # lets make a sorted loop
#
# s = {3, 1, 2}
#
# for i in sorted(s):
#     print(i)
#
