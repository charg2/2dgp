import sys;

i = 432;
a = 'a';
ㅁ = 'ㅁ';
str = '.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;.........;';

print(len(a));
print(len(ㅁ));
print(sys.getsizeof(i));
print("'a' : ", sys.getsizeof(a));
print("string의 사이즈",sys.getsizeof(str));
print("'ㅁ' : ", sys.getsizeof(ㅁ)); #캐릭를 기본

b_a:bytearray;

