class ASMParser:
  def __init__(self, constants, hackasm):
    self.symbols = constants # dictionary
    self.assembly = hackasm
    self.instructions = self.GetInstructions()
    self.symbolTable = self.GetLabels()

  def GetInstructions(self):
    asmRmvd = self.assembly
    instructions = []
    splitLines = asmRmvd.split('\n')
    for line in splitLines:
      try: 
        cIndex = line.index('//')
        nIndex = len(line)
        line = line[:cIndex] + line[nIndex:]
        if len(line) > 0:
          instructions.append(line.strip())
      except ValueError:
        if len(line) > 0:
          instructions.append(line.strip())
    return(instructions)
  
  def GetLabels(self):
    symbolTable = self.symbols # dictionary
    instructions = self.instructions # list
    currentLine = -1
    for item in instructions:
      itemParsed = item
      if item[0] == '(':
        itemParsed = item[1:len(item)-1]
        symbolTable[itemParsed] = currentLine+1
        continue
      currentLine += 1
    return symbolTable
        

        
        
    
    
    
    
    










   

      



   
    


    
