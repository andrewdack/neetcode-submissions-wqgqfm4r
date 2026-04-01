class MinStack {

    class StackNode {
        int val;
        StackNode next;
        StackNode prevMin;

        public StackNode(int val) {
            this.val = val;
            next = null;
            prevMin = null;
        }
    }

    StackNode head;
    StackNode min;

    public MinStack() {
        head = null;
        min = null;
    }
    
    public void push(int val) {
        if (head == null) {
            head = new StackNode(val);
            min = head;
            head.prevMin = head;
            return;
        }

        StackNode temp = head;
        head = new StackNode(val);
        head.next = temp;
        head.prevMin = min;

        if (head.val < min.val) {
            min = head;
        }
        
    }
    
    public void pop() {
        min = head.prevMin;
        head = head.next;
    }
    
    public int top() {
        return head.val;   
    }
    
    public int getMin() {
        return min.val;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */