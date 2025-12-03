N = int(input())

class Dish:
    def __init__(self, id, T, id1, id2, id3, id4):
        self.name = id
        self.T = T
        self.ingredients = [id1, id2, id3, id4]


dishes = []
for _ in range(N):
    ID, T, DI1, DI2, DI3, DI4 = list(map(int, input().split()))
    dish = Dish(ID, T, DI1, DI2, DI3, DI4)
    dishes.append(dish)

dishes.sort(key=lambda x: x.T)
# print([dish.name for dish in dishes])

def overlap(used, dish_ingredient) -> bool:
    for ingredient in dish_ingredient:
        if ingredient == 0:
            pass
        else:
            if ingredient in used:
                return True
    return False

ans = []

def dfs(current_index, memory, used_ingredients):
    for dish in memory:
        if dishes[current_index].T == dish.T:
            return

    if overlap(used_ingredients, dishes[current_index].ingredients):
        return

    memory.append(dishes[current_index])
    used_ingredients += dishes[current_index].ingredients

    if len(memory) == 3:
        if memory[0].T != memory[1].T and memory[1].T != memory[2].T and memory[0].T != memory[2].T:
            ans.append([dish.name for dish in memory[:]])

    for i in range(current_index+1, N):
        dfs(i, memory, used_ingredients)

    memory.pop()
    for ingredient in dishes[current_index].ingredients:
        used_ingredients.remove(ingredient)



for i in range(N):
    dfs(i, [], [])


if ans == []:
    print(-1)
else:
    ans.sort(key=lambda x: x[0])
    for dish_names in ans:
        print(" ".join([str(dish_name) for dish_name in dish_names]))