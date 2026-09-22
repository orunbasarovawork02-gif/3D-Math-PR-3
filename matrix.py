import math


def mat_mult(A, B): 
    result = [[0] * 4 for _ in range(4)]

    for i in range(4):              
        for j in range(4):          
            total = 0
            for k in range(4):      
                total += A[i][k] * B[k][j]
            result[i][j] = total

    return result


def apply(M, point):
    p = [point[0], point[1], point[2], 1]   
    out = []
    for i in range(3):
        total = 0
        for k in range(4):
            total += M[i][k] * p[k]
        out.append(round(total, 6))
    return tuple(out)


def translation(dx, dy, dz):
    return [[1, 0, 0, dx],
            [0, 1, 0, dy],
            [0, 0, 1, dz],
            [0, 0, 0, 1]]


def scaling(kx, ky, kz):
    return [[kx, 0,  0,  0],
            [0,  ky, 0,  0],
            [0,  0,  kz, 0],
            [0,  0,  0,  1]]


def rotation_z(degrees):
    a = math.radians(degrees)
    c = round(math.cos(a), 10)
    s = round(math.sin(a), 10)
    return [[c, -s, 0, 0],
            [s,  c, 0, 0],
            [0,  0, 1, 0],
            [0,  0, 0, 1]]


def show(name, M):
    print(name)
    for row in M:
        print("   │" + "".join(f"{v:7.2f}" for v in row) + "  │")
    print()



T = translation(4, 0, 0)
S = scaling(3, 3, 3)
R = rotation_z(-90)


ST = mat_mult(S, T)  
TS = mat_mult(T, S)  

print("=== 1. МАСШТАБИРОВАНИЕ И ПЕРЕНОС ===")
show("S · T — сначала перенос, потом масштаб (Cube_A)", ST)
show("T · S — сначала масштаб, потом перенос (Cube_B)", TS)


RT = mat_mult(R, T)  
TR = mat_mult(T, R)  

print("=== 2. ПОВОРОТ И ПЕРЕНОС ===")
show("R · T — сначала перенос, потом поворот (Cube_C)", RT)
show("T · R — сначала поворот, потом перенос (Cube_D)", TR)


center = (0, 0, 0)
print("=== РЕЗУЛЬТИРУЮЩИЕ КООРДИНАТЫ ЦЕНТРА КУБА (0, 0, 0) ===")
print("  Cube_A (S · T) ->", apply(ST, center))
print("  Cube_B (T · S) ->", apply(TS, center))
print("  Cube_C (R · T) ->", apply(RT, center))
print("  Cube_D (T · R) ->", apply(TR, center))