class DynamicArray {
    private int[] arr;
    private int len;

    public DynamicArray(int capacity) {
        arr = new int[capacity];
        len = 0;
    }

    public int get(int i) {
        return arr[i];
    }

    public void set(int i, int n) {
        arr[i] = n;
    }

    public void pushback(int n) {
        if (len == arr.length) {
            this.resize();
        }
        arr[len] = n;
        len++;
    }

    public int popback() {
        int elem = arr[len-1];
        len--;
        return elem;
    }

    private void resize() {
        int[] newArr = new int[arr.length*2];
        for (int i = 0; i < len; i++) {
            newArr[i] = arr[i];
        }

        arr = newArr;
    }

    public int getSize() {
        return len;
    }

    public int getCapacity() {
        return arr.length;
    }
}
