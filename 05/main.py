import graphlib

test_data = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""


def main(data_raw):
    data = data_raw.split("\n")

    # Find index where the split is
    found_split = False
    data_01 = []
    data_02 = []
    for i, r in enumerate(data):
        if len(r.strip()) == 0:
            found_split = True
        elif found_split == False:
            data_01.append(r)
        else:
            data_02.append(r)

    good_count = 0
    bad_count = 0
    for l in data_02:
        ll = l.split(",")

        # Get relevent order definitions
        dd = [d.split("|") for d in data_01]
        dd = [(a, b) for a, b in dd if a in ll or b in ll]
        graph = {}
        for a, b in dd:
            if b not in graph:
                graph[b] = {a}
            elif b in graph:
                graph[b] = set(list(graph[b]) + list({a}))
        if True:

            def compare(
                a, b
            ):  # negative when A should be sorted left, B when should be sorted right
                if b in graph and a in graph[b]:
                    return -1
                elif a in graph and b in graph[a]:
                    return 1
                else:
                    return 0

            from functools import cmp_to_key

            out_sorted = ll.copy()
            out_sorted.sort(key=cmp_to_key(compare))
        else:
            ts = graphlib.TopologicalSorter(graph)
            tso = ts.static_order()
            out_sorted = [o for o in tso if o in ll]
            breakpoint()

        if True and str(ll) == str(out_sorted):
            middle_element = out_sorted[len(out_sorted) // 2]
            # print(out_sorted, middle_element)
            good_count += int(middle_element)
        else:

            middle_element = out_sorted[len(out_sorted) // 2]
            # print(out_sorted, middle_element)
            bad_count += int(middle_element)
    print(good_count)
    print(bad_count)


with open("input.txt", "r") as fh:
    data = fh.read()

main(data)
