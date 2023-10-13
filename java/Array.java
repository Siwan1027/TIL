public class Array {
    public static void main(String[] args) {
        String[] weeks = new String[7];
        weeks[0] = "월";
        weeks[1] = "화";
        weeks[2] = "수";
        weeks[3] = "목";
        weeks[4] = "금";
        weeks[5] = "토";
        weeks[6] = "일";
        for (int i = 0; i < weeks.length; i++) {
            System.out.println(weeks[i]);
        } // 원래 내가 작성한 코드
        for (String week : weeks) {
            System.out.println(week);
        } // 이렇게도 가능하다 신기..

    }
}
