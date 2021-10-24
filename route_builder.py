def route_builder(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        route_builder(graph, next, visited)
    return visited

graph = {'0': set(['1']),
         '1': set(['0', '2','25']),
         '2': set(['1','4','3']),
         '3': set(['2']),
         '4': set(['2', '5','24','21']),
         '5': set(['4','6','7']),
         '6': set(['5']),
         '7': set(['8','22','5']),
         '8': set(['9','7','11']),
         '9': set(['8']),
         '10': set(['9','11']),
         '11': set(['10','22','12']),
         '12': set(['13','11','15','19']),
         '13': set(['12']),
         '14': set(['15']),
         '15': set(['14','16','18']),
         '16': set(['15']),
         '17': set(['18']),
         '18': set(['15','19','23','17']),
         '19': set(['20','12','18']),
         '20': set(['21','23','19']),
         '21': set(['20','22','4']),
         '22': set(['7','11','21']),
         '23': set(['18','24','20']),
         '24': set(['25','4','23']),
         '25': set(['26','1','24']),
         '26': set(['25']) 
}

route_builder(graph, '0') 
