def is_transitive(R):
    for a in R:
        for b in R:
            if a[1] == b[0]:
                if [a[0], b[1]] not in R:
                    return False
    return True

# Ejemplo de uso
R = [[2, 3], [3, 4], [2,4]]
print(is_transitive(R))

