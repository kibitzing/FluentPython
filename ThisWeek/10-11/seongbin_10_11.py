def get_squares_area(n):
    return n*n
def get_triangles_area(n):
    return n * n / 8 * (3 ** 0.5)

s = get_squares_area;
t = get_triangles_area;

print(s(3));
print(t(10));

##이름이 긴 함수를 짧게 표현하기
