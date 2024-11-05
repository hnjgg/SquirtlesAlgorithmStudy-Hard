def solution(m, n, X, Y, balls):
    return [min((X - nx) * (X - nx) + (Y - ny) * (Y - ny) for nx, ny in [(2*m-x, y), (-x, y), (x, 2*n-y), (x, -y)] if not (X == nx and (Y < y) == (y < ny) or Y == ny and (X < x) == (x < nx))) for x, y in balls]
