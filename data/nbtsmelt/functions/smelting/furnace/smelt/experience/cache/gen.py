for i in range(0, 9):
    begin = i + i * 10
    end = begin + 10

    content = ""

    for j in range(begin, end + 1):
        content += "execute if score #nbtsmelt.recipe.stored.index nbtsmelt.var matches {index} run function nbtsmelt:smelting/furnace/smelt/experience/cache/check/check_{index}\n".format(index=j)

    with open('{}_{}.mcfunction'.format(begin, end), 'w') as f:
        f.write(content)