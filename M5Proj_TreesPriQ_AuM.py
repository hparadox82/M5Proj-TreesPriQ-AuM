from binary_expression_tree import BinaryExpressionTree
from triage_sys import TriageSys
def main():
    print("----Binary Expression Tree----")

    #using postfix data example in instructions:
    test_cases = [
        "5 3 +",
        "8 2 - 3 +",
        "5 3 8 * +",
        "6 2 / 3 +",
        "5 8 + 3 -",
        "5 3 + 8 *",
        "8 2 3 * + 6 -",
        "5 3 8 * + 2 /",
        "8 2 + 3 6 * -",
        "5 3 + 8 2 / -"]
    tree=BinaryExpressionTree()

    for postfix in test_cases:
        try:
            #build tree
            tree.clear_tree()
            tree.buld_from_postfix(postfix)

            #get results and represents
            infix=tree.infix_trav()
            pfix_res=tree.postfix_trav()
            result = tree.evaluate_tree()
            
            #print
            print(f"Infix: {infix}\n")
            print(f"Postfix: {pfix_res}\n")
            print(f"Result: {result}\n")
            #exception handling
        except Exception as e:
            print(f"Error processing '{postfix}': {e}")

print("\n\n----Hospital Triage System----\n")

triage = TriageSys()
#test data from instructions:
incoming_patients = [("Sofia", 5),("Bob", 2),("Charlie",4),("Diana",3),("Eli",1),("Tom",4),("Alice",5),("Rachel", 4)]
print(f"\nInputting {len(incoming_patients)} arriving patients to the system: \n")

for name, severity in incoming_patients:
    try:
        triage.add_patient(name, severity)
        print(f"Registered: {name:<10} (Severity: {severity})")
    except ValueError as e:
        print(f"Issue registering {name}: {e}")

print("\n----------------------------\n")
print(f"Total Patients in Waiting Room: {triage.size()}\n")

#looking at first patient:
next_up=triage.peek_next()
if next_up:
    print(f">Next Patient: {next_up[0]} (Severity: {next_up[1]})")

#ordering patients:
print("\n----Prioritizing Patients----\n")
print(f"{'Order:<6'} | {'Name:<10'} | {'Severity'}")
print("\n-----------------------------\n")

count = 1
while not triage.is_empty():
    name, severity=triage.process_next()
    print(f"{count:<6} | {name:<10} | {severity}")
    count +=1

print("\n-----------------------------\n")
if triage.is_empty():
    print("\nAll Patients treated and discharged!\n")


if __name__ == "__main__":
    main()