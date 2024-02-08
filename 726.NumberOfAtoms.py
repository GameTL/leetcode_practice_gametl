import re

# Need to use Recursion
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # return the mass of (NO), (NO2)
        # temp_element =
        # temp_compound =
        same_element = False
        def dismantleCompound(sub_compound): #  ( inside here )2
            basic_pattern = r'([A-Z][a-z]*)(\d*)'
            basic_matches = re.findall(basic_pattern, formula)

            x = []
            for element, quantity in basic_matches:
                print(element, quantity)
                if quantity == '':
                    quantity = 1
                else:
                    quantity = int(quantity)
                x.append((element, quantity))
            return x


            temp_compound = 0
            if formula[i].isupper(): #Start of a element
                temp_compound += 1
                i += 1
            elif formula[i].islower():
                pass
            elif formula[i] == "(":
                # in the bracket
                i+= 1



        # compound_pattern = r'\(([A-Z][A-Z]*[a-z]*)\)(\d)'
        # compound_matches = re.findall(compound_pattern, formula)
        # return basic_matches
x = Solution()

# print(x.hammingWeight(00000000000000000000000010000000))
# print(x.hammingWeight(00000000000000000000000000001011))
# print(x.countOfAtoms("Mg(OH)2"))
print(x.countOfAtoms("MgO2"))
print(x.countOfAtoms("NO2"))
print(x.countOfAtoms("SO3"))
print(x.countOfAtoms("H2O")),
# print(x.countOfAtoms("K4(ON(SO3)2)2"))