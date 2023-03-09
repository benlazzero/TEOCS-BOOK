import tables

def NumToBin16(num):
  binAddress = "{0:b}".format(int(num))
  return binAddress.zfill(16)

class ASMCoder:
  def __init__(self, symbolTable, instructions):
    self.symbolTable = symbolTable # dictionary
    self.instructions = instructions # list
    self.currentVariable = 16
  
  def __call__(self): # assemble to .hack file
    with open('somehack.hack', 'w', encoding='utf-8') as f:
      for inst in self.instructions:
        instType = self.CheckInstruction(inst)
        if instType == 'A':
          bin = self.HandleAddress(inst)
          f.write(bin + '\n')
        if instType == 'L':
          self.HandleLabel(inst)
        if instType == 'C':
          bin2 = self.HandleComputation(inst)
          f.write(bin2 + '\n')
      f.close()
  
  def CheckInstruction(self, instruction):
    instructionType = ''
    if instruction[0] == '@':
      instructionType = 'A'
    elif instruction[0] == '(':
      instructionType = 'L'
    else:
      instructionType = 'C'
    return instructionType
  
  def HandleComputation(self, Cinst): # parsing...
    compStr = Cinst

    # if its a jump
    if ';' in compStr:
      cIndex = compStr.index(';')
      comp = compStr[:cIndex]
      jump = compStr[cIndex+1:]
      # handle the comp
      if comp in tables.compA0:
        comp = '1110' + tables.compA0[comp] + '000' 
        return comp + tables.jump[jump]
      if comp in tables.compA1:
        comp = '1111' + tables.compA1[comp] + '000' 
        return comp + tables.jump[jump]
    
    # if not jump
    cIndex = compStr.index('=')
    dest = compStr[:cIndex]
    calc = compStr[cIndex+1:]
    comp = ''
    if calc in tables.compA0:
        comp = '1110' + tables.compA0[calc] + tables.dest[dest] + '000' 
        return comp 
    if calc in tables.compA1:
        comp = '1111' + tables.compA1[calc] + tables.dest[dest] + '000' 
        return comp 
       

  def HandleAddress(self, Ainst):
    if Ainst[1:].isnumeric():
      return NumToBin16(Ainst[1:])
    isSymbol = Ainst[1:] in self.symbolTable 
    addressInt = 0
    if isSymbol:
      addressInt = self.symbolTable[Ainst[1:]]
      return NumToBin16(addressInt) 
    self.symbolTable[Ainst[1:]] = self.currentVariable
    self.currentVariable += 1
    return NumToBin16(Ainst[1:])
  
  def HandleLabel(self, Linst):
    labelSymbol = Linst[1:len(Linst)-1]
    return NumToBin16(self.symbolTable[labelSymbol])      
