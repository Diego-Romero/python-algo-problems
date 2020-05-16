class Sqrt:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        start = 2
        end = x // 2
        while start <= end:
            mid = start + (end - start) // 2
            num = mid * mid

            if num > x:
                end = mid - 1
            elif num < x:
                start = mid + 1
            else:
                return mid

        print(start, end)
        return end


if __name__ == '__main__':
    solution = Sqrt()

    print(solution.mySqrt(8))
