BASE = 3

comment = (
    '# By: shraavan97\n'
    '# 14 Nov 2019\n'
    '# \n'
    '#> Make the player entry\n'
)

lines = ['scoreboard players operation $bit nbtsmelt.temp = $uid nbtsmelt.temp',
'execute store result storage nbtsmelt:playerdb.global root.players[-1].bit{bit} byte 1 run scoreboard players operation $bit nbtsmelt.temp %= ${base} nbtsmelt.int',
'# tellraw @s [{"text":"", "color":"gold"}, {"text":"bit{bit}: "}, {"score":{"name":"$bit", "objective":"nbtsmelt.temp"}}]']

out = [comment]
for i in range(0, 999):
    if i ** BASE > (2**31-1):
        break
    out.append(lines[0])
    out.append(lines[1].format(bit=i, base=BASE))
    out.append(lines[2])

with open(f'uid_to_bits.mcfunction', 'w') as file:
    file.write('\n'.join(out))
