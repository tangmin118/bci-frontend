import csv

with open('BCI-001.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # 跳过表头
    rows = list(reader)
    
    print(f"总行数: {len(rows)}")
    print(f"前10行label: {[r[6] for r in rows[:10]]}")
    print(f"前100行中0的数量: {sum(1 for r in rows[:100] if r[6]=='0')}")
    print(f"前1000行中0的数量: {sum(1 for r in rows[:1000] if r[6]=='0')}")
    
    # 找出第一个label=1和label=2的位置
    first_1 = next((i for i, r in enumerate(rows) if r[6]=='1'), None)
    first_2 = next((i for i, r in enumerate(rows) if r[6]=='2'), None)
    print(f"第一个label=1出现在第 {first_1} 行")
    print(f"第一个label=2出现在第 {first_2} 行")
    
    # 检查前10000行的分布
    print(f"\n前10000行分布:")
    print(f"  0(集中): {sum(1 for r in rows[:10000] if r[6]=='0')}")
    print(f"  1(中性): {sum(1 for r in rows[:10000] if r[6]=='1')}")
    print(f"  2(放松): {sum(1 for r in rows[:10000] if r[6]=='2')}")
