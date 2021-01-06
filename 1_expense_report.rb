# Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input);
# apparently, something isn't quite adding up.
# Specifically, they need you to find the two entries that sum to 2020
# and then multiply those two numbers together.

# In your expense report, what is the product of the three entries that sum to 2020?

test_inputs = [1721, 979, 366, 299, 675, 1456]
inputs = [
    1779, 1737, 1537, 1167, 1804, 1873, 1894, 1446, 1262, 1608, 1430, 1421, 1826, 1718, 1888,
    1314, 1844, 248, 1812, 1627, 1605, 1641, 1126, 1051, 1839, 1067, 1685, 1800, 1383, 1415,
    1781, 1372, 1711, 1687, 1357, 1603, 1899, 1856, 1240, 1872, 1483, 1624, 1358, 1168, 1238,
    1585, 1159, 1409, 1615, 1258, 1412, 1468, 1912, 1840, 1681, 1700, 1031, 1757, 1911, 1096,
    1239, 1331, 1881, 1304, 1694, 1705, 1680, 820, 1744, 1245, 1922, 1545, 1335, 1852, 1318,
    1565, 1505, 1535, 1536, 1758, 1508, 1453, 1957, 1375, 1647, 1531, 1261, 1202, 1701, 1562,
    1933, 1293, 1828, 334, 1714, 1931, 1385, 1294, 1469, 1629, 1842, 1730, 1534, 1544, 1946,
    1805, 1188, 1684, 1875, 1623, 1248, 1347, 2006, 1191, 1037, 1387, 1903, 1746, 16, 952, 1246,
    384, 1518, 1738, 1269, 1747, 1423, 1764, 1666, 1999, 1776, 1673, 1350, 1698, 2004, 1235,
    1719, 1131, 1671, 1334, 1556, 1299, 1569, 1523, 1655, 1189, 1023, 1264, 1821, 1639, 1114,
    1391, 1154, 1225, 1906, 1481, 1728, 1309, 1682, 1662, 1017, 1952, 1948, 2010, 1809, 1394,
    1039, 1493, 1509, 1628, 1401, 1515, 1497, 1164, 1829, 1452, 1706, 1919, 1831, 1643, 1849,
    1558, 1162, 1328, 1432, 680, 1169, 1393, 1646, 1161, 1104, 1678, 1477, 1824, 1353, 1260,
    1736, 1777, 1658, 1715
]

def check_two(expense, remaining)
    result = remaining.find do |item|
        expense + item == 2020
    end
    return print "Product: #{expense * result}\n" if result
    check_two(remaining.shift, remaining) if remaining.any?
end

def check_three(inputs)
    i1 = 0
    i2 = 1
    i3 = 2
    count = inputs.length
    until i1 == count - 3
        until i2 == count - 2
            until i3 == count
                set = [inputs[i1], inputs[i2], inputs[i3]]
                return print "Product: #{set.reduce(:*)}\n" if set.sum == 2020 
                i3 += 1
            end
            i2 +=1
            i3 = i2 + 1
        end
        i1 += 1
        i2 = i1 + 1
        i3 = i2 + 1
    end
end

args = ARGV
inputs = test_inputs if args.include?('-t')

if args.include?('check_three')
    check_three(inputs)
else
    check_two(inputs.shift, inputs)
end