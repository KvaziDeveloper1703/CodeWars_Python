'''
You are working with a Binary Search Tree (BST). Before starting this kata, make sure you have already implemented the methods __eq__, __ne__, and __str__ for the Tree class.

Problem Description:
Imagine you have a binary search tree. Over time, you notice that some nodes are accessed more frequently than others. Since the access time of a node depends on its depth in the tree, it would be ideal to place the frequently accessed nodes closer to the root.

Each node has a weight attribute that represents how often it is accessed.
    + The cost of a node = (weight of the node) × (depth of the node);
    + The depth of the root is defined as 1, and each level below increases depth by 1;
    + The cost of the tree = sum of the costs of all its nodes.

Tasks:
    1) Implement cost(tree)
    A function that takes a tree and returns its cost.

    2) Implement make_min_tree(nodes)
    A function that takes a non-empty sorted list of nodes (in ascending order, without duplicates) and returns a tree with minimal cost.
        + Input: a sorted list of nodes (unique values);
        + Output: a binary search tree arranged in such a way that the overall cost is minimized;
        + Constraints: input list length ≤ 100.

Note: The known solution is O(n²) in space and O(n³) in time, but there might be more efficient ways.

Вы работаете с деревом бинарного поиска (Binary Search Tree, BST). Перед началом этого ката убедитесь, что у вас уже реализованы методы __eq__, __ne__ и __str__ для класса Tree (как было в предыдущем задании).

Описание задачи:
Представьте, что у вас есть бинарное дерево поиска. Со временем вы замечаете, что некоторые узлы используются чаще других. Поскольку время доступа к узлу зависит от его глубины, желательно, чтобы часто используемые узлы находились ближе к корню.

У каждого узла есть атрибут weight — это число, показывающее, насколько часто узел используется.
    + Стоимость узла = (вес узла) × (глубина узла);
    + Глубина корня всегда равна 1, а у дочернего узла глубина = (глубина родителя + 1);
    + Стоимость дерева = сумма стоимостей всех узлов.

Задачи:
    1) Реализовать функцию cost(tree)
    Она принимает дерево и возвращает его стоимость.

    2) Реализовать функцию make_min_tree(nodes)
    Она принимает непустой отсортированный список узлов (по возрастанию, без повторов) и строит дерево с минимальной стоимостью.
        Вход: отсортированный список уникальных узлов;
        Выход: бинарное дерево поиска, оптимально сбалансированное по стоимости;
        Ограничение: длина списка ≤ 100.

Замечание: известное решение работает за O(n²) по памяти и O(n³) по времени, но, возможно, существуют более эффективные алгоритмы.
'''

class Tree(object):
    def __init__(self, root, left=None, right=None):
        assert root and type(root) == Node
        if left:
            assert type(left) == Tree and left.root < root
        if right:
            assert type(right) == Tree and root < right.root
        self.left = left
        self.root = root
        self.right = right

    def is_leaf(self):
        return not (self.left or self.right)

    def __str__(self):
        if self.is_leaf():
            return f'[{self.root}]'
        left_str = str(self.left) if self.left else '_'
        right_str = str(self.right) if self.right else '_'
        return f'[{left_str} {self.root} {right_str}]'

    def __eq__(self, other):
        if not isinstance(other, Tree):
            return False
        return (self.root == other.root and
                self.left == other.left and
                self.right == other.right)

    def __ne__(self, other):
        return not self == other

class Node(object):
    def __init__(self, value, weight=1):
        self.value = value
        self.weight = weight

    def __str__(self):
        return '%s:%d' % (self.value, self.weight)

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

def cost(tree, depth=1):
    if tree is None:
        return 0
    current_node_cost = tree.root.weight * depth
    left_subtree_cost = cost(tree.left, depth + 1) if tree.left else 0
    right_subtree_cost = cost(tree.right, depth + 1) if tree.right else 0
    return current_node_cost + left_subtree_cost + right_subtree_cost

def make_min_tree(node_list):
    number_of_nodes = len(node_list)
    prefix_weight_sums = [0]
    for node in node_list:
        prefix_weight_sums.append(prefix_weight_sums[-1] + node.weight)

    def sum_weight(left_index_inclusive, right_index_inclusive):
        return prefix_weight_sums[right_index_inclusive + 1] - prefix_weight_sums[left_index_inclusive]

    dp_min_cost = [[0] * number_of_nodes for _ in range(number_of_nodes)]
    dp_root_choice = [[-1] * number_of_nodes for _ in range(number_of_nodes)]

    for index in range(number_of_nodes):
        dp_min_cost[index][index] = node_list[index].weight
        dp_root_choice[index][index] = index

    for segment_length in range(2, number_of_nodes + 1):
        for left_index in range(0, number_of_nodes - segment_length + 1):
            right_index = left_index + segment_length - 1
            total_segment_weight = sum_weight(left_index, right_index)
            best_segment_cost = float('inf')
            best_root_index = -1
            for root_index in range(left_index, right_index + 1):
                left_cost = dp_min_cost[left_index][root_index - 1] if root_index > left_index else 0
                right_cost = dp_min_cost[root_index + 1][right_index] if root_index < right_index else 0
                candidate_cost = left_cost + right_cost + total_segment_weight
                if candidate_cost < best_segment_cost:
                    best_segment_cost = candidate_cost
                    best_root_index = root_index
            dp_min_cost[left_index][right_index] = best_segment_cost
            dp_root_choice[left_index][right_index] = best_root_index

    def build_tree(left_index_inclusive, right_index_inclusive):
        if left_index_inclusive > right_index_inclusive:
            return None
        root_index = dp_root_choice[left_index_inclusive][right_index_inclusive]
        left_subtree = build_tree(left_index_inclusive, root_index - 1)
        right_subtree = build_tree(root_index + 1, right_index_inclusive)
        return Tree(node_list[root_index], left_subtree, right_subtree)

    return build_tree(0, number_of_nodes - 1)