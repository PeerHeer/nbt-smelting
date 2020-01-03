comment = (
    '# By: shraavan97\n'
    '# 18 Nov 2019\n\n'
)

lines = ['scoreboard players operation $bit nbtsmelt.temp = $uid nbtsmelt.temp',
'scoreboard players operation $bit nbtsmelt.temp %= $3 nbtsmelt.int',
'execute if score $bit nbtsmelt.temp matches 0 run data modify storage nbtsmelt:playerdb.temp root.filtered^ append from storage nbtsmelt:playerdb.temp root.filtered&[{bit^:0b}]',  # noqa
'execute if score $bit nbtsmelt.temp matches 0 run data modify storage nbtsmelt:playerdb.temp root.leftover append from storage nbtsmelt:playerdb.temp root.filtered&[{bit^:1b}]',  # noqa
'execute if score $bit nbtsmelt.temp matches 0 run data modify storage nbtsmelt:playerdb.temp root.leftover append from storage nbtsmelt:playerdb.temp root.filtered&[{bit^:2b}]',  # noqa
'execute if score $bit nbtsmelt.temp matches 1 run data modify storage nbtsmelt:playerdb.temp root.filtered^ append from storage nbtsmelt:playerdb.temp root.filtered&[{bit^:1b}]',  # noqa
'execute if score $bit nbtsmelt.temp matches 1 run data modify storage nbtsmelt:playerdb.temp root.leftover append from storage nbtsmelt:playerdb.temp root.filtered&[{bit^:0b}]',  # noqa
'execute if score $bit nbtsmelt.temp matches 1 run data modify storage nbtsmelt:playerdb.temp root.leftover append from storage nbtsmelt:playerdb.temp root.filtered&[{bit^:2b}]',  # noqa
'execute if score $bit nbtsmelt.temp matches 2 run data modify storage nbtsmelt:playerdb.temp root.filtered^ append from storage nbtsmelt:playerdb.temp root.filtered&[{bit^:2b}]',  # noqa
'execute if score $bit nbtsmelt.temp matches 2 run data modify storage nbtsmelt:playerdb.temp root.leftover append from storage nbtsmelt:playerdb.temp root.filtered&[{bit^:0b}]',  # noqa
'execute if score $bit nbtsmelt.temp matches 2 run data modify storage nbtsmelt:playerdb.temp root.leftover append from storage nbtsmelt:playerdb.temp root.filtered&[{bit^:1b}]',  # noqa
'scoreboard players operation $uid nbtsmelt.temp /= $3 nbtsmelt.int',
'execute store result score $size nbtsmelt.temp if data storage nbtsmelt:playerdb.temp root.filtered^[]',
'execute if score $size nbtsmelt.temp matches 0..1 run data modify storage nbtsmelt:playerdb.output root.player set from storage nbtsmelt:playerdb.temp root.filtered^[0]',  # noqa
'execute if score $size nbtsmelt.temp matches 2.. run function nbtsmelt:playerdb/_get/bit!']

for i in range(0, 20):
    out = [comment]

    for line in lines:
        if i == 19 and line.startswith('execute if score $size nbtsmelt.temp matches 2..'):
            out.append('execute if score $size nbtsmelt.temp matches 2.. run tellraw @a {"text": "ERROR, ERROR", "color":"red"}')  # noqa
            continue
        line = line.replace('!', str(i+1))
        line = line.replace('^', str(i))

        if i - 1 < 0:
            line = line.replace('&', '')
        else:
            line = line.replace('&', str(i-1))

        out.append(line)

    with open(f'bit{i}.mcfunction', 'w') as file:
        file.write('\n'.join(out))