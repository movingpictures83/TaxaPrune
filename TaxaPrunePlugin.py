import PyPluMA

class TaxaPrunePlugin:
   def input(self, filename):
      self.txtfile = open(filename, 'r')
      self.parameters = dict()
      for line in self.txtfile:
         contents = line.split('\t')
         self.parameters[contents[0]] = contents[1].strip()

      if len(PyPluMA.prefix()) != 0:
         self.parameters['otu'] = PyPluMA.prefix() + "/" + self.parameters['otu']
         self.parameters['tax'] = PyPluMA.prefix() + "/" + self.parameters['tax']

      self.otu_file = open(self.parameters['otu'], 'r')
      self.tax_file = open(self.parameters['tax'], 'r')

   def run(self):
       pass

   def output(self, filename):

      self.parameters['newotu'] = filename + "/" + self.parameters['newotu']
      self.parameters['newtax'] = filename + "/" + self.parameters['newtax']

      otu_filter_file = open(self.parameters['newotu'], 'w')
      tax_filter_file = open(self.parameters['newtax'], 'w')

      otu_filter_file.write(self.otu_file.readline()) #Header
      tax_filter_file.write(self.tax_file.readline()) #Header

      for line in self.tax_file:
          line = line.strip()
          contents = line.split(',')
          if (contents[5].find(self.parameters['pattern']) == -1):
              tax_filter_file.write(line+"\n")
              otu_filter_file.write(self.otu_file.readline())
          else:
              self.otu_file.readline() #Discard

