public class HelloWorld {
    public static void main(String[] args) {
        String a = new String("hello"); // 객체를 새로 생성해서 추가
        String b = "java"; // literal 표기법
        String c = "hello";
        StringBuffer sb = new StringBuffer(); // StringBuffer char 형으로 이뤄진 리스트 같은 느낌?
        sb.append("hell");
        sb.insert(0,"welcome ");
        int[] ods = {1,3,5,7,9};

        System.out.println(a.equals(b)); // false 출력
        System.out.println(a.equals(c)); // true 출력
        System.out.println(sb);
        System.out.println(ods); // 이렇게 출력하면 배열의 주소값을 리턴한다.
        System.out.println(ods[0]);
    }
}
