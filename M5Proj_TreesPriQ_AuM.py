from binary_expression_tree import BinaryExpressionTree

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
if __name__ == "__main__":
    main()