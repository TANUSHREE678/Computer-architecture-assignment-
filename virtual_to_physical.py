# Virtual Address to Physical Address Translation

page_size = 1024

page_table = {
    0: 5,
    1: 2,
    2: None,
    3: 7
}

addresses = [500, 1500, 2500, 3500]

print("Virtual Address | Page No | Offset | Frame No | Physical Address")
print("---------------------------------------------------------------")

for va in addresses:
    page_no = va // page_size
    offset = va % page_size

    if page_table[page_no] is None:
        print(va, "             |", page_no, "      |", offset,
              "    | Not present | Page fault")
    else:
        frame = page_table[page_no]
        pa = frame * page_size + offset

        print(va, "            |", page_no, "      |", offset,
              "    |", frame, "         |", pa)
