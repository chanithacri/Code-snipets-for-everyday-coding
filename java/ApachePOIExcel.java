/**
 * Read/write Excel spreadsheets using Apache POI with workbook and sheet helpers.
 */

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * ApachePOIExcel: Read/write Excel with Apache POI.
 *
 * The helper methods avoid a hard dependency on Apache POI while still showing
 * how data could be structured for export. The returned data maps sheet names
 * to row/column values that can be fed into a workbook builder in a project
 * that includes POI.
 */
public class ApachePOIExcel {

    public static Map<String, List<List<String>>> buildWorkbookData(String sheetName, List<String> headers,
            List<List<String>> rows) {
        Map<String, List<List<String>>> workbook = new LinkedHashMap<>();
        List<List<String>> sheet = new ArrayList<>();
        sheet.add(new ArrayList<>(headers));
        sheet.addAll(rows);
        workbook.put(sheetName, sheet);
        return workbook;
    }

    public static List<String> headerRow(String... columns) {
        List<String> header = new ArrayList<>();
        for (String column : columns) {
            header.add(column);
        }
        return header;
    }
}
