public class LinkedList {
    protected class Node {
        public int val;
        public Node next;

        public Node(int v, Node n) {
            val = v;
            next = n;
        }
    }

    private Node head;

    public LinkedList() {
        head = null;
    }

    public int get(int index) {
        Node n = head;
        if (n == null) return -1;

        for (int i = 0; i < index; i++) {
            if (n.next == null) {
                return -1;
            }
            n = n.next;
        }
        return n.val;
    } 

    public void insertHead(int val) {
        Node t = head;
        head = new Node(val, t);
    }

    public void insertTail(int val) {
        Node n = head;
        if (n == null) {
            head = new Node(val, null);
            return;
        }
        while (n.next != null) {
            n = n.next;
        }
        n.next = new Node(val, null);
    }

    public boolean remove(int index) {
        if (head == null) {
            return false;
        }

        if (index == 0) {
            head = head.next;
            return true;
        }

        Node n = head;
        for (int i = 0; i < index - 1; i++) {
            if (n.next == null) {
                return false;
            }
            n = n.next;
        }
        
        if (n.next == null) { // try to remove 1 more than last
            return false;
        }
        n.next = n.next.next;

        return true;
    }

    public ArrayList<Integer> getValues() {
        ArrayList<Integer> nodes = new ArrayList<>();

        Node n = head;
        if (n == null) return nodes;
        
        while (n != null) {
            nodes.add(n.val);
            n = n.next;
        }

        return nodes;
    }
}
