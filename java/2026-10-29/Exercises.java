/*
 * Java practice: 2026-10-29 (warm-up)
 *
 * Six small methods, starting very easy. Replace each
 *     throw new UnsupportedOperationException("TODO");
 * with your code.
 *
 * Run the checks:   java Exercises.java
 * Each exercise prints PASS, FAIL (with what went wrong) or TODO.
 *
 * ---------------------------------------------------------------------------
 * Python -> Java cheat sheet
 * ---------------------------------------------------------------------------
 *   Python                          Java
 *   ------                          ----
 *   x = 5                           int x = 5;            (say the type, end with ;)
 *   name = "Ishan"                  String name = "Ishan";
 *   True / False                    true / false
 *   def add(a, b):                  static int add(int a, int b) {
 *       return a + b                    return a + b;
 *                                   }                     (braces instead of indents)
 *   if x > 5:                       if (x > 5) {
 *   elif x > 2:                     } else if (x > 2) {
 *   else:                           } else {
 *   for n in nums:                  for (int n : nums) {
 *   len(nums)                       nums.length
 *   len(word)                       word.length()
 *   f"{a}:{b}"                      a + ":" + b
 *   # comment                       // comment
 * ---------------------------------------------------------------------------
 */
public class Exercises {

    // Ex1 (Strings, return)
    // Return a greeting.
    //   greet("Ishan") -> "Hello, Ishan!"
    // Hint: join Strings with +   e.g. "Hi " + name
    static String greet(String name) {
        String hi = "Hello, ";
        return hi + name+"!";
    }


    // Ex2 (int, arithmetic)
    // Return the sum of two whole numbers.
    //   add(2, 3) -> 5
    static int add(int a, int b) {
        int sum = a + b;
        return sum;
    }


    // Ex3 (boolean, %)
    // Return true if n is even, false otherwise.
    //   isEven(4) -> true      isEven(7) -> false
    // Hint: same % as Python. n % 2 is 0 for even numbers. Compare with ==
    static boolean isEven(int n) {
        if (n%2 == 0){
            return true;
        }
        else{
            return false;
        }
    }


    // Ex4 (if / else if / else)
    // Return "positive", "negative" or "zero".
    //   sign(5) -> "positive"   sign(-2) -> "negative"   sign(0) -> "zero"
    static String sign(int n) {
        if (n > 0){
            return "positive";
        } else if (n == 0){
            return "zero";
        } else{
            return "negative";
        }
    }


    // Ex5 (arrays, for loop)
    // Return the total of all numbers in the array.
    //   sum(new int[]{1, 2, 3}) -> 6
    // Hint: start with  int total = 0;  then loop with  for (int n : nums) { ... }
    static int sum(int[] nums) {
        int total = 0;
        for (int n : nums){
            total += n;
        }
        return total;
    }


    // Ex6 (putting it together: your Python Ex1, now in Java)
    // Convert milliseconds to "m:ss". Seconds always have 2 digits.
    //   formatDuration(255000) -> "4:15"     formatDuration(65000) -> "1:05"
    // Hint: / between two ints already drops the decimal (like Python's //).
    //       String.format("%d:%02d", minutes, seconds)  works like f"{minutes}:{seconds:02d}"
    static String formatDuration(int ms) {
        int total_seconds = ms / 1000;
        int minutes = total_seconds / 60;
        int seconds = total_seconds % 60;
        return String.format("%d:%02d", minutes, seconds);
    }


    // -----------------------------------------------------------------------
    // Checks: no need to edit below this line.
    // -----------------------------------------------------------------------

    interface Call { Object run(); }

    static void check(String label, Object[][] cases) {
        try {
            for (Object[] c : cases) {
                Object got = ((Call) c[0]).run();
                Object expected = c[1];
                if (!expected.equals(got)) {
                    System.out.println("FAIL " + label + ": " + c[2]
                            + "\n       expected " + expected + "\n       got      " + got);
                    return;
                }
            }
            System.out.println("PASS " + label);
        } catch (UnsupportedOperationException e) {
            System.out.println("TODO " + label);
        } catch (Exception e) {
            System.out.println("FAIL " + label + ": threw " + e);
        }
    }

    public static void main(String[] args) {
        check("Ex1", new Object[][] {
            { (Call) () -> greet("Ishan"), "Hello, Ishan!", "greet(\"Ishan\")" },
            { (Call) () -> greet("World"), "Hello, World!", "greet(\"World\")" },
        });
        check("Ex2", new Object[][] {
            { (Call) () -> add(2, 3), 5, "add(2, 3)" },
            { (Call) () -> add(-4, 4), 0, "add(-4, 4)" },
        });
        check("Ex3", new Object[][] {
            { (Call) () -> isEven(4), true, "isEven(4)" },
            { (Call) () -> isEven(7), false, "isEven(7)" },
            { (Call) () -> isEven(0), true, "isEven(0)" },
        });
        check("Ex4", new Object[][] {
            { (Call) () -> sign(5), "positive", "sign(5)" },
            { (Call) () -> sign(-2), "negative", "sign(-2)" },
            { (Call) () -> sign(0), "zero", "sign(0)" },
        });
        check("Ex5", new Object[][] {
            { (Call) () -> sum(new int[] {1, 2, 3}), 6, "sum({1, 2, 3})" },
            { (Call) () -> sum(new int[] {}), 0, "sum({})" },
        });
        check("Ex6", new Object[][] {
            { (Call) () -> formatDuration(255000), "4:15", "formatDuration(255000)" },
            { (Call) () -> formatDuration(65000), "1:05", "formatDuration(65000)" },
            { (Call) () -> formatDuration(600000), "10:00", "formatDuration(600000)" },
        });
    }
}
