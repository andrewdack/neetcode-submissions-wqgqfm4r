class Solution {
    public int evalRPN(String[] tokens) {
        // push numbers to the stack
        // if see an operand, use it on the last two items of the stack
        // combine those two items into one and push onto the stack
        Stack<Integer> stack = new Stack<>();

        for (String s: tokens) {
            int temp;
            switch (s) {
                case "+":
                    stack.push( stack.pop() + stack.pop());
                    break; 
                case "-":
                    temp = stack.pop();
                    stack.push(stack.pop() - temp);
                    break;
                case "*":
                    stack.push(stack.pop() * stack.pop());
                    break;
                case "/":
                    temp = stack.pop();
                    stack.push(stack.pop() / temp);
                    break;
                default: // just a normal int
                    stack.push(Integer.parseInt(s));
            }
        }
        return stack.peek();
    }
}
