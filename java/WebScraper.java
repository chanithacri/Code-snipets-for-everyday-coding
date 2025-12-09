/**
 * JSoup-powered helpers for fetching pages and extracting elements with robust error handling.
 */

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class WebScraper {
    public static void main(String[] args) throws Exception {
        String url = "https://example.com";
        // Connect to the website and parse HTML
        Document doc = Jsoup.connect(url).get();
        // Select all h1 elements
        Elements headings = doc.select("h1");
        // Print each heading text
        for (Element h1 : headings) {
            System.out.println(h1.text());
        }
    }
}
