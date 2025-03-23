class Solution {
    public int findKthLargest(int[] nums, int k) {
        int size = nums.length;
        for (int i = (size / 2) - 1; i >= 0; i--) {
            maxHeap(nums, size, i);
        }

        for (int i = size - 1; i >= 0; i--) {
            swap(nums, i, 0);
            maxHeap(nums, i, 0);
            if (i == size - k) {
                return nums[size - k];
            }
        }

        return nums[size - k];
    }

    private void maxHeap(int[] nums, int size, int index) {
        int left = (2 * index) + 1, right = (2 * index) + 2;
        int maxIndex = index;

        if (left < size && nums[left] > nums[maxIndex]) {
            maxIndex = left;
        }

        if (right < size && nums[right] > nums[maxIndex]) {
            maxIndex = right;
        }
        if (maxIndex != index) {
            swap(nums, maxIndex, index);
            maxHeap(nums, size, maxIndex);
        }
    }

    private void swap(int[] arr, int index1, int index2) {
        int temp = arr[index1];
        arr[index1] = arr[index2];
        arr[index2] = temp;
    }
}
