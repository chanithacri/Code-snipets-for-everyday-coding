/**
 * url_query_params: Parse and build URL query params.
 * Include minimal usage example at bottom.
 */

export function parseQuery(search) {
  const queryString = search.startsWith("?") ? search.slice(1) : search;
  const params = new URLSearchParams(queryString);
  const result = {};
  for (const [key, value] of params.entries()) {
    if (result[key] !== undefined) {
      const existing = Array.isArray(result[key]) ? result[key] : [result[key]];
      existing.push(value);
      result[key] = existing;
    } else {
      result[key] = value;
    }
  }
  return result;
}

export function buildQuery(params) {
  const search = new URLSearchParams();
  Object.entries(params).forEach(([key, value]) => {
    if (Array.isArray(value)) {
      value.forEach((item) => search.append(key, item));
    } else if (value !== undefined && value !== null) {
      search.append(key, value);
    }
  });
  const qs = search.toString();
  return qs ? `?${qs}` : "";
}

/* Usage example:
const parsed = parseQuery("?page=2&tag=js&tag=node");
const query = buildQuery({ page: 2, tag: ["js", "node"] });
*/
