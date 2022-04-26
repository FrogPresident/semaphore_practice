def main():
    # sequence slicing
    r = list(range(10))  # 0 1 2 3 4 5 6 7 8 9
    print(r[slice(4, 8, 2)])
    print(r[5:8])
    print(r[:8])
    print(r[5:100])
    print(r[:])

    r_p = r[:]
    r[0] = 100
    print(r is r_p)
    print(r[0], r_p[0])

    print("----------------------------------")
    s = S()
    print(s["A":"z"])


class S:

    def __getitem__(self, item):
        if isinstance(item, slice):
            self._validate_slice(item)
            step = item.step or 1
            if step > 0:
                start = item.start or "a"
                end = item.stop or "z"
            else:
                start = item.start or "z"
                end = item.stop or "a"
            offset = 1 if step > 0 else -1
            return ''.join([chr(i) for i in range(ord(start), ord(end) + offset, step)])
        else:
            raise IndexError(f"{item} must be a slice")

    def _validate_slice(self, s: slice) -> None:
        if s.step == 0:
            raise IndexError(f'invalid {s}')
        values = [(s.start, str), (s.stop, str), (s.step, int)]
        for v, typ in values:
            if v is not None:
                if not isinstance(v, typ):
                    raise IndexError(f'invalid {s}')
                if issubclass(typ, str) and len(v) != 1:
                    raise IndexError(f'invalid {s}')


if __name__ == '__main__':
    main()
