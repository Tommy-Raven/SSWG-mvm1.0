def export_graphviz(wf, out_path="./build/workflow_graph.dot"):
    graph = wf.get("dependency_graph", {})
    nodes = graph.get("nodes", [])
    edges = graph.get("edges", [])
    with open(out_path, "w") as f:
        f.write("digraph workflow {\n")
        for n in nodes:
            f.write(f'  "{n}" [shape=box];\n')
        for e in edges:
            f.write(f'  "{e[0]}" -> "{e[1]}";\n')
        f.write("}\n")
    return out_path
