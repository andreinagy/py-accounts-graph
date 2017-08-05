# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import FileFinder as f
import ParserING as parserIng

if __name__ == "__main__":
    print("Python Bank Accounts CSV parser")

for file in f.findFilesInDirectory(f.cwd(), ".csv"):
    parserIng.parseFile(file)

