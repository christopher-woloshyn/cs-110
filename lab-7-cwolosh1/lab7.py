import lsystem
def main():
    axiom = input("Please enter your axiom: ")
    iters = int(input("Please enter number of iterations: "))
    angle = int(input("Please enter the angle: "))
    distance = int(input("Please enter the distance: "))
    num_rules = int(input("Please enter the number of rules: "))
    rules = {}
    for i in range(num_rules):
        rule = input("Please enter an lsystem rule in the format 'character:substitution' : ")
        rule = rule.split(':')
        rules[rule[0].strip()] = rule[1].strip()
    result = lsystem.createLSystem(iters, axiom, rules)
    lsystem.drawLSystem(result, distance, angle)
main()
