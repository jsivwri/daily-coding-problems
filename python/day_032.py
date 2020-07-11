# JP SIVERTSEN-WRIGHT - DAILY CODING PROBLEM 32

# This problem was asked by Jane Street.

# Suppose you are given a table of currency exchange rates, represented as a 2D array. Determine whether there is a possible arbitrage: that is, whether there is some sequence of trades you can make, starting with some amount A of any currency, so that you can end up with some amount greater than A of that currency.

# There are no transaction costs and you can trade fractional quantities.

class Node:
    def __init__(self, name):
        self.name = name
        self.connected_nodes = {}
    
    def add_connection(self, name, weight):
        self.connected_nodes[name] = weight


def determine_arbitrage(currency_exchanges):
    exchange_graph = []
    products = []

    for currency_index in range(len(currency_exchanges)):
        exchange_graph.append(Node(currency_index))

        for rate_index in range(len(currency_exchanges[currency_index])):
            exchange_graph[currency_index].add_connection(rate_index, currency_exchanges[currency_index][rate_index])

    initial_start_node = exchange_graph[0]
    initial_start_node_name = exchange_graph[0].name
    initial_next_nodes_and_weights = initial_start_node.connected_nodes.items()
    initial_visited_nodes = [initial_start_node.name]
    initial_current_product = 1

    queue = [(initial_next_nodes_and_weights, initial_visited_nodes, initial_current_product)]

    while queue != []:
        next_nodes_and_weights, visited_nodes, current_product = queue.pop(0)
        next_nodes = [entry[0] for entry in next_nodes_and_weights]
        
        for key in next_nodes:
            if key == initial_start_node_name:
                products.append(current_product*next_nodes_and_weights[key][1])

            if key not in visited_nodes:
                node = exchange_graph[key]
                visited_nodes += [key]
                queue += [(node.connected_nodes.items(), visited_nodes, current_product*next_nodes_and_weights[key][1])]

    for product in products:
        if product > 1.0:
            return True

    return False 

# TEST CODE
assert determine_arbitrage([[1, 2],[0.5, 1]]) == False
assert determine_arbitrage([[1, 2],[2, 1]]) == True