
public class NayukiLexPermutationsDifficultAnswer {
	
	static boolean nextPermutation(int[] array) {
	    // Find longest non-increasing suffix
	    int i = array.length - 1;
	    while (i > 0 && array[i - 1] >= array[i])
	        i--;
	    // Now i is the head index of the suffix
	    
	    // Are we at the last permutation already?
	    if (i <= 0)
	        return false;
	    
	    // Let array[i - 1] be the pivot
	    // Find rightmost element that exceeds the pivot
	    int j = array.length - 1;
	    while (array[j] <= array[i - 1])
	        j--;
	    // Now the value array[j] will become the new pivot
	    // Assertion: j >= i
	    
	    // Swap the pivot with j
	    int temp = array[i - 1];
	    array[i - 1] = array[j];
	    array[j] = temp;
	    
	    // Reverse the suffix
	    j = array.length - 1;
	    while (i < j) {
	        temp = array[i];
	        array[i] = array[j];
	        array[j] = temp;
	        i++;
	        j--;
	    }
	    
	    // Successfully computed the next permutation
	    return true;
	} 
	    /* 
	     * Solution to Project Euler problem 24
	     * by Project Nayuki
	     * 
	     * https://www.nayuki.io/page/project-euler-solutions
	     * https://github.com/nayuki/Project-Euler-solutions
	     */


	    
	    	
	    	public static void main(String[] args) 
	    	{
	    		// Initialize
	    		int[] arr = {0,1,2,3,4,5,6,7,8,9};
	    		
	    		// Permute
	    		for (int i = 0; i < 999999; i++) {
	    			nextPermutation(arr);
	    		}
	    		
	    		// Format output
	    		String ans = "";
	    		
	    		for (int i = 0; i < arr.length; i++)
	    			ans += arr[i];
	    		
	    		System.out.println(ans);
	    	}
	    	
}


