num_tests = int(raw_input())
for test_index in range(num_tests):
    (num_nodes, num_edges) = map(int, raw_input().split())
    for edge_index in range(num_edges):
        (from_node, to_node, weight) = map(int, raw_input().split())
    print(num_nodes + num_edges)
