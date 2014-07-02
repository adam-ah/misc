import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map.Entry;

import org.apache.curator.RetryPolicy;
import org.apache.curator.framework.CuratorFramework;
import org.apache.curator.framework.CuratorFrameworkFactory;
import org.apache.curator.framework.api.GetDataBuilder;
import org.apache.curator.retry.ExponentialBackoffRetry;
import org.apache.zookeeper.WatchedEvent;
import org.apache.zookeeper.Watcher;
import org.apache.zookeeper.ZooDefs.Perms;
import org.apache.zookeeper.data.ACL;
import org.apache.zookeeper.data.Id;
import org.apache.zookeeper.data.Stat;

public class App {
    private static final int MAX_RETRIES = 3;
    private static final int BASE_SLEEP_TIME_MS = 1000;
    private static final String CONFIG_PATH = "/rabbit/config";
    private static final String CONNECTION_STRING = "127.0.0.1:2181";

    public static void main(final String[] args) throws Exception {
        final RetryPolicy retryPolicy =
            new ExponentialBackoffRetry(BASE_SLEEP_TIME_MS, MAX_RETRIES);
        final CuratorFramework client =
            CuratorFrameworkFactory.newClient(CONNECTION_STRING, retryPolicy);
        client.start();

        final Watcher watcher = new Watcher() {
            @Override
                public void process(final WatchedEvent event) {
                    try {
                        final GetDataBuilder getDataBuilder = client.getData();
                        final byte[] configBytes = getDataBuilder.forPath(CONFIG_PATH);
                        final String config = new String(configBytes);
                        System.out.println(event.getType() + ", " + config);

                        // Re-create the watcher.
                        client.getData().usingWatcher(this).forPath(CONFIG_PATH);
                    } catch (final Exception ex) {
                        System.out.println(ex);
                    }
                }
        };

        final Stat stat = client.checkExists().forPath(CONFIG_PATH);

        if (stat != null) {
            System.out.println("Found node: " + stat);

            final GetDataBuilder getDataBuilder = client.getData();
            final byte[] configBytes = getDataBuilder.forPath(CONFIG_PATH);
            final String config = new String(configBytes);

            System.out.println("Data: " + config);

            client.setData().forPath(CONFIG_PATH, "Hello from Java.".getBytes());

            // Delete the data.
            // client.delete().forPath(CONFIG_PATH);
        } else {
            final ArrayList<ACL> acls = new ArrayList<>();
            // Restrict access to this node to localhost clients only.
            acls.add(new ACL(Perms.ALL, new Id("ip", "127.0.0.1")));
            client.create().creatingParentsIfNeeded().withACL(acls)
                .forPath(CONFIG_PATH, "Hello from Java.".getBytes());

            System.out.println("Created node: " + CONFIG_PATH);
        }

        // Create the first watcher.
        client.getData().usingWatcher(watcher).forPath(CONFIG_PATH);

        // Wait and listen to changes.
        Thread.sleep(300 * 1000);
    }
}

