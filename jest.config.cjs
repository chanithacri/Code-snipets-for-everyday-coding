// Jest configuration for JavaScript snippets and tests.
// Sets Node environment and limits discovery to tests/javascript specs.
module.exports = {
  testEnvironment: "node",
  roots: ["<rootDir>"],
  testMatch: ["**/tests/javascript/**/*.test.js"],
  transform: {},
};
