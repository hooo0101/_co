class Assembler:
    def __init__(self):
        self.symbol_table = {}
        self.instructions = []
        self.machine_code = []

    def parse(self, lines):
        # 第一遍：解析符號
        address = 0
        for line in lines:
            line = line.strip()
            if ":" in line:  # 標籤
                label = line.split(":")[0]
                self.symbol_table[label] = address
            else:
                self.instructions.append(line)
                address += 1

        # 第二遍：生成機器碼
        for line in self.instructions:
            parts = line.split()
            op = parts[0]
            if op == "LOAD":
                self.machine_code.append(0x01)
            elif op == "STORE":
                self.machine_code.append(0x02)
            elif op == "ADD":
                self.machine_code.append(0x03)
            elif op == "JMP":
                label = parts[1]
                address = self.symbol_table[label]
                self.machine_code.append(0x04)
                self.machine_code.append(address)

    def assemble(self, asm_code):
        lines = asm_code.strip().split("\n")
        self.parse(lines)
        return self.machine_code


# 測試程式碼
asm_code = """
START: LOAD 10
       ADD 20
       STORE 30
       JMP START
"""

assembler = Assembler()
machine_code = assembler.assemble(asm_code)
print("機器碼:", machine_code)

