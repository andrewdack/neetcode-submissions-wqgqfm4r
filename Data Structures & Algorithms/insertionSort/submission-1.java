// Definition for a pair
// class Pair {
//     int key;
//     String value;
//
//     Pair(int key, String value) {
//         this.key = key;
//         this.value = value;
//     }
// }
public class Solution {
    public List<List<Pair>> insertionSort(List<Pair> pairs) {
        List<List<Pair>> output = new ArrayList<List<Pair>>();
        if (pairs.size() > 0) {
            output.add(new ArrayList<>(pairs));
        }
        for (int i = 1; i < pairs.size(); i++) {
            for (int j = 0; j < i; j++) {
                if (pairs.get(i).key < pairs.get(j).key) {
                    Pair element = pairs.get(i);
                    pairs.remove(i);
                    pairs.add(j, element);
                }
            }
            output.add(new ArrayList<>(pairs));
        }
        return output;
    }
}
