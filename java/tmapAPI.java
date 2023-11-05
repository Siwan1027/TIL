

public class tmapAPI {
    public static void main(String[] args) {
        Counter myCounter = new Counter();
        System.out.println(myCounter.count);
        Updater myUpdater = new Updater();
        myUpdater.update(myCounter.count);
        System.out.println(myCounter.count);

    }
}