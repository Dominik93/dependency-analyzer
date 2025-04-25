import unittest
from maven.maven import Maven
from tests.mock_executor import MockExecutor


class MavenTestCase(unittest.TestCase):
    def test_maven(self):
        mock = {"mvn -f /path/sample dependency:tree -Dincludes=com.sample:dependency": "response"}
        maven = Maven("/path", MockExecutor(mock), ["com.sample:dependency"])

        actual = maven.dependency_tree("sample")

        self.assertEqual(actual, "response")


if __name__ == '__main__':
    unittest.main()
